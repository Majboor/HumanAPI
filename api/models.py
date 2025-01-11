from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name





class FacialRecognition(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='facial_recognition')
    left_image = models.ImageField(upload_to='facial_recognition/left/')
    right_image = models.ImageField(upload_to='facial_recognition/right/')
    front_image = models.ImageField(upload_to='facial_recognition/front/')
    embeddings = models.JSONField(null=True, blank=True)  # To store facial feature data (optional)
    
    def __str__(self):
        return f"Facial recognition data for {self.user.name}"



class SkillPath(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skill_path')
    path_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Skill Path for {self.user.name}"



class AptitudeTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aptitude_test')
    score = models.FloatField()
    test_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Aptitude test for {self.user.name}"



class Quiz(models.Model):
    course_id = models.CharField(max_length=100)
    question = models.TextField()
    options = models.JSONField()  # Storing multiple-choice options
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return f"Quiz for {self.course_id}"



class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"
