from rest_framework import serializers
from .models import User, FacialRecognition, SkillPath, AptitudeTest, Quiz, JobListing


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'left_face_image', 'right_face_image', 'front_image']


# FacialRecognition Serializer
class FacialRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacialRecognition
        fields = ['user', 'image_data']


# SkillPath Serializer
class SkillPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillPath
        fields = ['user', 'path_data']


# AptitudeTest Serializer
class AptitudeTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AptitudeTest
        fields = ['user', 'test_data', 'result']


# Quiz Serializer
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['course_id', 'question_data', 'answers']


# JobListing Serializer
class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['title', 'company', 'location', 'description', 'salary', 'is_active']
