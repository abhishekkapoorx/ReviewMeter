from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from Home.models import Course, Review
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
import random
import json
from Home.serializers import CourseSerializer, ReviewSerializer
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Create your views here.
def index(request):
    return render(request, "Home/index.html")


@login_required(login_url="/authenticate/sign-in/")
def addCourse(request):
    try:
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
    except Exception as e:
        messages.error(request, "Something went wrong, please try again.")
        return redirect("/add-course/")


@login_required(login_url="/authenticate/sign-in/")
def reviewCourse(request, courseid):
    try:
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
    except Exception as e:
        messages.error(request, "Something went wrong!")
        return redirect("/view-reviews/")


@login_required(login_url="/authenticate/sign-in/")
def editCourse(request, courseid):
    if request.method == "POST":
        try:
            course = Course.objects.filter(id=courseid).first()
            course.course_name = request.POST.get("coursename")
            course.course_description = request.POST.get("coursedescription")
            course.no_of_modules = request.POST.get("noofmodules")
            course.module_content = request.POST.get("modulecontent")
            course.author = request.POST.get("author")
            # course.published_date = request.POST.get("published")
            course.course_url = request.POST.get("courseurl")
            course.course_image = request.FILES.get("courseimage")
            course.save()
            messages.success(request, "Course Updated Successfully")
            return redirect("/")
        except Exception as e:
            messages.error(request, "Something went wrong!")
            return redirect("/view-reviews/")
    else:
        if request.user.is_superuser:
            course = Course.objects.filter(id=courseid).first()
            return render(request, "Home/editCourse.html", {"course": course})
        else:
            messages.error(request, "Not a Administrator")
            redirect("/")


@login_required(login_url="/authenticate/sign-in/")
def viewReviews(request):
    if request.method == "POST":
        try:
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
                    if reviews["avg"] == None:
                        courseList.append([c, 0])
                    else:
                        courseList.append([c, reviews["avg"]])
                    print(reviews)

            return render(request, "Home/viewReviews.html", {"courses": courseList})
        except Exception as e:
            messages.error(request, e)
            return redirect("/")
    else:
        try:
            courses = Course.objects.filter(accepted=True).all()
            courseList = []
            for c in courses:
                # print(c.id)
                reviews = Review.objects.filter(courseid=c.id, accepted=True).aggregate(
                    avg=Avg("overall_rating")
                )
                if reviews["avg"] == None:
                        courseList.append([c, 0])
                else:
                    courseList.append([c, reviews["avg"]])
                # courseList.append([c, reviews["avg"]])
            print(len(courseList))
            return render(request, "Home/viewReviews.html", {"courses": courseList})
        except Exception as e:
            messages.error(request, e)
            return redirect("/")


@login_required(login_url="/authenticate/sign-in/")
def viewReviewsByCourse(request, courseid):
    try:
        course = Course.objects.filter(id=courseid).first()
        reviews = Review.objects.filter(courseid=course, accepted=True).all()
        return render(
            request, "Home/viewReviewsByCourse.html", {"reviews": reviews, "course": course}
        )
    except Exception as e:
        messages.error(request, "Something went wrong!")
        return redirect("/view-reviews/")


@login_required(login_url="/authenticate/sign-in/")
def editReview(request, reviewid):
    pass


@login_required(login_url="/authenticate/sign-in/")
def compareCourse(request):
    return render(request, "Home/compareCourse.html")


@login_required(login_url="/authenticate/sign-in/")
def compareResults(request):
    if request.method == "POST":
        try:
            course1 = request.POST.get("course1-radio")
            course2 = request.POST.get("course2-radio")

            resCourse1 = Course.objects.get(id=course1)
            resCourse2 = Course.objects.get(id=course2)
            resReview1 = Review.objects.filter(
                courseid=resCourse1.id, accepted=True
            ).aggregate(
                overall=Avg("overall_rating"),
                relevence=Avg("relevence"),
                content_quality=Avg("content_quality"),
                instructor_expertise=Avg("instructor_expertise"),
                engagement=Avg("engagement"),
                clarity_of_explanation=Avg("clarity_of_explanation"),
                practical_application=Avg("practical_application"),
                support_resources=Avg("support_resources"),
                feedback_and_assessment=Avg("feedback_and_assessment"),
                flexibility=Avg("flexibility"),
                community_and_networking_opportunities=Avg(
                    "community_and_networking_opportunities"
                ),
                value_for_money=Avg("value_for_money"),
            )
            if resReview1["overall"] == None:
                resReview1 = {
                    "overall":0,
                    "relevence":0,
                    "content_quality":0,
                    "instructor_expertise":0,
                    "engagement":0,
                    "clarity_of_explanation":0,
                    "practical_application":0,
                    "support_resources":0,
                    "feedback_and_assessment":0,
                    "flexibility":0,
                    "community_and_networking_opportunities":0,
                    "value_for_money":0,
                }
            resReview2 = Review.objects.filter(
                courseid=resCourse2.id, accepted=True
            ).aggregate(
                overall=Avg("overall_rating"),
                relevence=Avg("relevence"),
                content_quality=Avg("content_quality"),
                instructor_expertise=Avg("instructor_expertise"),
                engagement=Avg("engagement"),
                clarity_of_explanation=Avg("clarity_of_explanation"),
                practical_application=Avg("practical_application"),
                support_resources=Avg("support_resources"),
                feedback_and_assessment=Avg("feedback_and_assessment"),
                flexibility=Avg("flexibility"),
                community_and_networking_opportunities=Avg(
                    "community_and_networking_opportunities"
                ),
                value_for_money=Avg("value_for_money"),
            )
            if resReview2["overall"] == None:
                resReview2 = {
                    "overall": 0,
                    "relevence": 0,
                    "content_quality": 0,
                    "instructor_expertise": 0,
                    "engagement": 0,
                    "clarity_of_explanation": 0,
                    "practical_application": 0,
                    "support_resources": 0,
                    "feedback_and_assessment": 0,
                    "flexibility": 0,
                    "community_and_networking_opportunities": 0,
                    "value_for_money": 0,
                }
            return render(
                request,
                "Home/compareResults.html",
                {
                    "course1": resCourse1,
                    "course2": resCourse2,
                    "review": zip(resReview1, resReview2),
                    "reviewcourse1": resReview1,
                    "reviewcourse2": resReview2,
                },
            )
        except Exception as e:
            return JsonResponse({"success": False, "message": f"{e}"}, status=500)
    else:
        messages.error(request, "Method not allowed")
        return redirect("/compare/")


def compareCourseList(request):
    if request.method == "POST":
        try:
            coursename = json.loads(request.body)["coursename"]
            course = Course.objects.filter(
                course_name__icontains=coursename, accepted=True
            ).all()
            courseserializer = CourseSerializer(course, many=True)
            return JsonResponse(
                {"success": True, "courses": courseserializer.data}, status=200
            )
        except Exception as e:
            return JsonResponse({"success": False, "message": f"{e}"}, status=500)
    else:
        messages.error(request, "Method not allowed")
        return redirect("/")


@login_required(login_url="/authenticate/sign-in/")
def aiInsights(request, courseid):
    if request.method == "POST":
        try:
            courseid = json.loads(request.body)["courseid"]
            course = Course.objects.filter(id=courseid, accepted=True).first()
            reviews = Review.objects.filter(courseid=course).all()
            # courseserializer = CourseSerializer(course)
            # reviewserializer = ReviewSerializer(reviews, many=True)

            llm = Ollama(model="llama3")
            reviewsStr = """"""

            for count, review in enumerate(reviews):
                reviewsStr += f"""
REVIEW {count}:
Review Description: "{review.review_desc}"
Overall rating: "{review.overall_rating}"
Relevence: "{review.relevence}"
Content Quality: "{review.content_quality}"
Instructor Expertise: "{review.instructor_expertise}"
Engagement: "{review.engagement}"
Clarity of Explanation: "{review.clarity_of_explanation}"
Practical Application: "{review.practical_application}"
Support Resources: "{review.support_resources}"
Feedback and Assessment: "{review.feedback_and_assessment}"
Flexibility: "{review.flexibility}"
Community and Networking Opportunities: "{review.community_and_networking_opportunities}"
Value for Money: "{review.value_for_money}"
\n
                
"""
            message = f"""
You are a helpful ai assistance. You have to give insights on courses whether a user should choose a course or not. You will be given with course details and reviews given by users. 

Course details are given below in triple backticks as a list of course detail fields:
```
Course Name: "{course.course_name}"
Course Description: "{course.course_description}"
No of Modules: "{course.no_of_modules}"
Module Content: "{course.module_content}"
Author: "{course.author}"
Published Date: "{course.published_date}"
Course URL: "{course.course_url}"
```

Reviews are given below in triple backticks as a list of dictionaries of reviews:
```
{reviewsStr}
```


"""
            message += "{input}"
            print(message)
            prompt = PromptTemplate.from_template(message)
            output_parser = StrOutputParser()
            # output_parser = JsonOutputParser()

            chain = prompt | llm | output_parser
            result = chain.invoke(
                {
                    "input": "Based on course details and reviews give review to user whether a user should choose a course or not. Tell user why and why not to choose a course."
                }
            )

            return JsonResponse({"success": True, "result": result}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "message": f"{e}"}, status=500)
    else:
        course = Course.objects.filter(id=courseid, accepted=True).first()
        return render(request, "Home/aiInsights.html", {"course": course})
