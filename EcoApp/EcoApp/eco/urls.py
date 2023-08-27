from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'eco'
urlpatterns = [
    path('', views.CourseListView.as_view()),
    path('card/<int:pk>', views.EcoCardListView.as_view(), name='card'),
    path('soviet/<int:pk>/', views.EcoSovietListView.as_view(), name='soviet_list'),
    # path('detai-soviet/<int:pk>', views.EcoSovietDetailView.as_view()),
]
