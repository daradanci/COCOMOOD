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
        read_books = await self.store.accessor.get_completed_books(self.request.user.id)
        return json_response(
            data={
                "read_amount": read_books,
            }
        )
        

class InterestView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        interest_stat = await self.store.accessor.get_all_read_info_by_user_id(self.request.user.id)
        i = 0
        total_interest = 0
        for read_instance in interest_stat.data:
            for manga_instance in read_instance.read:
                i+=1
                total_interest+=manga_instance.rating
        return json_response(
            data={
                "average_interest": total_interest/i,
            }
        )

class ReadTimeView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        read_time_stat = await self.store.accessor.get_all_read_time_by_user_id(self.request.user.id)
        i = 0
        total_time = 0
        for read_instance in read_time_stat.data:
            total_time+=(read_instance.start-read_instance.end).total_seconds()
        return json_response(
            data={
                "average_interest": int(total_time/i),
            }
        )

class ReadDaysView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        read_periods = await self.store.accessor.get_all_read_time_by_user_id_within_week(self.request.user.id)
        return json_response(
            data={
                "periods":[{"start":period.start,"end":period.end}for period in read_periods.data],
            }
        )

class MangaView(AuthRequiredMixin,CorsViewMixin, View):
    async def get(self):
        pass