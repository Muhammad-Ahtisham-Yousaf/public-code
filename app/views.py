from django.shortcuts import render, redirect
from django.http import HttpResponse

# User auth builtin forms
from django.contrib.auth.forms import UserCreationForm
from . djangoForms.registration import CustomRegistrationForm

# user auth builtin model
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return  render (request , 'main.html')

def candidate_registration (request):
    if request.method =='GET':
     form = CustomRegistrationForm()
    #  return HttpResponse (form)
     return render (request, 'Candidate/registration.html' ,{ 'form_data':form})
    else:
        form = CustomRegistrationForm(request.POST)
        # return HttpResponse(form)
        if form.is_valid():
            # return HttpResponse ('suscuss')
            form.save()
            return redirect(candidate_login) 
        else:
            return  HttpResponse (form.errors)

def candidate_login(request):
    return render (request, 'Candidate/login.html')

def employer_registration (request):
    return render (request, 'Employer/registration.html')

def employer_login(request):
    return render (request, 'Employer/login.html')

def aboutus (request):
    return render (request, 'aboutus.html')

def contact_us(request):
    return render (request, 'contact_us.html')

def job_posting(request):
    return render (request, 'job_posting.html')

def privacy_and_policy(request):
    return render (request, 'terms_of_user.html')

# def employer_login(request):
#     return render (request, 'Employer/login.html')

# def employer_login(request):
#     return render (request, 'Employer/login.html')

# def employer_login(request):
#     return render (request, 'Employer/login.html')