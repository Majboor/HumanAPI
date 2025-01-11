from rest_framework import serializers
from .models import UserProfile, SkillPath, Course, CourseEnrollment, JobSkillApplication, Quiz, QuizSubmission, RealTimeInteraction, SystemConfiguration

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Include all fields

class SkillPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillPath
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

class JobSkillApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkillApplication
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSubmission
        fields = '__all__'

class RealTimeInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTimeInteraction
        fields = '__all__'

class SystemConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfiguration
        fields = '__all__'
