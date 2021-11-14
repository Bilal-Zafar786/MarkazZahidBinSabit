from django.shortcuts import render,redirect
from django.views import View
from .models import Student_Registration

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'index.html')


class Registration(View):
    def get(self,request):
        return render(request,'registration.html')

    def post(self,request):
        postData = request.POST
        roll_number = postData.get('roll')
        name =postData.get('name')
        father_name = postData.get('f_name')
        B_Form = postData.get('bform')
        dob = postData.get('dob')
        cnic = postData.get('cnic')
        address = postData.get('address')
        cell = postData.get('cell')
        addmission = postData.get('addmission')
        promised_fee = postData.get('promised')

        data = {
            'roll_number':roll_number,
            'name':name,
            'father_name':father_name,
            'B_Form':B_Form,
            'dob':dob,
            'cnic':cnic,
            'address':address,
            'cell':cell,
            'addmission':addmission,
            'promised_fee':promised_fee
        }

        student_registration = Student_Registration(
            roll_number=roll_number,
            name=name,
            father_name=father_name,
            B_Form=B_Form,
            DOB=dob,
            address=address,
            phone=cell,
            addmission_date=addmission,
            promised_fee=promised_fee
        )
        student_registration.save()
        return redirect('registration')