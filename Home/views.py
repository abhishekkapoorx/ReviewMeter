from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Home.models import Course, Review
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "Home/index.html")

@login_required(login_url="/authenticate/sign-in/")
def addCourse(request):
    if request.method == "POST":
        courseName = request.POST.get("coursename")
        courseDescription = request.POST.get("coursedescription")
        noofmodules = request.POST.get("noofmodules")
        modulecontent = request.POST.get("modulecontent")
        author = request.POST.get("author")
        published = request.POST.get("published")
        courseurl = request.POST.get("courseurl")
        courseimage = request.FILES.get("courseimage")

        course = Course(
            course_name=courseName,
            course_description=courseDescription,
            no_of_modules=noofmodules,
            module_content=modulecontent,
            author=author,
            published_date=published,
            course_url=courseurl,
            course_image=courseimage,
        )
        course.save()
        messages.success(request, "Course saved successfully.")
    return render(request, "Home/addCourse.html")


@login_required(login_url="/authenticate/sign-in/")
def reviewCourse(request, courseid):
    if request.method == "POST":
        review_description = request.POST.get("reviewdescription")
        overall_rating = request.POST.get("overall_rating")
        relevence = request.POST.get("relevence")
        content_quality = request.POST.get("content-quality")
        instructor_expertise = request.POST.get("ins-exp")
        engagement = request.POST.get("engagement")
        clarity_of_explanation = request.POST.get("clearity")
        practical_application = request.POST.get("practicalapp")
        support_resources = request.POST.get("supportres")
        feedback_and_assessment = request.POST.get("feedback")
        flexibility = request.POST.get("flexibility")
        community_and_networking_opportunities = request.POST.get("networking")
        value_for_money = request.POST.get("valueformoney")
        proof_of_course = request.FILES.get("courseproof")
        course = Course.objects.get(id=courseid)
        review = Review(
            review_desc=review_description,
            overall_rating=overall_rating,
            relevence=relevence,
            content_quality=content_quality,
            instructor_expertise=instructor_expertise,
            engagement=engagement,
            clarity_of_explanation=clarity_of_explanation,
            practical_application=practical_application,
            support_resources=support_resources,
            feedback_and_assessment=feedback_and_assessment,
            flexibility=flexibility,
            community_and_networking_opportunities=community_and_networking_opportunities,
            value_for_money=value_for_money,
            proof_of_course=proof_of_course,
            courseid=course,
            userid=request.user,
        )
        review.save()
        messages.success(request, "Review saved successfully.")
        return redirect("/")
    else:
        course = Course.objects.get(id=courseid)
        return render(request, "Home/reviewCourse.html", {"course": course})
    # return render(request, "Home/reviewCourse.html")


@login_required(login_url="/authenticate/sign-in/")
def viewReviews(request):
    if request.method == "POST":
        course = request.POST.get("course")
        courses = Course.objects.filter(accepted=True).all()
        courseList = []
        for c in courses:
            if (
                course.lower() in c.course_name.lower()
                or course.lower() in c.course_url.lower()
            ):
                courseList.append(c)
        return render(request, "Home/viewReviews.html", {"courses": courseList})
    else:
        courseList = Course.objects.filter(accepted=True).all()
        print(len(courseList))
        return render(request, "Home/viewReviews.html", {"courses": courseList})


@login_required(login_url="/authenticate/sign-in/")
def viewReviewsByCourse(request, courseid):
    course = Course.objects.filter(id=courseid).first()
    reviews = Review.objects.filter(courseid=course, accepted=True).all()
    return render(
        request, "Home/viewReviewsByCourse.html", {"reviews": reviews, "course": course}
    )
