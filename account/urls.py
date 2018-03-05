from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
