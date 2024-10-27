from typing import Optional, TYPE_CHECKING
from aiohttp import ClientSession

from app.base.base_accessor import BaseAccessor
from app.store.bot.bot.update_handler import Updater

TELEGRAM_HOST = "https://api.telegram.org"

if TYPE_CHECKING:
    from app.web.app import Application


class BotApi(BaseAccessor):
    def __int__(self, app: "Application", *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self.client: Optional[ClientSession] = None
        self.updater: Optional[Updater] = None

    async def connect(self, app: "Application"):
        self.client = ClientSession()
        self.updater = Updater(self.app)
        await self.updater.start()

    async def disconnect(self, app: "Application"):
        await self.client.close()
        await self.updater.stop()
        self.client = None
