from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from core import views

router = routers.DefaultRouter()
router.register('navers', views.NaversView, basename='navers')
router.register('projetos', views.ProjetosView, basename='projetos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('users/register', views.UserCreate.as_view()),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
]