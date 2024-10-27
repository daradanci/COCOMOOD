from asyncio import Task
from datetime import datetime
from enum import Enum
from typing import Optional

import typing
import asyncio

from app.system.dataclasses import TGDC

from .dataclasses import DialogueState
from app.store.bot.api.dataclasses import (
    CallbackQueryUpdate,
    MessageUpdate,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    MessageEntity,
    MessageToSend,
    answerCallbackQuery,
    CallbackQuery,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


class Updater:
    def __init__(self, app: "Application"):
        self.app = app
        self.is_running = False
        self.handle_task: list[Task] | None

    async def start(self):
        print("manager init")
        self.is_running = True
        self.handle_task = asyncio.gather(
            self.handle_update(),
            self.handle_update(),
        )

    async def stop(self):
        self.is_running = False
        self.handle_task.cancel()

    class Commands(Enum):
        START = "/start"
        STARTREAD = "/startread"
        READ = "/read"
        

    async def handle_update(self):
        while self.is_running:
            message = await self.app.store.work_queue.get()
            try:
                self.app.logger.info(f"Manager: Новое сообщение {message}")
                if type(message) is CallbackQueryUpdate:
                    await self.handle_callbackquery(message)
                elif type(message) is MessageUpdate:
                    await self.handle_message(message)
            except Exception as inst:
                self.app.logger.error("Manager: Была получена ошибка:", exc_info=inst)
            finally:
                self.app.store.work_queue.task_done()

    async def handle_message(self, message: MessageUpdate):
        if message.message.text.startswith("/"):
            command = message.message.text.split("@")
            if len(command) == 1 or command[1] == "necron_alex_game_bot":
                await self.handle_command(message)
        else:
            await self.handle_text_message(message)

    async def handle_command(self, message: MessageUpdate):
        match message.message.text.split("@")[0]:
            case self.Commands.START.value:
                await self.handle_start(message)
            case self.Commands.STARTREAD.value:
                await self.handle_start_read(message)
            case self.Commands.READ.value:
                await self.handle_read(
                    message.message.chat.id, message.message.message_thread_id
                )
            case _:
                await self.handle_wrong_command(message)

    async def handle_start(self, message: MessageUpdate):
        chat_id = message.message.chat.id
        chat = await self.app.store.accessor.get_chat(chat_id)
        if not chat:
            await self.app.store.accessor.add_chat(chat_id)
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text='''Вы запустили меня. Теперь авторизуйтесь, для этого введите Логин и пароль в формате: login|password''',
            )
        else:
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text="Вы уже запустили меня",
            )
        

    async def handle_start_read(self, message: MessageUpdate):
        chat_id = message.message.chat.id
        chat = await self.app.store.accessor.get_chat(chat_id)
        if DialogueState(chat.state) == DialogueState.AUTH:
            await self.app.store.accessor.edit_chat_state(chatid=chat_id,state="READING")
            inline_keyboard = InlineKeyboardMarkup(
                                    inline_keyboard=[[
                                        
                                            InlineKeyboardButton(
                                                text="Закончить чтение",
                                                callback_data=f"end",
                                            ),
                                        
                                        
                                            InlineKeyboardButton(
                                                text="Удалить сессию",
                                                callback_data=f"abort",
                                            )
                                           
                                    ]]
                                )
            data = await self.handle_to_queue(
                reply_markup=inline_keyboard,
                chat_id=message.message.chat.id,
                message_thread_id=message.message.message_thread_id,
                text="Чтение началось",
            )
            ob = await self.app.store.accessor.add_readtime(chat.userid)
            sessions = await self.app.store.accessor.get_last_30_readtime(chat.userid)
            if sessions:
                if len(sessions.data) >2:
                    asyncio.create_task(
                    self.handle_notification(
                    )
                )

        else:
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text="Вы сейчас не в состоянии начать чтение",
            )
        
    async def handle_notification(
        self,
    ):
        pass

    async def handle_read(
        self,
        message: MessageUpdate
    ):
        chat_id = message.message.chat.id
        chat = await self.app.store.accessor.get_chat(chat_id)
        if DialogueState(chat.state) == DialogueState.AUTH:
            await self.app.store.accessor.edit_chat_state(chatid=chat_id,state="SCORE")
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text='''Вы перешли в режим оценки. Введите название произведения (примерное), и его оценку (1-10). Формат вводимых данных: Название|оценка''',
            )
        else:
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text="Вы сейчас не в учесть книгу",
            )
        

    async def handle_wrong_command(self, message: MessageUpdate):
        await self.handle_to_queue(
            chat_id=message.message.chat.id,
            message_thread_id=message.message.message_thread_id,
            reply_to_message_id=message.message.message_id,
            text=f"Такой команды не существует",
        )



    async def handle_callbackquery(self, callback: CallbackQueryUpdate):
        callback_query = callback.callback_query
        chat_id = callback_query.message.chat.id
        chat = await self.app.store.accessor.get_chat(chat_id)
        if DialogueState(chat.state) == DialogueState.READING:
            callback_data = callback_query.data
            if callback_data == "end":
                await self.handle_endread(chat=chat, callback=callback_query)
            else:
                await self.handle_abort(chat=chat, callback=callback_query)
        else:
            answerCallbackQuery(
                        callback_query_id=callback_query.id,
                        text="Вы не в состоянии выполнить это действие",
                        show_alert=True,
                    )


    async def handle_endread(self, chat: TGDC, callback: CallbackQuery):
        readtime = await self.app.store.accessor.get_last_readtime(chat.userid)
        await self.app.store.accessor.add_readtime_end(readtime.id)
        await self.app.store.accessor.edit_chat_state(chatid=chat.chatid,state="REVIEW")
        await self.handle_to_queue(
                    chat_id=chat.chatid,
                    message_thread_id=callback.message.message_thread_id,
                    text='''Напишите свою заинтересованность в формате: Произведение1--оценка (1-10)|Произведение2--оценка (1-10) ''',
                )
        

    async def handle_abort(self, chat: TGDC, callback: CallbackQuery):
        readtime = await self.app.store.accessor.get_last_readtime(chat.userid)
        await self.app.store.accessor.del_readtime(readtime.id)
        await self.app.store.accessor.edit_chat_state(chatid=chat.chatid,state="AUTH")
        await self.handle_to_queue(
                    chat_id=chat.chatid,
                    message_thread_id=callback.message.message_thread_id,
                    text='''Последняя сессия чтения удалена''',
                )
        
    async def handle_text_message(self, message: MessageUpdate):
        chat_id = message.message.chat.id
        chat = await self.app.store.accessor.get_chat(chat_id)

        if DialogueState(chat.state) == DialogueState.INIT:
            await self.handle_login(chat=chat, message=message)
        elif DialogueState(chat.state) == DialogueState.REVIEW:
            await self.handle_review(chat=chat, message=message)
            
        elif DialogueState(chat.state) == DialogueState.SCORE:
            await self.handle_score(chat=chat, message=message)
        else:
            await self.handle_to_queue(
                chat_id=chat_id,
                message_thread_id=message.message.message_thread_id,
                text='''Зачем ты пишешь чтото в чат 2к мусор, ты такой убежище''',
            )
    

    async def handle_login(self, chat: TGDC, message: MessageUpdate):

        text = message.message.text
        credentials = text.split('|')
        
        if len(credentials)==2:
            logindata = await self.app.store.accessor.get_by_login(credentials[0])
            if logindata is None:
                await self.handle_to_queue(
                        chat_id=chat.chatid,
                        message_thread_id=message.message.message_thread_id,
                        text='''Неправильный логин''',
                    )
            else:
                if logindata.is_password_valid(credentials[1]):
                    await self.handle_to_queue(
                        chat_id=chat.chatid,
                        message_thread_id=message.message.message_thread_id,
                        text=f'''Успешная авторизация {logindata.name}''',
                    )
                    await self.app.store.accessor.add_chat_user(chatid=chat.chatid,userid=logindata.id)
                    await self.app.store.accessor.edit_chat_state(chatid=chat.chatid,state="AUTH")
        else:
            await self.handle_to_queue(
                        chat_id=chat.chatid,
                        message_thread_id=message.message.message_thread_id,
                        text='''Неправильный ввод''',
                    )


    async def handle_review(self, chat: TGDC, message: MessageUpdate):
        text = message.message.text
        mangas = text.split('|')
        readtime = await self.app.store.accessor.get_last_readtime(chat.userid)
        for i in range(len(mangas)):
            current = mangas[i].split('--')
            manga = await self.app.store.accessor.seacrh_manga_name(current[0])
            if manga:
                await self.app.store.accessor.add_readtimemanga(read_id=readtime.id,manga_id=manga.id,rating=int(current[1]))
            else:
                await self.handle_to_queue(
                        chat_id=chat.chatid,
                        message_thread_id=message.message.message_thread_id,
                        text=f'''Ненаход  {current[0]}''',
                    )
            
        #машинка
        await self.app.store.accessor.edit_chat_state(chatid=chat.chatid,state="AUTH")


    async def handle_score(self, chat: TGDC, message: MessageUpdate):
        text = message.message.text
        current = text.split('|')
        manga = await self.app.store.accessor.seacrh_manga_name(current[0])
        if manga:
            await self.app.store.accessor.add_score(manga_id=manga.id,user_id=chat.userid,score=int(current[1]))
        else:
            await self.handle_to_queue(
                        chat_id=chat.chatid,
                        message_thread_id=message.message.message_thread_id,
                        text=f'''Ненаход  {current[0]}''',
                    )
        await self.app.store.accessor.edit_chat_state(chatid=chat.chatid,state="AUTH")
            
    async def handle_to_queue(
        self,
        chat_id: int,
        text: str,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: typing.List[MessageEntity] | None = None,
        disable_notification: bool | None = None,
        reply_to_message_id: int | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> None:
        await self.app.store.send_queue.put(
            MessageToSend(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                text=text,
                parse_mode=parse_mode,
                entities=entities,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
            )
        )
