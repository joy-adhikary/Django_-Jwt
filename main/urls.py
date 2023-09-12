from django.urls import path
from main.views import *

urlpatterns = [
    path('',Joy.as_view()),
    path('index/',Roy.as_view())
]