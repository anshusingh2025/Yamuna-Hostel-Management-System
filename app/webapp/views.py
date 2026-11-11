from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Contact, Complaint , Student, Attendance
from django.utils import timezone
from django.contrib import messages





def index(request):
    return render(request,"index.html")

   
def about(request):
    return render(request,"about.html")

def Room(request):
    return render(request,"Room.html")

def fee(request):
    return render(request,"fee.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            subject=subject,
            message=message
        )
    
    
    return render(request, 'contact.html')


#data show
def contactdata(request):
    
    students=Contact.objects.all()
    
    return render(request,"contactdata.html",{
       "students":students
    })
    

def faq(request):
    return render(request,"faq.html")

def complaint(request):

    if request.method == "POST":

        name = request.POST.get("name")
        category = request.POST.get("category")
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        room = request.POST.get("room")
        priority = request.POST.get("priority")

        Complaint.objects.create(
            name=name,
            category=category,
            subject=subject,
            description=description,
            room=room,
            priority=priority,
        )

        return redirect("complaint")

    complaints = Complaint.objects.all().order_by("-id")

    return render(request, "complaint.html", {
        "complaints": complaints
    })

def attendance(request):
    room_no = request.GET.get("room")

    return render(request, "attendance.html", {"room_no": room_no})


def notice(request):
    return render(request, "notice.html")

    
@login_required
def profile(request):
    student = Student.objects.filter(
        username=request.user.username
    ).first()

    return render(request, "hostel/profile.html", {
        "student": student
    })





def register(request):

    if request.method == "POST":

        student_name = request.POST.get("student_name")
        father_name = request.POST.get("father_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")

        course = request.POST.get("course")
        year = request.POST.get("year")
        roll_no = request.POST.get("roll_no")
        room = request.POST.get("room")

        address = request.POST.get("address")

        username = request.POST.get("username")
        password = request.POST.get("password")

        if Student.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        # Student table me registration data save hoga
        Student.objects.create(
            student_name=student_name,
            father_name=father_name,
            email=email,
            mobile=mobile,
            gender=gender,
            dob=dob,
            course=course,
            year=year,
            roll_no=roll_no,
            room=room,
            address=address,
            username=username,
            password=password
        )

        # Django login ke liye User create hoga
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")    
   
    


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")
     

@login_required
def dashboard(request):

    # Jo student abhi login hai
    current_student = Student.objects.filter(
        username=request.user.username
    ).first()

    context = {
        "current_student": current_student,
    }

    return render(request, "hostel/dashboard.html", context)




def studentdashboard(request):

    student = Student.objects.filter(
        Q(username=request.user.username) |
        Q(email=request.user.email)
        
    ).first()

    return render(
        request,
        "studentdashboard.html",
        {
            "student": student
        }
    )

def logout(request):
    return render(request, "logout.html",)
    