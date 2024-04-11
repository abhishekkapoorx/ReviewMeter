from django.contrib import admin
from Home.models import Course, CourseAdmin, Review, ReviewAdmin

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Review, ReviewAdmin)