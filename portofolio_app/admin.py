from django.contrib import admin
from .models import Profile, GeneralSkill,ProjectImage,Status , Category , SpecificSkill, Service, Project, Education, Certification, Experience, SocialMedia

# Register your models with the Django admin site
admin.site.register(Profile)
admin.site.register(GeneralSkill)
admin.site.register(SpecificSkill)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience)
admin.site.register(SocialMedia)
admin.site.register(ProjectImage)
admin.site.register(Category)
admin.site.register(Status)


