from rest_framework import serializers
from .models import SensorData,FitnessProgress,Exercise,Workout,ExerciseLog,UserProfileInfo

        
class UserProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfileInfo
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class FitnessProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessProgress
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLog
        fields = '__all__'