from rest_framework import serializers
from Home.models import Course, Review

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "course_name",
            "course_description",
            "author",
            "published_date",
            "course_image",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
