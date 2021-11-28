from django.urls import path, include
from .views import RegisterApi

urlpatterns = [
    #path('auth/', include('dj_rest_auth.urls')), # http://127.0.0.1:8000/accounts/auth/login/
    path('', include('dj_rest_auth.urls')), # http://127.0.0.1:8000/accounts/login/
    path('register/', RegisterApi.as_view())
]