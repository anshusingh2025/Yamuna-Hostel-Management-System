from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Complaint(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    room = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)   
     

    
    



class Student(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    dob = models.DateField()

    course = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50, blank=True)
    room = models.CharField(max_length=50)

    address = models.TextField()

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
class Attendance(models.Model):
    student_id = models.CharField(max_length=30)
    student_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=20)
    attendance_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ("Present", "Present"),
            ("Absent", "Absent"),
        ]
    )

    class Meta:
        ordering = ["room_no", "student_name"]
        constraints = [
            models.UniqueConstraint(
                fields=["student_id", "attendance_date"],
                name="unique_student_attendance_per_day"
            )
        ]

    def __str__(self):
        return f"{self.student_name} - {self.status} - {self.attendance_date}"


    def __str__(self):
        return self.student_name    

    
    


