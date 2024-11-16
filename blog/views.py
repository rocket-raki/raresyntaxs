from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from .models import ContactFormSubmission
from django.views.decorators.csrf import csrf_exempt
from .pages import *
from .looks import *

# Create your views here.


def home(request):
    css = HomeLook()
    context = {
        'css':css,
        'blogname':'Rare Syntax',
        'tagline':'Thoughts, Stories, and Ideas',
        'posts' : [
        {'blogtitle': 'Python', 'date': 'November 14, 2024', 'description': 'An introductory guide to Python programming and its applications.'},
        {'blogtitle': 'Java', 'date': 'November 13, 2024', 'description': 'Explore Java and its versatility in building cross-platform applications.'},
        {'blogtitle': 'JavaScript', 'date': 'November 12, 2024', 'description': 'Learn about JavaScript, the backbone of web development.'},
        {'blogtitle': 'Django', 'date': 'November 11, 2024', 'description': 'Django makes web development easy and efficient. Here’s how!'},
        {'blogtitle': 'Machine Learning', 'date': 'November 10, 2024', 'description': 'Introduction to machine learning concepts and algorithms.'},
        {'blogtitle': 'Data Science', 'date': 'November 9, 2024', 'description': 'Dive into data science, from data analysis to visualization.'},
        {'blogtitle': 'React', 'date': 'November 8, 2024', 'description': 'Build interactive UIs with React, a popular JavaScript library.'},
        {'blogtitle': 'Flask', 'date': 'November 7, 2024', 'description': 'Learn Flask, a lightweight web framework for Python developers.'},
        {'blogtitle': 'SQL', 'date': 'November 6, 2024', 'description': 'Understand the basics of SQL for database management.'}
    ]
    }
    html_content = HomePage()
    
   
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})




def about(request):
    css = AboutLook()
    html_content = AboutPage()
    context={
        'title':'about',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})





@csrf_exempt
def contact(request):
    # Define CSS content
    css = ContactLook()
   
    if request.method == 'POST':
    # CSRF token will be verified automatically here
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        inquiry_type = request.POST.get('inquiry-type')
        message = request.POST.get('message')
        preferred_contact_method = request.POST.getlist('contact-method')
        preferred_contact_time = request.POST.get('contact-time')

    # Save form data
        contact_submission = ContactFormSubmission(
           full_name=full_name,
           email=   email,
           phone=phone,
           subject=subject,
           inquiry_type=inquiry_type,
           message=message,
           preferred_contact_method=", ".join(preferred_contact_method),
           preferred_contact_time=preferred_contact_time
           )
        contact_submission.save()

    # Redirect after saving
        return redirect('contact') 

    # Passing the context to the template
    context = {
        'title': 'Contact Us',
        'css': css
    }

    html_content = ContactPage()
    context={
        'title':'contact',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})





  
def gallery(request):
    css = GalleryLook() 

    html_content = GalleryPage()
    context={
        'title':'gallery',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    


def reviews(request):
    css = ReviewsLook()
    html_content = ReviewsPage()
    
    
    context={
        'title':'about',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})











def courses(request):
    css = CoursesLook()
    html_content = CoursesPage()
    context={
        'title':'courses',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})

  



def course(request, course):
    css = CourseLook()

    # Dummy course data (to be replaced with database in a real app)
    courses = {
        "python": {
            "title": "Python Programming",
            "description": "Learn the basics and advanced concepts of Python programming. This course will take you from beginner to expert, covering everything from syntax to building real-world applications.",
            "image": "https://bigblue.academy/images/image/blog/python-courses/204.jpg ",
        },
        "javascript": {
            "title": "JavaScript for Web Development",
            "description": "Master JavaScript and create interactive websites. This course covers both the fundamentals and advanced techniques for modern web development.",
            "image": "https://img-c.udemycdn.com/course/480x270/5422984_16fc_2.jpg ",
        },
        "django": {
            "title": "Django for Web Development",
            "description": "Learn how to build dynamic, secure, and scalable web applications using Django. This course teaches you the power of Python-based web development.",
            "image": "https://www.creative-tim.com/blog/content/images/2021/09/cover-ct-django-cheat-sheet.png",
        },
    }

    # Check if the course exists
   


    html_content = CoursePage()
    # Context to pass to the template
    
    context={
        'title':'gallery',
        'css':css,
        'course':courses[course]
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    




def course_learn(request, course_name, course_level):
    css = CourselearnLook()

    # Course data for different levels and courses (Python, JavaScript, Django)
    courses = {
        "python": {
            "beginner": {
                "title": "Python for Beginners",
                "description": "Learn the basics of Python programming. This course will cover syntax, basic libraries, and getting started with programming.",
                "image": "https://goedu.ac/wp-content/uploads/2021/11/Python-for-beginners.png",
            },
            "intermediate": {
                "title": "Intermediate Python",
                "description": "Take your Python skills to the next level with topics like object-oriented programming (OOP), file handling, and more advanced libraries.",
                "image": "https://blob.sololearn.com/assets/python-intermediate-web-og-v1.png",
            },
            "advanced": {
                "title": "Advanced Python",
                "description": "Dive deep into Python's advanced features like decorators, generators, multi-threading, and building efficient algorithms.",
                "image": "https://purpletutor.com/wp-content/uploads/2023/02/advance-python.jpeg",
            },
        },
        "javascript": {
            "beginner": {
                "title": "JavaScript for Beginners",
                "description": "Learn the fundamentals of JavaScript, one of the most popular programming languages for web development.",
                "image": "https://static.skillshare.com/uploads/video/thumbnails/0ab63be061d2a2051fc5a20337d2bc7f/original",
            },
            "intermediate": {
                "title": "Intermediate JavaScript",
                "description": "Deepen your understanding of JavaScript with topics like async programming, DOM manipulation, and modern JavaScript frameworks.",
                "image": "https://static-assets.codecademy.com/assets/course-landing-page/meta/4x3/learn-intermediate-javascript.jpg",
            },
            "advanced": {
                "title": "Advanced JavaScript",
                "description": "Master advanced concepts like closures, the event loop, and building complex applications with JavaScript.",
                "image": "https://cdn0.knowledgecity.com/opencontent/courses/previews/CMP1282/800--v112252.jpg",
            },
        },
        "django": {
            "beginner": {
                "title": "Django for Beginners",
                "description": "Learn how to build web applications using Django, one of the most popular web frameworks in Python.",
                "image": "https://codewithstein.com/media/media/uploads/course_images/Cws_-_premium.006.jpeg",
            },
            "intermediate": {
                "title": "Intermediate Django",
                "description": "Take your Django skills to the next level by learning advanced techniques like creating APIs, using Django Rest Framework, and working with databases.",
                "image": "https://justdjango.com/_next/image?url=https%3A%2F%2Fjustdjango-static.sfo2.digitaloceanspaces.com%2Fmedia%2Fcourse_thumbnails%2Fintermediate.png&w=1920&q=75",
            },
            "advanced": {
                "title": "Advanced Django",
                "description": "Master Django with advanced concepts such as optimization, security, and deployment strategies.",
                "image": "https://d3s1xydsbc15sr.cloudfront.net/media/elearning/skill/Django_Advanced.jpg",
            },
        },
    }

    html_content = CourselearnPage()
    context={
        'course':courses[course_name][course_level],
        'title':course_name,
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    
