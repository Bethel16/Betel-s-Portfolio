from django.shortcuts import render
from .models import *

def index(request):
    genral_skills = GeneralSkill.objects.all()  # Fetch skills from the database
    my_profile = Profile.objects.first()   
    specific_skill = SpecificSkill.objects.all()
    institutions = Education.objects.all()
    projects= Project.objects.all()
    project_imgs = Project.objects.prefetch_related('images').all()  # Prefetch images to optimize queries
    experiences = Experience.objects.all()
    services = Service.objects.all()
    status = Status.objects.first() 
    categories = Category.objects.prefetch_related('projects').all()
    general_skills = GeneralSkill.objects.prefetch_related('specific_skills').all()

 

    context = {
        'genral_skills': genral_skills,
        'my_profile': my_profile ,
        'specific_skill': specific_skill,
        'institutions': institutions,
        'projects': projects,
        'project_imgs': project_imgs,
        'experiences': experiences, 
        'services': services,
        'status': status, 
        'categories': categories , 
        'general_skills': general_skills,
    }
    return render(request , 'index.html',context)


from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages

def send_to_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  # Customer's email from the form
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Validate required fields
        if not name or not email or not message:
            messages.error(request, 'All required fields must be filled.')
            return JsonResponse({'error': 'All required fields must be filled.'}, status=400)

        try:
            # Compose the email
            subject = f"Contact form message from {name}"
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

            # Create the email message
            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.EMAIL_HOST_USER,  # Your verified email address
                to=[settings.EMAIL_HOST_USER],  # Where you want to receive the email (your email)
                reply_to=[email]  # Reply-to is the customer's email
            )

            # Send the email
            email_message.send(fail_silently=False)
            messages.success(request, 'Email sent successfully!')
            return JsonResponse({'message': 'Email sent successfully'}, status=200)

        except Exception as e:
            messages.error(request, 'An error occurred. Please try again later.')
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
