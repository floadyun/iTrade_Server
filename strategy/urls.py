from rest_framework import routers
from strategy import views

router = routers.DefaultRouter()
router.register(r'', views.StrategyViewSet)
