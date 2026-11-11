from django.urls import path
from. import views

urlpatterns=[
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("Room/",views.Room,name="Room"),
    path("fee/",views.fee,name="fee"),
    path("gallery/",views.gallery,name="gallery"),
    path("contact/",views.contact,name="contact"),
    path("contactdata/",views.contactdata,name="contactdata"),
    path("faq/",views.faq,name="faq"),
    path("complaint/", views.complaint, name="complaint"),
    path("attendance/",views.attendance,name="attendance"),
    path("notice/",views.notice,name="notice"),
    path("profile/",views.profile,name="profile"),
    path("register/",views.register,name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("studentdashboard/", views.studentdashboard,name="studentdashboard"),
    path("logout/", views.logout, name="logout"),
    ]