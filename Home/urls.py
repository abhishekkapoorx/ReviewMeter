"""
URL configuration for ReviewMeter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from Home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-course/", views.addCourse, name="addCourse"),
    path("edit-course/<int:courseid>", views.editCourse, name="editCourse"),
    path("review-course/<int:courseid>", views.reviewCourse, name="reviewCourse"),
    path("view-reviews/", views.viewReviews, name="viewReviews"),
    path("view-reviews/<int:courseid>", views.viewReviewsByCourse, name="viewReviews"),
    path("edit-reviews/<int:reviewid>", views.editReview, name="editReviews"),
]
