from rest_framework import viewsets
from .models import UserProfile, SkillPath, Course, CourseEnrollment, JobSkillApplication, Quiz, QuizSubmission, RealTimeInteraction, SystemConfiguration
from .serializers import UserProfileSerializer, SkillPathSerializer, CourseSerializer, CourseEnrollmentSerializer, JobSkillApplicationSerializer, QuizSerializer, QuizSubmissionSerializer, RealTimeInteractionSerializer, SystemConfigurationSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class SkillPathViewSet(viewsets.ModelViewSet):
    queryset = SkillPath.objects.all()
    serializer_class = SkillPathSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer

class JobSkillApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobSkillApplication.objects.all()
    serializer_class = JobSkillApplicationSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizSubmissionViewSet(viewsets.ModelViewSet):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializer

class RealTimeInteractionViewSet(viewsets.ModelViewSet):
    queryset = RealTimeInteraction.objects.all()
    serializer_class = RealTimeInteractionSerializer

class SystemConfigurationViewSet(viewsets.ModelViewSet):
    queryset = SystemConfiguration.objects.all()
    serializer_class = SystemConfigurationSerializer
