from django.urls import path
from . import views

urlpatterns = [
    path("propertys/", views.PropertyListCreateView.as_view()),
]
