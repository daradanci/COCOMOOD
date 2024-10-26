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


class TAModel(db):
    __tablename__ = "target_audience"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class AuthorModel(db):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class GenreModel(db):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class TypeModel(db):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class StatusModel(db):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


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


class MangaThemeModel(db):
    __tablename__ = "mangatheme"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    theme_id = Column(Integer, ForeignKey("theme.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, theme_id),)


class MangaTAModel(db):
    __tablename__ = "mangata"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    ta_id = Column(Integer, ForeignKey("target_audience.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, ta_id),)


class MangaAuthorModel(db):
    __tablename__ = "mangaauthor"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, author_id),)


class MangaGenreModel(db):
    __tablename__ = "mangagenre"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    __table_args__ = (PrimaryKeyConstraint(manga_id, genre_id),)


class ScoreModel(db):
    __tablename__ = "score"

    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint(manga_id, user_id),)


class ReadTimeModel(db):
    __tablename__ = "readtime"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)


class ReadTimeMangaModel(db):
    __tablename__ = "readtimemanga"

    readtime_id = Column(Integer, ForeignKey("readtime.id"), nullable=False)
    manga_id = Column(Integer, ForeignKey("manga.id"), nullable=False)
    rating = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint(manga_id, readtime_id),)


class NodeModel(db):
    __tablename__ = "node"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    shortname = Column(String, unique=True, nullable=False)
    parent_id = Column(
        Integer, ForeignKey("node.id", ondelete="cascade"), nullable=True
    )
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    editor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_time = Column(DateTime, nullable=False)
    edited_time = Column(DateTime, nullable=False)
    type_id = Column(
        Integer, ForeignKey("type.id", ondelete="cascade"), nullable=False
    )
    description = Column(String, nullable=True)
    x_cord = Column(Float, nullable=False)
    y_cord = Column(Float, nullable=False)
    z_cord = Column(Float, nullable=False)

    children = relationship("NodeModel")
    usermade = relationship(
        "UserModel",
        back_populates="usermade",
        foreign_keys="NodeModel.creator_id",
    )
    nodetype = relationship(
        "TypeModel", back_populates="nodetype", foreign_keys="NodeModel.type_id"
    )
    node1 = relationship(
        "ConnectionModel",
        back_populates="node1",
        foreign_keys="ConnectionModel.node1_id",
    )
    node2 = relationship(
        "ConnectionModel",
        back_populates="node2",
        foreign_keys="ConnectionModel.node2_id",
    )
    useredit = relationship(
        "UserModel",
        back_populates="useredit",
        foreign_keys="NodeModel.editor_id",
    )

    def to_dc(self) -> NodeDC:
        return NodeDC(
            id=self.id,
            parent_id=self.parent_id,
            creator_id=self.creator_id,
            editor_id=self.editor_id,
            created_time=self.created_time,
            edited_time=self.edited_time,
            type_id=self.type_id,
            name=self.name,
            shortname=self.shortname,
            description=self.description,
            x_cord=self.x_cord,
            y_cord=self.y_cord,
            z_cord=self.z_cord,
        )


class ConnectionModel(db):
    __tablename__ = "connection"

    id = Column(Integer, primary_key=True, autoincrement=True)
    node1_id = Column(
        Integer, ForeignKey("node.id", ondelete="cascade"), nullable=False
    )
    node2_id = Column(
        Integer, ForeignKey("node.id", ondelete="cascade"), nullable=False
    )
    distance = Column(Float, nullable=False)
    time = Column(Float, nullable=False)
    t_weight = Column(Float, nullable=False)

    __tableargs__ = (
        UniqueConstraint("node1_id", "node2_id", name="node_combination"),
    )

    node1 = relationship(
        "NodeModel",
        back_populates="node1",
        foreign_keys="ConnectionModel.node1_id",
    )
    node2 = relationship(
        "NodeModel",
        back_populates="node2",
        foreign_keys="ConnectionModel.node2_id",
    )

    def to_dc(self) -> NodeConnectionDC:
        return NodeConnectionDC(
            id=self.id,
            node1_id=self.node1_id,
            node2_id=self.node2_id,
            distance=self.distance,
            time=self.time,
            t_weight=self.t_weight,
        )
