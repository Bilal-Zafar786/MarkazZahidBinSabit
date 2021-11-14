from django.db import models

# Create your models here.
class Student_Registration(models.Model):
    roll_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    B_Form = models.ImageField(upload_to="B_Form/",default="")
    DOB = models.DateField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=30)
    addmission_date = models.DateField()
    promised_fee = models.IntegerField()
    class Meta:
        db_table = 'student_registration'
