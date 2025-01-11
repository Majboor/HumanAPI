from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SkillPathViewSet, CourseViewSet, CourseEnrollmentViewSet, JobSkillApplicationViewSet, QuizViewSet, QuizSubmissionViewSet, RealTimeInteractionViewSet, SystemConfigurationViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'skill-paths', SkillPathViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course-enrollments', CourseEnrollmentViewSet)
router.register(r'job-skill-applications', JobSkillApplicationViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'quiz-submissions', QuizSubmissionViewSet)
router.register(r'real-time-interactions', RealTimeInteractionViewSet)
router.register(r'system-configurations', SystemConfigurationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

