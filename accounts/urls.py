from django.urls import path
from rest_framework import urlpatterns
from .views import MyTokenObtainPairView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path("api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/token/",
        csrf_exempt(MyTokenObtainPairView.as_view()),
        name="token_obtain_pair",
    ),
]
