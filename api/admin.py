from django.contrib import admin
from api.models import SensorData,FitnessProgress,Exercise,Workout,ExerciseLog,UserProfileInfo,SensarData

admin.site.register(UserProfileInfo)
admin.site.register(SensorData)
admin.site.register(FitnessProgress)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(ExerciseLog)
admin.site.register(SensarData)


# Register your models here.
