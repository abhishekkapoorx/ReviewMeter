from datetime import datetime
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import time


# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=500, default="")
    course_description = models.TextField(max_length=5000, default="")
    no_of_modules = models.IntegerField(default=0)
    module_content = models.TextField(max_length=5000, default="")
    author = models.CharField(max_length=50, default="")
    published_date = models.DateField(default=datetime.now)
    course_image = models.ImageField(
        upload_to="course_images/"
    )
    course_url = models.URLField(max_length=500, default="")
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.course_name} created by {self.author} on {self.published_date}"


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course_name",
        "course_description",
        "no_of_modules",
        "author",
        "published_date",
        "course_image",
        "course_url",
        "accepted"
    )
    list_filter = [
        "accepted"
    ]

"""
Review model description
# 

- [ ]  id
- [ ]  course id (if Already Added)
- [ ]  course url (if not already Added)
- [ ]  overall rating
- [ ]  Relevence
- [ ]  Content Quality
- [ ]  Instructor Expertise
- [ ]  Engagement
- [ ]  Clarity of Explanation
- [ ]  Practical Application
- [ ]  Support Resources
- [ ]  Feedback and Assessment
- [ ]  Flexibility
- [ ]  Community and Networking Opportunities
- [ ]  Value for Money

"""
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    courseid = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="reviews"
    )
    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review_desc = models.TextField(default="", max_length=2000)
    overall_rating = models.IntegerField(default=0)
    relevence = models.IntegerField(default=0)
    content_quality = models.IntegerField(default=0)
    instructor_expertise = models.IntegerField(default=0)
    engagement = models.IntegerField(default=0)
    clarity_of_explanation = models.IntegerField(default=0)
    practical_application = models.IntegerField(default=0)
    support_resources = models.IntegerField(default=0)
    feedback_and_assessment = models.IntegerField(default=0)
    flexibility = models.IntegerField(default=0)
    community_and_networking_opportunities = models.IntegerField(default=0)
    value_for_money = models.IntegerField(default=0)
    accepted = models.BooleanField(default=False)
    proof_of_course = models.FileField(
        upload_to="course_proof/"
    )

    def __str__(self):
        return f"{self.id} {self.courseid} created by {self.courseid.author} on {self.courseid.published_date}"

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "courseid",
        # "course_url",
        "overall_rating",
        "accepted",
        "relevence",
        "content_quality",
        "instructor_expertise",
        "engagement",
        "clarity_of_explanation",
        "practical_application",
        "support_resources",
        "feedback_and_assessment",
        "flexibility",
        "community_and_networking_opportunities",
        "value_for_money",
        "proof_of_course",
        "accepted"

    )
    list_filter = ["accepted"]
