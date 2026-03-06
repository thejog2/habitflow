from django.urls import path
from . import views
from .views import HabitListView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('habits/', HabitListView.as_view(), name='habit_list'),
    path('habits/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit_detail'),
]
