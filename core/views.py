from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Prefetch
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from django.conf import settings
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from rest_framework.response import Response


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
    serializer_class = serializers.NaverSerializer
    queryset = models.Naver.objects.all()
    filterset_class = filters.NaversIndexFilter

    # def form_valid(self, form):
    #     form.instance.user = models.Naver.objects.get(user=self.request.user)
    #     return super(NaversView, self).form_valid(form)

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

    def create(self, *args, **kwargs):
        if self.request.method == 'POST':
            naver = dict(
                name=self.request.data['name'],
                birthdate=self.request.data['birthdate'],
                admission_date=self.request.data['admission_date'],
                job_role=self.request.data['job_role'],
                created_by=self.request.data['created_by']
            )
            serializer = self.get_serializer_class()
            serializer = serializer(data=naver)
            if serializer.is_valid():
                with transaction.atomic():
                    user = models.User.objects.get(
                        id=naver['created_by'])
                    validated_data = serializer.data
                    validated_data['created_by'] = user
                    instance = models.Naver.objects.create(
                        **validated_data
                    )
                    instance.save()
                    serialized_instance = self.get_serializer_class()(
                        instance).data
                    return Response(data=serialized_instance, status=201)
            return Response(serializer.errors)


class ProjetosView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProjetoSerializer
    queryset = models.Projeto.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

# @api_view(['POST'])
# def create_auth(request):
#     serialized = serializers.UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         models.User.objects.create_user(
#             serialized.init_data['email'],
#             serialized.init_data['password']
#         )
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)