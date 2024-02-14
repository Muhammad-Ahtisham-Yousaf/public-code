from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('candidate_registration/',views.candidate_registration, name='candidate_registration'), 
    path('employer_registration/',views.employer_registration, name='employer_registration'),
    path('employer_login/',views.employer_login, name='employer_login'),
    path('candidate_login/',views.candidate_login, name='candidate_login'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('job_posting/',views.job_posting, name='job_posting'),
    path('privacy_and_policy/',views.privacy_and_policy, name='privacy_and_policy'),
    path('dashboard/',views.dashboard, name='dashboard'),
   


     path('edit/<int:id>',views.edit, name='edit'),
    path('delete/<int:id>',views.delete, name='delete'),
     path('update/',views.update, name='update')
]