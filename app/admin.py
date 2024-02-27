from django.contrib import admin
from .models import JobPosting , UserDetails, EditUser

class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('id','job_title','job_location','skills_required','posting_date','salary','industry','education','experience_required', 'gender', 'company_name')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','industry','company','contact_no','location','user','type') 

admin.site.register(UserDetails,UserDetailsAdmin)

#  Register your models here.
admin.site.register(JobPosting,JobPostingAdmin)
# # admin.site.register(Myuser,MyAdmin)

class EditUserAdmin(admin.ModelAdmin):
    list_display = ('id','location','mobile_no','skills','joining_date','education','university','priveus_job','interests', 'gender')

#  Register your models here.
admin.site.register(EditUser,EditUserAdmin)
# # admin.site.register(Myuser,MyAdmin)