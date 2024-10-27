from dataclasses import dataclass
from datetime import datetime


@dataclass
class ThemeDC:
    id: int
    name: str


@dataclass
class TADC:
    id: int
    name: str


@dataclass
class AuthorDC:
    id: int
    name: str


@dataclass
class GenreDC:
    id: int
    name: str


@dataclass
class TypeDC:
    id: int
    name: str


@dataclass
class StatusDC:
    id: int
    name: str


@dataclass
class MangaDC:

    id: int
    title: str
    type_id: int
    score: float | None
    status_id: int
    volumes: int | None
    chapters: int | None
    image: str
    link: str


@dataclass
class MangaThemeDC:
    manga_id: int
    theme_id: int


@dataclass
class MangaTADC:

    manga_id: int
    ta_id: int


@dataclass
class MangaAuthorDC:
    manga_id: int
    author_id: int
    role: str


@dataclass
class MangaGenreDC:

    manga_id: int
    genre_id: int


@dataclass
class ScoreDC:
    manga_id: int
    user_id: int
    rating: int


@dataclass
class ReadTimeDC:

    id: int
    user_id: int
    start: datetime
    end: datetime | None


@dataclass
class ReadTimeMangaDC:

    readtime_id: int
    manga_id: int
    rating: int


@dataclass
class ReadTimeListDC:
    data: list[ReadTimeDC] | None


@dataclass
class ReadTimeMangaListDC:
    data: list[ReadTimeMangaDC] | None


@dataclass
class ReadTimeDetailsDC:
    readtime: ReadTimeDC
    read: list[ReadTimeMangaDC] | None


@dataclass
class ReadTimeDetailsListDC:
    data: list[ReadTimeDetailsDC] | None


@dataclass
class MangaInfoDC:

    id: int
    title: str
    score: float | None
    volumes: int | None
    chapters: int | None
    image: str
    link: str

    type: TypeDC
    status: StatusDC
    theme: list[MangaThemeDC] | None
    ta: list[MangaTADC] | None
    author: list[MangaAuthorDC] | None
    genre: list[MangaGenreDC] | None


@dataclass
class ThemeListDC:
    data: list[ThemeDC]


@dataclass
class TAListDC:
    data: list[TADC]


@dataclass
class AuthorListDC:
    data: list[AuthorDC]


@dataclass
class GenreListDC:
    data: list[GenreDC]


@dataclass
class ScoreFullDC:
    manga: MangaInfoDC
    user_id: int
    rating: int

@dataclass
class ScoreListDC:
    data: list[ScoreFullDC]|None

@dataclass
class TGDC:
    userid: int
    state: str
    chatid:int