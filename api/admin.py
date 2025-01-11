from django.contrib import admin
from .models import User, FacialRecognition, SkillPath, AptitudeTest, Quiz, JobListing

admin.site.register(User)
admin.site.register(FacialRecognition)
admin.site.register(SkillPath)
admin.site.register(AptitudeTest)
admin.site.register(Quiz)
admin.site.register(JobListing)