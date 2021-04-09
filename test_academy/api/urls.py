from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'resources', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('total_cost/', total_cost)
    ]