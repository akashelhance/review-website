
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def Contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        send_mail(subject= subject,message= message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list = [email],fail_silently  = True,)
        return render(request,'home.html')
    return render(request,'contact.html',{})

# Create your views here.
def allcourse(request):
    return render(request, 'allcourse.html')

def addcourse(request):
    return render(request,'addcourse.html')


def Home(request):
    return render(request,'home.html')



def About(request):
    return render(request,'about.html')

def courseDetail(request , pk):
  
    return render(request, 'course_details.html')

    



