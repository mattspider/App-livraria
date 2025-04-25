from django.urls import include, path
from rest_framework import routers

from api.views import LivrosViewSet

router = routers.DefaultRouter()

router.register(r'livro', LivrosViewSet)

urlpatterns = [
    path("", include(router.urls)),
]