from django.db import models

# Create your models here.
# class User (models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255,null=True)
#     email = models.EmailField()
#     contact_no = models.CharField(max_length=30)
#     CV = models.FileField(upload_to='static/',null=True)



#     def __str__(self):
#         return f' {self.id} -  {self.first_name} - {self.last_name} - {self.email} - {self.contact_no}' 

# class Myuser (models.Model):
#     full_name = models.CharField(max_length=150)
    
#     email = models.EmailField(max_length=150)

#     contact_no = models.CharField(max_length=150)
   
#     def __str__(self):
#         return f'User :{self.username}'
#         # return f' {self.id} -  {self.f_name} - {self.l_name} - {self.email} - {self.contact_no}' 