from app.base.db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class UserModel(db):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    tgid = Column(Integer, nullable=True)

    #ссылка на ребенка
    user_score = relationship(
        "ScoreModel",
        back_populates="user_score",
        foreign_keys="ScoreModel.user_id",
    )
    #ссылка на ребенка
    user_time = relationship(
        "ReadTimeModel",
        back_populates="user_time",
        foreign_keys="ReadTimeModel.user_id",
    )
    
