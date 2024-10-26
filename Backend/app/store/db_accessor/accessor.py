import typing
from hashlib import sha256

from sqlalchemy import select, desc, update, delete, func
from sqlalchemy.orm import selectinload
import sqlalchemy.exc

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
    

    async def add_theme(self,)->None:
        pass
    async def add_ta(self,)->None:
        pass
    async def add_author(self,)->None:
        pass
    async def add_genre(self,)->None:
        pass
    async def add_type(self,)->None:
        pass
    async def add_status(self,)->None:
        pass
    async def add_manga(self,)->None:
        pass
    async def add_mangatheme(self,)->None:
        pass
    async def add_mangata(self,)->None:
        pass
    async def add_mangaauthor(self,)->None:
        pass
    async def add_mangagenre(self,)->None:
        pass
    async def add_score(self,)->None:
        pass
    async def add_readtime(self,)->None:
        pass
    async def add_readtimemanga(self,)->None:
        pass
    

    

        
