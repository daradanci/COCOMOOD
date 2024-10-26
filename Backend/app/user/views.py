from aiohttp.web_exceptions import (
    HTTPForbidden,
    HTTPUnauthorized,
    HTTPBadRequest,
    HTTPConflict,
    HTTPNotFound,
)
from aiohttp_apispec import (
    request_schema,
)

from aiohttp_cors import CorsViewMixin
from aiohttp_session import new_session

from app.web.app import View
from app.web.mixin import AuthRequiredMixin
from app.web.utils import json_response

from app.user.schemas import (
    UserSchema,
    NewUserSchema,
    UpdUserSchema,
)


class UserLoginView(CorsViewMixin, View):
    @request_schema(UserSchema)
    async def post(self):
        logindata = await self.store.userAPI.get_by_login(self.data.get("login"))
        if logindata is None:
                raise HTTPForbidden(reason="Неправильный логин пароль")
        if not logindata.tgid:
            tgid = None
        else:
            tgid = logindata.tgid
        user_data = {
            "id": logindata.id,
            "login": logindata.login,
            "name": logindata.name,
            "tg": tgid,
        }
        if "password" in self.data and logindata.is_password_valid(self.data["password"]):
            session = await new_session(request=self.request)
            session["user"] = user_data
            return json_response(data=user_data)
        raise HTTPForbidden(reason="Неправильный логин пароль")


class UserCurrentView(AuthRequiredMixin, CorsViewMixin, View):
    async def get(self):
        if self.request.user is not None:
            return json_response(
                data={
                    "id": self.request.user.id,
                    "login": self.request.user.login,
                    "name": self.request.user.name,
                }
            )
        raise HTTPUnauthorized(reason="Ошибка проверки авторизации")


class UserCreate(CorsViewMixin, View):
    @request_schema(NewUserSchema)
    async def post(self):
        user = await self.store.userAPI.create_user(
            login=self.data["login"],
            password=self.data["password"],
            name=self.data["name"],
        )
        if user is None:
            raise HTTPConflict(reason="Пользователь с таким логином уже существует")
        return json_response(
            data={
                "id": user.id,
                "login": user.login,
                "name": user.name,
            }
        )

    @request_schema(UpdUserSchema)
    async def put(self):
        if self.request.user is not None:
            user = await self.store.userAPI.update_userinfo(
                self.request.user.id,
                name=self.data.get("name"),
            )
            if user is None:
                raise HTTPConflict(reason="Ошибка смены данных")
            return json_response(
                data={
                    "id": user.id,
                    "login": user.login,
                    "name": user.name,
                }
            )
        raise HTTPUnauthorized(reason="Ошибка проверки авторизации")
