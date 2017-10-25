from django.conf.urls import url, include
from rest_framework import routers
from account.serialzers import UserSerializer

router = routers.DefaultRouter()
router.register(r'user', UserSerializer)
