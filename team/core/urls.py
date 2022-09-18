from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from core.views import (
    UserSignUp,
    TestView
)

urlpatterns = [
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('sign-up/', UserSignUp.as_view(), name='sign_up'),
    path('test/', TestView.as_view(), name='test'),
]
