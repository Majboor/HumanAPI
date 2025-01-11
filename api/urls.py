from django.urls import path
from .views import (
    ProfileCreateView, ProfileCheckView, ProfileFetchView,
    SkillPathCreateView, SkillPathFetchView,
    AptitudeTestCreateView, AptitudeTestFetchView,
    QuizCreateView, QuizFetchView,
    JobListingFetchView
)

urlpatterns = [
    # Profile Endpoints
    path('profiles/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profiles/check/', ProfileCheckView.as_view(), name='profile-check'),
    path('profiles/fetch/', ProfileFetchView.as_view(), name='profile-fetch'),

    # Skill Path Endpoints
    path('skill-path/create/', SkillPathCreateView.as_view(), name='skill-path-create'),
    path('skill-path/fetch/', SkillPathFetchView.as_view(), name='skill-path-fetch'),

    # Aptitude Test Endpoints
    path('aptitude-test/create/', AptitudeTestCreateView.as_view(), name='aptitude-test-create'),
    path('aptitude-test/fetch/', AptitudeTestFetchView.as_view(), name='aptitude-test-fetch'),

    # Quiz Endpoints
    path('quiz/create/', QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/fetch/', QuizFetchView.as_view(), name='quiz-fetch'),

    # Job Listing Endpoints
    path('job-listings/fetch/', JobListingFetchView.as_view(), name='job-listings-fetch'),
]
