from django.urls import path

from . import views

urlpatterns = [
    path('', views.BeerMixinView.as_view()),
    #path('<int:pk>/', views.BeerDetailAPIView.as_view()),
    #path('', views.BeerListCreateAPIView.as_view()),
    path('<int:pk>/', views.BeerDetailAPIView.as_view()),
    path('<int:pk>/update/', views.BeerUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.BeerDeleteAPIView.as_view()),
]
