from django.conf.urls import url
from api.views import users
urlpatterns = [
    url('register', users.RegisterAPIView.as_view()),
    url('login', users.LoginAPIView.as_view())
]