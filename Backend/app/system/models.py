from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    UniqueConstraint,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import relationship
from app.base.db import db
from app.map.dataclasses import NodeDC, NodetypeDC, NodeConnectionDC





class ThemeModel(db):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    thememm = relationship(
        "MangaThemeModel",
        back_populates="thememm",
        foreign_keys="MangaThemeModel.theme_id",
    )
    


class TAModel(db):
    __tablename__ = "target_audience"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    tamm = relationship(
        "MangaTAModel",
        back_populates="tamm",
        foreign_keys="MangaTAModel.ta_id",
    )


class AuthorModel(db):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    authormm = relationship(
        "MangaAuthorModel",
        back_populates="authormm",
        foreign_keys="MangaAuthorModel.author_id",
    )


class GenreModel(db):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    genremm = relationship(
        "MangaGenreModel",
        back_populates="genremm",
        foreign_keys="MangaGenreModel.genre_id",
    )
    


class TypeModel(db):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    mangatype = relationship(
        "MangaModel",
        back_populates="mangatype",
        foreign_keys="MangaModel.type_id",
    )
    




class StatusModel(db):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    
    mangastatus = relationship(
        "MangaModel",
        back_populates="mangastatus",
        foreign_keys="MangaModel.status_id",
    )
    


class MangaModel(db):
    __tablename__ = "manga"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)
    score = Column(Float, nullable=True)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    volumes = Column(Integer, nullable=True)
    chapters = Column(Integer, nullable=True)
    image = Column(String, nullable=False)
    link = Column(String, nullable=False)


    mangatype = relationship(
        "TypeModel",
        back_populates="mangatype",
        foreign_keys="MangaModel.type_id",
    )
    mangastatus = relationship(
        "StatusModel",
        back_populates="mangastatus",
        foreign_keys="MangaModel.status_id",
    )

    mangatheme = relationship(
        "MangaThemeModel",
        back_populates="mangatheme",
        foreign_keys="MangaThemeModel.manga_id",
    )
    
    mangata = relationship(
        "MangaTAModel",
        back_populates="mangata",
        foreign_keys="MangaTAModel.manga_id",
    )
    
    mangaauthor = relationship(
        "MangaAuthorModel",
        back_populates="mangaauthor",
        foreign_keys="MangaAuthorModel.manga_id",
    )
    
    mangagenre = relationship(
        "MangaGenreModel",
        back_populates="mangagenre",
        foreign_keys="MangaGenreModel.manga_id",
    )
    mangascore = relationship(
        "ScoreModel",
        back_populates="mangascore",
        foreign_keys="ScoreModel.manga_id",
    )
    mangareadtime = relationship(
        "ReadTimeMangaModel",
        back_populates="mangareadtime",
        foreign_keys="ReadTimeMangaModel.manga_id",
    )
    
    
    





class MangaThemeModel(db):
    __tablename__ = "mangatheme"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    theme_id = Column(Integer, ForeignKey("theme.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, theme_id),)
    thememm = relationship(
        "ThemeModel",
        back_populates="thememm",
        foreign_keys="MangaThemeModel.theme_id",
    )
    mangatheme = relationship(
        "MangaModel",
        back_populates="mangatheme",
        foreign_keys="MangaThemeModel.manga_id",
    )


class MangaTAModel(db):
    __tablename__ = "mangata"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    ta_id = Column(Integer, ForeignKey("target_audience.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, ta_id),)
    tamm = relationship(
        "TAModel",
        back_populates="tamm",
        foreign_keys="MangaTAModel.ta_id",
    )
    mangata = relationship(
        "MangaModel",
        back_populates="mangata",
        foreign_keys="MangaTAModel.manga_id",
    )


class MangaAuthorModel(db):
    __tablename__ = "mangaauthor"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, author_id),)
    authormm = relationship(
        "AuthorModel",
        back_populates="authormm",
        foreign_keys="MangaAuthorModel.author_id",
    )
    mangaauthor = relationship(
        "MangaModel",
        back_populates="mangaauthor",
        foreign_keys="MangaAuthorModel.manga_id",
    )



class MangaGenreModel(db):
    __tablename__ = "mangagenre"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, genre_id),)
    genremm = relationship(
        "GenreModel",
        back_populates="genremm",
        foreign_keys="MangaGenreModel.genre_id",
    )
    mangagenre = relationship(
        "MangaModel",
        back_populates="mangagenre",
        foreign_keys="MangaGenreModel.manga_id",
    )



class ScoreModel(db):
    __tablename__ = "score"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint(manga_id, user_id),)
    user_score = relationship(
        "UserModel",
        back_populates="user_score",
        foreign_keys="ScoreModel.user_id",
    )
    mangascore = relationship(
        "MangaModel",
        back_populates="mangascore",
        foreign_keys="ScoreModel.manga_id",
    )


class ReadTimeModel(db):
    __tablename__ = "readtime"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    user_time = relationship(
        "UserModel",
        back_populates="user_time",
        foreign_keys="ReadTimeModel.user_id",
    )
    readtimedetails = relationship(
        "ReadTimeMangaModel",
        back_populates="readtimedetails",
        foreign_keys="ReadTimeMangaModel.readtime_id",
    )
    


class ReadTimeMangaModel(db):
    __tablename__ = "readtimemanga"

    readtime_id = Column(Integer, ForeignKey("readtime.id"), nullable=False)
    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint(manga_id, readtime_id),)

    mangareadtime = relationship(
        "MangaModel",
        back_populates="mangareadtime",
        foreign_keys="ReadTimeMangaModel.manga_id",
    )
    readtimedetails = relationship(
        "ReadTimeModel",
        back_populates="readtimedetails",
        foreign_keys="ReadTimeMangaModel.readtime_id",
    )

    

