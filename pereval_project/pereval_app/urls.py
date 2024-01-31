from django.urls import include, path
from rest_framework import routers

from .views import PerevalCreateView


router = routers.DefaultRouter()
router.register('submitData', PerevalCreateView)

urlpatterns = [
    path('', include(router.urls)),
]