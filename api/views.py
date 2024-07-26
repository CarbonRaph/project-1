from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import  SensorData,FitnessProgress,Exercise,Workout,ExerciseLog, UserProfileInfo
from api.serializers import ( SensorDataSerializer, FitnessProgressSerializer, ExerciseSerializer, WorkoutSerializer, ExerciseLogSerializer, UserProfileInfoSerializer)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the API homepage!")




@api_view(['GET', 'POST'])
def sensor_data_list(request):
    if request.method == 'GET':
        sensor_data = SensorData.objects.all()
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def fitness_progress_list(request):
    if request.method == 'GET':
        fitness_progress = FitnessProgress.objects.all()
        serializer = FitnessProgressSerializer(fitness_progress, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FitnessProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def exercise_list(request):
    if request.method == 'GET':
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def workout_list(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def exercise_log_list(request):
    if request.method == 'GET':
        exercise_logs = ExerciseLog.objects.all()
        serializer = ExerciseLogSerializer(exercise_logs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExerciseLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_profile_list(request):
    if request.method == 'GET':
        user_profiles = UserProfileInfo.objects.all()
        serializer = UserProfileInfoSerializer(user_profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserProfileInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
