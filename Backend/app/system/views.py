from aiohttp.web_exceptions import (
    HTTPForbidden,
    HTTPUnauthorized,
    HTTPBadRequest,
    HTTPNotFound,
    HTTPServiceUnavailable
)
from aiohttp_apispec import (
    request_schema,
)

from aiohttp_cors import CorsViewMixin
from Backend.app.web.mixin import AuthRequiredMixin
from app.web.app import View
from app.web.utils import json_response

from app.system.schemas import (
    NewConnSchema,
    NewNodeSchema,
    NewTypeSchema,
    UpdConnSchema,
    UpdNodeSchema,
    UpdTypeSchema,
)



class ReadStatView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass

class InterestView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass

class ReadTimeView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass

class ReadDaysView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass

class MangaView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass