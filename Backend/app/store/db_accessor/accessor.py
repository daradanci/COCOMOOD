import typing
from hashlib import sha256

from sqlalchemy import select, desc, update, delete, func
from sqlalchemy.orm import selectinload
import sqlalchemy.exc
import datetime

from app.base.base_accessor import BaseAccessor
from app.system.dataclasses import (
    ThemeDC,
    TADC,
    TypeDC,
    AuthorDC,
    MangaAuthorDC,
    ReadTimeDC,
    ReadTimeMangaDC,
    MangaTADC,
    MangaThemeDC,
    GenreDC,
    MangaGenreDC,
    MangaDC,
    ScoreDC,
    StatusDC,
)
from app.system.models import (
    ThemeModel,
    TAModel,
    TypeModel,
    AuthorModel,
    MangaAuthorModel,
    ReadTimeModel,
    ReadTimeMangaModel,
    MangaTAModel,
    MangaThemeModel,
    GenreModel,
    MangaGenreModel,
    MangaModel,
    ScoreModel,
    StatusModel,
)
from app.user.models import UserModel
from app.user.dataclasses import UserDC, UserforRequest

if typing.TYPE_CHECKING:
    from app.web.app import Application


class DBAccessor(BaseAccessor):
    async def get_by_login(self, login: str) -> UserDC | None:
        async with self.app.database.session() as session:
            query = select(UserModel).where(UserModel.login == login)
            res = await session.scalars(query)
            user = res.one_or_none()
            if user:
                return UserDC(
                    id=user.id,
                    login=user.login,
                    name=user.name,
                    tg=user.tg,                    
                    password=user.password,
                    registration_date=user.reregistration_date,
                    book_plan=user.book_plan,
                )
            return None

    async def get_by_tg(self, tg: int) -> UserDC | None:
        async with self.app.database.session() as session:
            query = select(UserModel).where(UserModel.tgid == tg)
            res = await session.scalars(query)
            user = res.one_or_none()
            if user:
                return UserDC(
                    id=user.id,
                    login=user.login,
                    name=user.name,
                    tg=user.tg, 
                    password=user.password,
                    registration_date=user.reregistration_date,
                    book_plan=user.book_plan,
                )
            return None

    async def get_by_id(self, id: int) -> UserDC | None:
        async with self.app.database.session() as session:
            query = select(UserModel).where(UserModel.id == id)
            res = await session.scalars(query)
            user = res.one_or_none()
            if user:
                return UserDC(
                    id=user.id,
                    login=user.login,
                    name=user.name,
                    tg=user.tg, 
                    password=user.password,
                    registration_date=user.reregistration_date,
                    book_plan=user.book_plan,
                )
            return None
    
    async def create_user(
        self, login: str, password: str, name: str
    ) -> UserforRequest | None:
        try:
            async with self.app.database.session() as session:
                user = UserModel(
                    login=login,
                    password=sha256(password.encode()).hexdigest(),
                    name=name,
                    registration_date=datetime.now(),
                )
                session.add(user)
                await session.commit()
                return UserforRequest(
                    id=user.id,
                    login=user.login,
                    name=user.name,
                )
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    
    async def add_tg_id(self, login:str,tgid:int)->UserDC|None:
        try:
            async with self.app.database.session() as session:
                query = (
                    update(UserModel)
                    .where(UserModel.login == login)
                    .values(
                        tgid=tgid
                    )
                )
                await session.execute(query)
                await session.commit()
                user = await self.get_by_login(login=login)
                return user
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
        
    
    
    async def add_target(self, tgid:int,target:int)->UserDC|None:
        try:
            async with self.app.database.session() as session:
                query = (
                    update(UserModel)
                    .where(UserModel.tgid == tgid)
                    .values(
                        book_plan=target
                    )
                )
                await session.execute(query)
                await session.commit()
                user = await self.get_by_tg(tgid=tgid)
                return user
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    

    async def add_theme(self,name:str)->ThemeDC|None:
        try:
            async with self.app.database.session() as session:
                theme = ThemeModel(
                    name=name,
                )
                session.add(theme)
                await session.commit()
                return theme.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_ta(self,name:str)->TADC|None:
        try:
            async with self.app.database.session() as session:
                ta = TAModel(
                    name=name,
                )
                session.add(ta)
                await session.commit()
                return ta.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_author(self,name:str)->AuthorDC|None:
        try:
            async with self.app.database.session() as session:
                author = AuthorModel(
                    name=name,
                )
                session.add(author)
                await session.commit()
                return author.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_genre(self,name:str)->GenreDC|None:
        try:
            async with self.app.database.session() as session:
                genre = GenreModel(
                    name=name,
                )
                session.add(genre)
                await session.commit()
                return genre.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_type(self,name:str)->TypeDC|None:
        try:
            async with self.app.database.session() as session:
                type_ = TypeModel(
                    name=name,
                )
                session.add(type_)
                await session.commit()
                return type_.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_status(self,name:str)->StatusDC|None:
        try:
            async with self.app.database.session() as session:
                status = StatusModel(
                    name=name,
                )
                session.add(status)
                await session.commit()
                return status.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_manga(self,title:str,type_id:int,status_id:int,image:str,link:int,score:float|None=None,volumes:int|None=None,chapters:int|None=None)->MangaDC|None:
        try:
            async with self.app.database.session() as session:
                manga = MangaModel(
                    title=title,
                    type_id=type_id,
                    status_id=status_id,
                    image=image,
                    link=link,
                    score=score,
                    volumes=volumes,
                    chapters=chapters,
                )
                session.add(manga)
                await session.commit()
                return manga.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_mangatheme(self,manga_id:int,theme_id:int)->MangaThemeDC|None:
        try:
            async with self.app.database.session() as session:
                mt = MangaThemeModel(
                    manga_id=manga_id,
                    theme_id=theme_id
                )
                session.add(mt)
                await session.commit()
                return mt.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_mangata(self,manga_id:int,ta_id:int)->MangaTADC|None:
        try:
            async with self.app.database.session() as session:
                mt = MangaTAModel(
                    manga_id=manga_id,
                    ta_id=ta_id
                )
                session.add(mt)
                await session.commit()
                return mt.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_mangaauthor(self,manga_id:int,author_id:int,role:str)->MangaAuthorDC|None:
        try:
            async with self.app.database.session() as session:
                ma = MangaAuthorModel(
                    manga_id=manga_id,
                    author_id=author_id,
                    role=role
                )
                session.add(ma)
                await session.commit()
                return ma.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_mangagenre(self,manga_id:int,genre_id:int)->MangaGenreDC|None:
        try:
            async with self.app.database.session() as session:
                mg = MangaGenreModel(
                    manga_id=manga_id,
                    genre_id=genre_id
                )
                session.add(mg)
                await session.commit()
                return mg.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_score(self,manga_id:int, user_id:int,score:int)->ScoreDC|None:
        try:
            async with self.app.database.session() as session:
                score = ScoreModel(
                    manga_id=manga_id,
                    user_id=user_id,
                    score=score
                )
                session.add(score)
                await session.commit()
                return score.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_readtime(self,user_id:int)->ReadTimeDC|None:
        try:
            async with self.app.database.session() as session:
                rt = ReadTimeModel(
                    user_id=user_id,
                    start=datetime.now()
                )
                session.add(rt)
                await session.commit()
                return rt.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_readtime_end(self,id:int)->None:
        try:
            async with self.app.database.session() as session:
                query = (
                    update(ReadTimeModel)
                    .where(ReadTimeModel.id == id )
                    .values(
                        end=datetime.now()
                    )
                )
                await session.execute(query)
                await session.commit()
                return None
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def get_last_readtime(self,user_id:int)->ReadTimeDC|None:
        try:
            async with self.app.database.session() as session:
                query = select(ReadTimeModel).where(ReadTimeModel.user_id == user_id).desc().limit(1)
                res = await session.scalars(query)
                readtime = res.one_or_none()
                if readtime:
                    return ReadTimeDC(
                        id=readtime.id,
                        user_id=readtime.user_id,
                        start=readtime.start,
                        end=readtime.end
                    )
                return None
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def del_readtime(self,id:int)->None:
        try:
            async with self.app.database.session() as session:
                query = delete(ReadTimeModel).where(ReadTimeModel.id == id)
                await session.execute(query)
                await session.commit()
                return None
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def add_readtimemanga(self,read_id:int,manga_id:int,rating:int)->ReadTimeMangaDC|None:
        try:
            async with self.app.database.session() as session:
                rt = ReadTimeMangaModel(
                    readtime_id=read_id,
                    manga_id=manga_id,
                    rating=rating
                )
                session.add(rt)
                await session.commit()
                return rt.to_DC()
        except sqlalchemy.exc.IntegrityError:
            return None
        except sqlalchemy.exc.ProgrammingError:
            return None
    async def change_score(self,)->None:
        pass
    async def get_last_30_readtime(self,)->None:
        pass
    async def get_completed_books(self,)->None:
        pass
    async def get_all_read_info_by_user_id(self,)->None:
        pass
    async def get_all_read_time_by_user_id(self,)->None:
        pass
    async def get_all_read_time_by_user_id_within_week(self,)->None:
        pass
    async def get_mangainfo(self,)->None:
        pass



    

        
