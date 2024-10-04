from django.db import models

# Profile and Contact Information
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)  # Fixed typo from 'Last_name' to 'last_name'
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile image field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Fixed __str__ method

# General Skills
class GeneralSkill(models.Model):
    skill_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome or other icon class", null=True)  # Add this field


    def __str__(self):
        return self.skill_name


# Specific Skills linked to General Skills
class SpecificSkill(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Skill level from 1-100")
    general_skill = models.ForeignKey(GeneralSkill, related_name='specific_skills', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.skill_name} ({self.proficiency}%)"


# Services Offered
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    service_image = models.ImageField(upload_to='service_images/', blank=True, null=True)  # Image for the service

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(blank=True)
    completion_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title



class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"{self.project.title} Image"


# Education
class Education(models.Model):
    institution = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=True, null=True)
    institution_image = models.ImageField(upload_to='institution_image/', blank=True, null=True)  # Image for the project
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f"{self.completed} - {self.institution}"

# Certifications
class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

# Experience
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.job_title

# Social Media Links
class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()

    def __str__(self):
        return self.platform_name

class Status(models.Model):
    happy_client = models.IntegerField()
    project_completed = models.IntegerField()
    certification = models.IntegerField()
    experience_year = models.IntegerField()

    def __str__(self):
        return self.happy_client
