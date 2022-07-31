from django.urls import path

from . import views

urlpatterns = [
    path('', views.BeerListCreateAPIView.as_view()),
    path('<int:pk>/', views.BeerDetailAPIView.as_view()),
]
