from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class HelloView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, world!'}
        return Response(content)


class NaversView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NaverSerializer
    queryset = models.Naver.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']


class ProjetosView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProjetoSerializer
    queryset = models.Projeto.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']