from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    passing_points = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True, blank=True)

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    content_path = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections', null=True)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    variants = models.JSONField(null=True)
    correct_variant = models.CharField(max_length=255, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='final_questions', null=True)
    is_final = models.BooleanField(default=False)
