from django.urls import path
from . import views

app_name = "test"
urlpatterns = [
    path('', views.TestView.as_view(), name='index'),
]