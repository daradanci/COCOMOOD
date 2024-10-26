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


class ThemeModel(db):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    thememm = relationship(
        "MangaThemeModel",
        back_populates="thememm",
        foreign_keys="MangaThemeModel.theme_id",
    )

    def to_DC(self) -> ThemeDC:
        return ThemeDC(id=self.id, name=self.name)


class TAModel(db):
    __tablename__ = "target_audience"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    tamm = relationship(
        "MangaTAModel",
        back_populates="tamm",
        foreign_keys="MangaTAModel.ta_id",
    )

    def to_DC(self) -> TADC:
        return TADC(id=self.id, name=self.name)


class AuthorModel(db):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    authormm = relationship(
        "MangaAuthorModel",
        back_populates="authormm",
        foreign_keys="MangaAuthorModel.author_id",
    )

    def to_DC(self) -> AuthorDC:
        return AuthorDC(id=self.id, name=self.name)


class GenreModel(db):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    genremm = relationship(
        "MangaGenreModel",
        back_populates="genremm",
        foreign_keys="MangaGenreModel.genre_id",
    )

    def to_DC(self) -> GenreDC:
        return GenreDC(id=self.id, name=self.name)


class TypeModel(db):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    mangatype = relationship(
        "MangaModel",
        back_populates="mangatype",
        foreign_keys="MangaModel.type_id",
    )

    def to_DC(self) -> TypeDC:
        return TypeDC(id=self.id, name=self.name)


class StatusModel(db):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    mangastatus = relationship(
        "MangaModel",
        back_populates="mangastatus",
        foreign_keys="MangaModel.status_id",
    )

    def to_DC(self) -> StatusDC:
        return StatusDC(id=self.id, name=self.name)


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

    def to_DC(self) -> MangaDC:
        return MangaDC(
            id=self.id,
            title=self.title,
            type_id=self.type_id,
            score=self.score,
            status_id=self.status_id,
            volumes=self.volumes,
            chapters=self.chapters,
            image=self.image,
            link=self.link,
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

    def to_DC(self) -> MangaThemeDC:
        return MangaThemeDC(manga_id=self.manga_id, theme_id=self.theme_id)


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

    def to_DC(self) -> MangaTADC:
        return MangaTADC(manga_id=self.manga_id, ta_id=self.ta_id)


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

    def to_DC(self) -> MangaAuthorDC:
        return MangaAuthorDC(manga_id=self.manga_id, author_id=self.author_id)


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

    def to_DC(self) -> MangaGenreDC:
        return MangaGenreDC(manga_id=self.manga_id, genre_id=self.genre_id)


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

    def to_DC(self) -> ScoreDC:
        return ScoreDC(
            manga_id=self.manga_id, user_id=self.user_id, rating=self.rating
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

    def to_DC(self) -> ReadTimeDC:
        return ReadTimeDC(
            id=self.id, user_id=self.user_id, start=self.start, end=self.end
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

    def to_DC(self) -> ReadTimeMangaDC:
        return ReadTimeMangaDC(
            readtime_id=self.readtime_id,
            manga_id=self.manga_id,
            rating=self.rating,
        )
