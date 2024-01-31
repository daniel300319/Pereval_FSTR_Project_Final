from django.urls import include, path
from rest_framework import routers

from .views import PerevalAPIView


router = routers.DefaultRouter()
router.register('submitData', PerevalAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
