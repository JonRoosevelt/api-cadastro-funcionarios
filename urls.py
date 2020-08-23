from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from core import views

router = routers.DefaultRouter()
router.register('navers', views.NaversView, basename='navers')
router.register('projetos', views.ProjetosView, basename='projetos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('users/register', views.UserCreate.as_view())
    # path('projetos/', views.ProjetosView.as_view(), name='projetos'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]