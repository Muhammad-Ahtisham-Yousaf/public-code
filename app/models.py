from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobPosting (models.Model):
    job_title = models.CharField(max_length=255, null = True )
    job_location = models.CharField(max_length=255,null =True)
    job_description = models.TextField( null =True )
    skills_required = models.CharField(max_length=200, null =True)
    posting_date = models.CharField(max_length=100, null =True)
    salary = models.CharField(max_length=255,null =True)
#     company_logo = models.ImageField(null =True,upload_to='app' ,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5RhqcwxGDJustOfPZ5ybmAWzysfuMvTAYoUyVx63gKBwNRIeMm9kDwlS5NEN6I6vrnac&usqp=CAU' )
    industry = models.CharField(max_length =66,null =True)
    education = models.CharField(max_length=70,null =True)
    experience_required = models.CharField(max_length =200,null =True)
    gender = models.CharField(max_length =200,null =True)
    company_name = models.CharField(max_length =200, default='Company Name')
    name = models.CharField(max_length =200,default=' Name')
    mobile_no = models.CharField(max_length =200,default='Mobile Number')
    email = models.EmailField(max_length =200,default='something@gmail.com')

    def __str__(self):
         return f' {self.id} -  {self.job_title} - {self.job_location} - {self.job_description}  - {self.skills_required} - {self.posting_date} - {self.salary} - {self.industry} - {self.education}-{self.experience_required} -{self.company_name} -{self.name} -{self.mobile_no} -{self.email}' 

class Employer (models.Model):
     full_name = models.CharField(max_length=150)
     industry =models.CharField (max_length =100)
     company =models.CharField (max_length =100)
     contact_no = models.CharField(max_length=150)
     email = models.EmailField(max_length=150)
     location = models.CharField(max_length=150)
     password =models.CharField(max_length =8)


     def __str__(self):
        #  return f'User :{self.username}'
          return f' {self.id} -  {self.full_name} - {self.industry} - {self.email} - {self.contact_no} - {self.location} - {self.password}' 
     
#    User Edit Form
class UserDetails (models.Model):
     industry =models.CharField (max_length =100,null=True)
     company =models.CharField (max_length =100)
     contact_no = models.CharField(max_length=150,null=True)
     location = models.CharField(max_length=150,null=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE )
     type = models.IntegerField(max_length = 1, default = 0)




class EditUser (models.Model):
    location = models.CharField(max_length=255, null = True )
    mobile_no = models.CharField(max_length=255,null =True)
    about_me = models.TextField( null =True )
    skills = models.CharField(max_length=200, null =True)
    joining_date = models.CharField(max_length=100, null =True)
    education = models.CharField(max_length=255,null =True)
#     company_logo = models.ImageField(null =True,upload_to='app' ,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5RhqcwxGDJustOfPZ5ybmAWzysfuMvTAYoUyVx63gKBwNRIeMm9kDwlS5NEN6I6vrnac&usqp=CAU' )
    university = models.CharField(max_length =66,null =True)
    priveus_job = models.CharField(max_length=70,null =True)
    projects = models.CharField(max_length =200,null =True)
    project_desc = models.CharField(max_length =200,null =True)
    interests = models.CharField(max_length =200)
    gender = models.CharField(max_length =200,default='None')
#     name = models.CharField(max_length =200,default=' Name')
#     mobile_no = models.CharField(max_length =200,default='Mobile Number')
#     email = models.EmailField(max_length =200,default='something@gmail.com')

    def __str__(self):
         return f' {self.id} -  {self.location} - {self.mobile_no} - {self.about_me}  - {self.skills} - {self.joining_date} - {self.education} - {self.university} - {self.education}-{self.priveus_job} -{self.projects} -{self.projects} -{self.project_desc} -{self.interests-{self.gender}}' 