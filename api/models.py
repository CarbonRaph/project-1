from django.db import models
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(help_text='Email', unique=True)  # Ensure email is unique
    password = models.CharField(max_length=15, )   # Ensure password is unique
    date_of_birth = models.DateField(help_text='Date of Birth')
    Gender = models.CharField(max_length=20, help_text='Sex/Gender')
    Telephone_number = models.FloatField()



class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data_type = models.TextField()
    data = models.FileField(upload_to='static/')
    strength = models.FloatField()
    fatigue = models.FloatField()


class FitnessProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField()
    range_of_motion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Range of motion in degrees")
    muscle_fatigue = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Muscle fatigue level")
    muscle_strength = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Muscle strength level")
    progress_percentage = models.FloatField()

    class Meta:
        verbose_name = "Fitness Progress"
        verbose_name_plural = "Fitness Progresses"

    def __str__(self):
        return f"{self.date} - Range of Motion: {self.range_of_motion}, Muscle Fatigue: {self.muscle_fatigue}, Muscle Strength: {self.muscle_strength}"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_groups = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration_minutes = models.IntegerField()

class ExerciseLog(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    duration_seconds = models.IntegerField()

class SensarData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    accel_x = models.FloatField()
    accel_y = models.FloatField()
    accel_z = models.FloatField()
    
    temp = models.FloatField()
    

    def __str__(self):
        return f"{self.timestamp}: X={self.accel_x}, Y={self.accel_y}, Z={self.accel_z} , Temp={self.temp}"

  

# Create your models here.
