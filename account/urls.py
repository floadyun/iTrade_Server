from django.conf.urls import url
from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    # user
    url(r'login', views.login),
    url(r'register', views.register),
]

urlpatterns +=router.urls