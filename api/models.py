from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    english_language_knowledge = models.BooleanField(default=False)
    basic_computing_knowledge = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    left_face_image = models.ImageField(upload_to='face_images/', null=True, blank=True)
    right_face_image = models.ImageField(upload_to='face_images/', null=True, blank=True)
    front_face_image = models.ImageField(upload_to='face_images/', null=True, blank=True)
    voice_embedding = models.TextField(null=True, blank=True)  # Store voice embeddings in text format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SkillPath(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    path_name = models.CharField(max_length=100)
    path_description = models.TextField()
    is_completed = models.BooleanField(default=False)  # Default to False when not completed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} - {self.path_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50, choices=[('basic', 'Basic'), ('advanced', 'Advanced')], default='basic')
    content = models.TextField()  # Could be linked to actual files or lessons
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseEnrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0)  # Default to 0% completion
    is_completed = models.BooleanField(default=False)  # Default to False when not completed
    
    def __str__(self):
        return f"{self.user.name} - {self.course.name}"


class JobSkillApplication(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)
    task_submitted = models.BooleanField(default=False)  # Default to False, meaning task has not been submitted
    submission = models.TextField(null=True, blank=True)  # Optional task submission text
    feedback = models.TextField(null=True, blank=True)  # Optional feedback

    def __str__(self):
        return f"{self.user.name} - {self.job_title}"


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_choices = models.JSONField()  # Store choices as a JSON array
    correct_answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz for {self.course.name}"


class QuizSubmission(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submitted_answers = models.JSONField()  # Store answers as a JSON array
    score = models.IntegerField(default=0)  # Default to 0 if no score is provided
    feedback = models.TextField(null=True, blank=True)  # Optional feedback

    def __str__(self):
        return f"{self.user.name} - {self.quiz.course.name} Quiz"


class RealTimeInteraction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50, choices=[('voice', 'Voice'), ('text', 'Text')], default='text')
    interaction_data = models.TextField()  # Could be audio, text, or commands
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction with {self.user.name} at {self.timestamp}"


class SystemConfiguration(models.Model):
    config_name = models.CharField(max_length=100)
    config_value = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Config: {self.config_name}"
