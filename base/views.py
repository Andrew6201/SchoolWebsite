from django.shortcuts import render, redirect
from . models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def bachdegree(request):
    return render(request,'bachdegree.html')

def mastersdegree(request):
    return render(request,'mastersdegree.html')

def iot(request):
    return render(request, 'iot.html')

def nursing(request):
    return render(request, 'nursing.html')

def business(request):
    return render(request, 'business.html')

def engineering(request):
    return render(request, 'engineering.html')

def about(request):
    return render(request, 'about.html')

def applyinfo(request):
    return render(request, 'applyinfo.html')

def jointapp(request):
    return render(request, 'jointapp.html')

def directapp(request):
    return render(request, 'directapp.html')

def eligibility(request):
    return render(request, 'eligibility.html')

def studyplace(request):
    return render(request, 'studyplace.html')

def infostudents(request):
    return render(request, 'infostudents.html')

def howdirect(request):
    return render(request, 'howdirect.html')

def directselection(request):
    return render(request, 'directselection.html')

def directfees(request):
    return render(request, 'directfees.html')

def scholarship(request):
    return render(request, 'scholarship.html')

def howjoint(request):
    return render(request,'howjoint.html')

def jointselection(request):
    return render(request,'jointselection.html')

def jointfees(request):
    return render(request,'jointfees.html')

def digitalhealth(request):
    return render(request,'digitalhealth.html')

def energy(request):
    return render(request,'energy.html')

def howmasters(request):
    return render(request,'howmasters.html')

def masterfees(request):
    return render(request,'masterfees.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def applicationform(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        programme = request.POST['programme']
        email = request.POST['email']
        nationality = request.POST['nationality']
        age = request.POST['age']
        school = request.POST['school']
        gender = request.POST['gender']

        student = Student(firstname=firstname,lastname=lastname,programme=programme,email=email,nationality=nationality,age=age,school=school,gender=gender)
        student.save()
        return redirect('home')
    return render(request,'applicationform.html')


