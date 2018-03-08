from django.conf.urls import url
from rest_framework import routers
from strategy import views

router = routers.DefaultRouter()
router.register(r'', views.StrategyViewSet)

urlpatterns = [
    url(r'addStrategy', views.addStrategy),
    url(r'getStrategyList', views.getStrategyList),
]

urlpatterns += router.urls
