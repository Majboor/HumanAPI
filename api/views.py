

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, FacialRecognition, SkillPath, AptitudeTest, Quiz, JobListing
from .serializers import UserSerializer, FacialRecognitionSerializer, SkillPathSerializer, AptitudeTestSerializer, QuizSerializer, JobListingSerializer


class ProfileCreateView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data.get('user')
        facial_data = request.data.get('facial_recognition')

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()

            # Saving facial recognition data (if provided)
            if facial_data:
                facial_recognition_serializer = FacialRecognitionSerializer(data=facial_data)
                if facial_recognition_serializer.is_valid():
                    facial_recognition_serializer.save(user=user_serializer.instance)

            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileCheckView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')

        try:
            user = User.objects.get(name=name)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)



class ProfileFetchView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        try:
            user = User.objects.get(name=name)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class SkillPathCreateView(APIView):
    def post(self, request, *args, **kwargs):
        skill_path_data = request.data
        serializer = SkillPathSerializer(data=skill_path_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SkillPathFetchView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        try:
            skill_path = SkillPath.objects.get(user_id=user_id)
            return Response(SkillPathSerializer(skill_path).data)
        except SkillPath.DoesNotExist:
            return Response({"message": "Skill path not found"}, status=status.HTTP_404_NOT_FOUND)




class AptitudeTestCreateView(APIView):
    def post(self, request, *args, **kwargs):
        test_data = request.data
        serializer = AptitudeTestSerializer(data=test_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AptitudeTestFetchView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        try:
            test_result = AptitudeTest.objects.get(user_id=user_id)
            return Response(AptitudeTestSerializer(test_result).data)
        except AptitudeTest.DoesNotExist:
            return Response({"message": "Test result not found"}, status=status.HTTP_404_NOT_FOUND)



class QuizCreateView(APIView):
    def post(self, request, *args, **kwargs):
        quiz_data = request.data
        serializer = QuizSerializer(data=quiz_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class QuizFetchView(APIView):
    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id')
        try:
            quiz = Quiz.objects.get(course_id=course_id)
            return Response(QuizSerializer(quiz).data)
        except Quiz.DoesNotExist:
            return Response({"message": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)



class JobListingFetchView(APIView):
    def get(self, request, *args, **kwargs):
        job_listings = JobListing.objects.filter(is_active=True)
        return Response(JobListingSerializer(job_listings, many=True).data)
