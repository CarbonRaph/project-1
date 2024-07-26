from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sensor-data-list/', views.sensor_data_list, name='sensor-data-list'),
    path('fitness-progress-list/', views.fitness_progress_list, name='fitness-progress-list'),
    path('exercise-list/', views.exercise_list, name='exercise-list'),
    path('workout-list/', views.workout_list, name='workout-list'),
    path('exercise-log-list/', views.exercise_log_list, name='exercise-log-list'),
    path('user-profile-list/',views.user_profile_list, name='user-profile-list'),
    
]