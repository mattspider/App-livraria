from requests import Response
from rest_framework import mixins, permissions, viewsets
from rest_framework import status

from api.models import Livros
from api.serializers import LivrosSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
