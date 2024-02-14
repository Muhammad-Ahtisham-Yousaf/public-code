from django.shortcuts import render, redirect
from django.http import HttpResponse


# user authentication
from django.contrib.auth import authenticate, login, logout

# user auth forms
from django.contrib.auth.forms import UserCreationForm
from .djangoForms.registration import CustomRegistrationForm
# from .forms.user_edit_form import UserChangeCustomForm

# user auth model
from django.contrib.auth.models import User

# flash messages
from django.contrib import messages
# Create your views here.
def home (request):
    # return HttpResponse( 'working')
    return  render (request , 'main.html')

def candidate_registration (request):
    if request.method == 'GET':
     form = CustomRegistrationForm()
    #  return HttpResponse (form)
     return render (request, 'Candidate/registration.html' ,{ 'form_data':form})
    else:
        form = CustomRegistrationForm(request.POST)
        # return HttpResponse(form)
        if form.is_valid():
            # return HttpResponse ('suscuss')
            form.save()
            # return HttpResponse(form)
            return redirect(dashboard) 
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
    
    
def dashboard (request):
       # return HttpResponse(request.user.is_authenticated)
    # if request.user.is_authenticated:
        users = User.objects.all()
        return render(request,'dashboard.html',{'users':users})
    # else:
        messages.error(request,'Kindly Login first')
        
        return HttpResponse(users)
        return  render (request,'dashboard.html')

def edit (request):
     return HttpResponse (' edituser')

def delete (request):
     return HttpResponse ('delete')

def  update (request):
   return HttpResponse ('update')