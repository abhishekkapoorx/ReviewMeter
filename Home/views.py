from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from Home.models import Course, Review
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
import random


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
        print(proof_of_course)
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
        questions_dict = {
            "Overall Rating": [
                random.choice(
                    [
                        "How would you rate your overall experience with this course on a scale of 1 to 10?",
                        "What were the standout aspects of this course that contributed most to your overall impression?",
                        "Did this course meet or exceed your expectations? Please explain.",
                        "How likely are you to recommend this course to a friend or colleague?",
                        "What impact has this course had on your personal or professional growth?",
                        "How satisfied are you with the structure and organization of the course material?",
                        "How would you describe your emotional response to completing this course?",
                    ]
                ),
                "overall_rating",
            ],
            "Relevance": [
                random.choice(
                    [
                        "How relevant was the content of this course to your current needs or interests?",
                        "In what specific ways did this course address topics that are important to you?",
                        "Did this course cover the areas you expected it to, based on the description?",
                        "How applicable do you find the knowledge gained from this course to real-life scenarios?",
                        "Have you been able to implement any concepts learned in this course into your daily work or activities?",
                        "How would you rate the timeliness and relevance of the course content?",
                    ]
                ),
                "relevence",
            ],
            "Content Quality": [
                random.choice(
                    [
                        "How would you rate the depth and breadth of the content covered in this course?",
                        "Did the course materials (videos, readings, assignments) meet your expectations in terms of quality?",
                        "Were you challenged appropriately by the content of this course?",
                        "How engaging and interesting did you find the course content?",
                        "Were there any areas where the content could have been improved or expanded?",
                        "How well did the course content align with industry standards or best practices?",
                    ]
                ),
                "content-quality",
            ],
            "Instructor Expertise": [
                random.choice(
                    [
                        "What qualities did the instructor bring to the course that enhanced your learning experience?",
                        "How effective was the instructor in explaining complex topics?",
                        "Did the instructor demonstrate a deep understanding of the subject matter?",
                        "How responsive was the instructor to questions and feedback?",
                        "In what ways did the instructor motivate or inspire you throughout the course?",
                        "How would you rate the instructor's ability to keep your interest and attention?",
                    ]
                ),
                "ins-exp",
            ],
            "Engagement": [
                random.choice(
                    [
                        "Did this course keep you engaged throughout its duration?",
                        "What elements of the course design contributed most to your engagement?",
                        "How interactive was the course, and did this enhance your learning?",
                        "Were you encouraged to participate actively in discussions or activities?",
                        "Did the course provide enough opportunities for hands-on learning or practical application?",
                        "How well did the course maintain your interest from start to finish?",
                    ]
                ),
                "engagement",
            ],
            "Clarity of Explanation": [
                random.choice(
                    [
                        "How clear and understandable were the explanations provided in this course?",
                        "Were complex concepts explained in a way that was easy to grasp?",
                        "Did the course use examples or analogies effectively to clarify concepts?",
                        "Were there any areas where you found the explanations unclear or confusing?",
                        "How would you rate the overall communication skills of the instructor?",
                        "Did the course offer supplementary materials that helped clarify difficult topics?",
                    ]
                ),
                "clearity",
            ],
            "Practical Application": [
                random.choice(
                    [
                        "Were you able to apply the knowledge gained from this course to practical situations?",
                        "How well did the course prepare you for real-world challenges or tasks?",
                        "Can you give examples of how this course has impacted your professional or personal life?",
                        "Did the course provide actionable insights or skills that you can use immediately?",
                        "Were the practical exercises or assignments useful in reinforcing key concepts?",
                        "How relevant were the practical aspects of this course to your goals or objectives?",
                    ]
                ),
                "practicalapp",
            ],
            "Support Resources": [
                random.choice(
                    [
                        "How would you rate the availability and usefulness of support resources (e.g., forums, helpdesk)?",
                        "Were you able to easily access additional materials or support when needed?",
                        "Did you feel adequately supported by the course staff or community?",
                        "How responsive was the support team to your inquiries or issues?",
                        "Were there any specific resources or tools provided that you found particularly helpful?",
                        "Did the course offer enough supplementary resources to enhance your learning experience?",
                    ]
                ),
                "supportres",
            ],
            "Feedback and Assessment": [
                random.choice(
                    [
                        "How valuable were the feedback and assessments provided during this course?",
                        "Did the course assessments accurately reflect your understanding of the material?",
                        "Were you satisfied with the quality and timeliness of the feedback you received?",
                        "How did the course assessments contribute to your learning process?",
                        "Did the course encourage self-assessment and reflection?",
                        "Were there opportunities for peer feedback or review?",
                    ]
                ),
                "feedback",
            ],
            "Flexibility": [
                random.choice(
                    [
                        "How flexible was the course structure in accommodating your schedule or learning pace?",
                        "Were you able to navigate the course materials easily?",
                        "Did the course offer options for customization or personalization?",
                        "Were deadlines or timelines reasonable and manageable?",
                        "How well did the course adapt to different learning styles or preferences?",
                        "Were there opportunities to revisit or review content based on your needs?",
                    ]
                ),
                "flexibility",
            ],
            "Community and Networking Opportunities": [
                random.choice(
                    [
                        "How valuable were the networking or community aspects of this course?",
                        "Did you engage with other learners or professionals through this course?",
                        "Were there opportunities to collaborate or share ideas with fellow participants?",
                        "How supportive was the course community in facilitating discussions or knowledge sharing?",
                        "Did the course foster a sense of belonging or connection with others?",
                        "Have you continued to stay in touch with individuals you met through this course?",
                    ]
                ),
                "networking",
            ],
            "Value for Money": [
                random.choice(
                    [
                        "Do you feel that the course provided good value for the cost?",
                        "How does this course compare to others you have taken in terms of value?",
                        "Did the benefits and outcomes of the course justify the investment?",
                        "Would you have been willing to pay more or less for this course based on your experience?",
                        "How would you rate the return on investment (ROI) of this course?",
                        "Did the course meet your expectations in terms of the value delivered?",
                    ]
                ),
                "valueformoney",
            ],
        }

        return render(
            request,
            "Home/reviewCourse.html",
            {"course": course, "questions_dict": questions_dict},
        )
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
                # print(c.id)
                reviews = Review.objects.filter(
                    courseid=c.id, accepted=True
                ).aggregate(avg=Avg("overall_rating"))

                courseList.append([c, reviews["avg"]])

        return render(request, "Home/viewReviews.html", {"courses": courseList})
    else:
        courses = Course.objects.filter(accepted=True).all()
        courseList = []
        for c in courses:
            # print(c.id)
            reviews = Review.objects.filter(courseid=c.id, accepted=True).aggregate(
                avg=Avg("overall_rating")
            )
            courseList.append([c, reviews["avg"]])
        print(len(courseList))
        return render(request, "Home/viewReviews.html", {"courses": courseList})


@login_required(login_url="/authenticate/sign-in/")
def viewReviewsByCourse(request, courseid):
    course = Course.objects.filter(id=courseid).first()
    reviews = Review.objects.filter(courseid=course, accepted=True).all()
    return render(
        request, "Home/viewReviewsByCourse.html", {"reviews": reviews, "course": course}
    )
