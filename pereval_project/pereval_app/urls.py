from django.urls import include, path
from rest_framework import routers

from .views import PerevalViewSet


router = routers.DefaultRouter()
router.register('submitData', PerevalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]