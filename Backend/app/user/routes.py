from app.web.app import Application

from app.user.views import UserLoginView, UserCurrentView, UserCreate, UserInfoView


def register_urls(application: Application):

    application.router.add_view("/user/login", UserLoginView)
    application.router.add_view("/user/current", UserCurrentView)
    application.router.add_view("/user/create", UserCreate)
    application.router.add_view("/user/info", UserInfoView)
