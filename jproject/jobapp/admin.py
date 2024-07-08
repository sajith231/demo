from django.contrib import admin
from django.utils.html import format_html
from .models import Job,Application
from .models import UserProfile

# Register your models here.




class JobAdmin(admin.ModelAdmin):
    list_display = ['title','description','location','company_name','salary','logo' ]

    site_header = 'Your Project Name Admin'
    site_title = 'Your Project Name Admin'

    def display_image(self, obj):
        # Assuming 'image' is the name of the ImageField in your Product model
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None

    display_image.short_description = 'Image'
    

admin.site.register(Job,JobAdmin)





@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'download_resume']

    def download_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}">Download</a>', obj.resume.url)
        else:
            return 'No resume uploaded'
        
    download_resume.allow_tags = True
    download_resume.short_description = 'Resume Download'




@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'user_profile', 'last_name', 'download_resume', 'phone_number', 'email', 'experience', 'qualification', 'skills']

    def job_title(self, obj):
        return obj.job.title if obj.job else '-'

    job_title.short_description = 'Job Title'

    def user_profile(self, obj):
        return obj.candidate.userprofile.first_name if obj.candidate.userprofile else obj.candidate.username

    user_profile.short_description = 'User Profile'

    def last_name(self, obj):
        return obj.candidate.last_name if obj.candidate.last_name else '-'

    def download_resume(self, obj):
        if obj.candidate.userprofile and obj.candidate.userprofile.resume:
            return format_html('<a href="{}">Download</a>', obj.candidate.userprofile.resume.url)
        else:
            return 'No resume uploaded'
        
    download_resume.allow_tags = True
    download_resume.short_description = 'Resume Download'

    def phone_number(self, obj):
        return obj.candidate.userprofile.phone_number if obj.candidate.userprofile and obj.candidate.userprofile.phone_number else '-'

    def email(self, obj):
        return obj.candidate.email if obj.candidate.email else '-'

    def experience(self, obj):
        return obj.candidate.userprofile.experience if obj.candidate.userprofile and obj.candidate.userprofile.experience else '-'

    def qualification(self, obj):
        return obj.candidate.userprofile.qualification if obj.candidate.userprofile and obj.candidate.userprofile.qualification else '-'

    def skills(self, obj):
        return obj.candidate.userprofile.skills if obj.candidate.userprofile and obj.candidate.userprofile.skills else '-'