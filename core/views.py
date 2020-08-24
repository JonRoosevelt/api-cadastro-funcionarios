from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, views, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import filters, models, serializers


class HelloView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, world!'}
        return Response(content)


class UserCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny, )


class NaversView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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

    def get_serialized_data(self):
        naver = dict(
            name=self.request.data['name'],
            birthdate=self.request.data['birthdate'],
            admission_date=self.request.data['admission_date'],
            job_role=self.request.data['job_role'],
        )
        serializer = self.get_serializer_class()
        return serializer(data=naver)

    def create(self, *args, **kwargs):
        if self.request.method != 'POST':
            return
        serialized_data = self.get_serialized_data()
        if serialized_data.is_valid():
            with transaction.atomic():
                user = self.request.user
                validated_data = serialized_data.data
                validated_data['created_by'] = user
                instance = models.Naver.objects.create(
                    **validated_data
                )
                instance.save()
                serialized_instance = self.get_serializer_class()(
                    instance).data
                return Response(data=serialized_instance, status=201)
        return Response(serialized_data.errors)

    def update(self, *args, **kwargs):
        if self.request.method != 'PUT':
            return
        naver = models.Naver.objects.filter(id=self.kwargs['pk']).first()
        if naver:
            if naver.created_by.id == self.request.user.id:
                serialized_data = self.get_serialized_data()
                if serialized_data.is_valid():
                    with transaction.atomic():
                        user = self.request.user
                        validated_data = serialized_data.data
                        validated_data['created_by'] = user
                        instance = models.Naver.objects.update(
                            **validated_data
                        )
                        if bool(instance):
                            validated_data['id'] = int(self.kwargs['pk'])
                            validated_data['created_by'] = self.request.user.id
                            return Response(data=validated_data, status=201)
                return Response(serialized_data.errors)
            return Response(status=403)
        return Response(status=404)

    # @action(methods=['delete'], detail=True)
    def destroy(self, *args, **kwargs):
        if self.request.method != 'DELETE':
            return
        naver = models.Naver.objects.filter(id=self.kwargs['pk'])
        if naver:
            if naver.filter(created_by=self.request.user.id):
                with transaction.atomic():
                    naver.delete()
                return Response(status=204)
            return Response(status=403)
        return Response(status=404)


class ProjetosView(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProjetoSerializer
    queryset = models.Projeto.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ProjetoDetailsSerializer
        return serializers.ProjetoSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return (models.Projeto.objects
                    .prefetch_related(
                        'navers'
                    ).all())
        return models.Projeto.objects.all()

    def get_serialized_data(self):
        project = dict(
            name=self.request.data['name'],
        )
        serializer = self.get_serializer_class()
        return serializer(data=project)
    
    def create(self, *args, **kwargs):
        if self.request.method != 'POST':
            return
        serialized_data = self.get_serialized_data()
        if serialized_data.is_valid():
            with transaction.atomic():
                user = self.request.user
                validated_data = serialized_data.data
                validated_data['created_by'] = user
                instance = models.Projeto.objects.create(
                    **validated_data
                )
                instance.save()
                serialized_instance = self.get_serializer_class()(
                    instance).data
                return Response(data=serialized_instance, status=201)
        return Response(serialized_data.errors)