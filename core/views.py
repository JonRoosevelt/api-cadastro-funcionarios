from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Prefetch
from rest_framework.decorators import action


class HelloView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, world!'}
        return Response(content)


class NaversView(viewsets.ModelViewSet):
    serializer_class = serializers.NaverSerializer
    queryset = models.Naver.objects.all()
    filterset_class = filters.NaversIndexFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.NaverDetailsSerializer
        return serializers.NaverSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return (models.Naver.objects
                    .prefetch_related(
                        'projects'
                    ).all())

    @action(detail=True, methods=['GET'])
    def details(self, request, pk):
        return super().retrieve(request, pk)


class ProjetosView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProjetoSerializer
    queryset = models.Projeto.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
