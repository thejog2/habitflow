from django.urls import path
from . import views
from .views import HabitListView

urlpatterns = [

    # -------------------------
    # Habits
    # -------------------------
    path('habits/', HabitListView.as_view(), name='habit_list'),
    path('habits/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit_detail'),
    path('habits/<int:pk>/edit/', views.HabitUpdateView.as_view(), name='habit_edit'),
    path('habits/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),

    # -------------------------
    # Log Entries
    # -------------------------
    path('habit/<int:habit_pk>/log/add/', views.CreateLogEntryView.as_view(), name='log_add'),
    path('log/<int:pk>/edit/', views.UpdateLogEntryView.as_view(), name='log_edit'),
    path('log/<int:pk>/delete/', views.DeleteLogEntryView.as_view(), name='log_delete'),

    # -------------------------
    # Dashboard & Quick Log
    # -------------------------
    path('dashboard/', views.dashboard, name='dashboard'),
    path('habit/<int:pk>/quick-log/', views.quick_log, name='quick_log'),
]
