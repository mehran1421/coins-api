from django.urls import path, include
from .views import CoinsViewSet
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('coins', CoinsViewSet, basename="coins")


urlpatterns = [
	path("", include(router.urls)),
]