from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random
from .models import *
from .databases import *

def send_email(request):
    emailId = request.POST.get('email')    
    subject =  "test email"
    message = str(random.randint(1000,9999))
    sender_email = settings.EMAIL_HOST_USER  

    try:
        send_mail(subject, message, sender_email, [emailId])
        login = LoginDetails(
        email = emailId,
        otp = message
        )
        login.save()
        
    except Exception as e:
        messages.error(request, f'Error sending email: {str(e)}')
    
    

def otp_verification(request):
    email = "prakashpandianpython@gmail.com"
    otp_check = "7389"
    
    try:
        # Using get instead of filter to retrieve a single object
        user = LoginDetails.objects.get(email=email)
        stored_otp = user.otp
        
        # Check if the provided OTP matches the stored OTP
        if otp_check == stored_otp:
            print("Otp verified")
            return redirect('index')
        else:
            print("Otp verification failed")
            # Optionally, you can add a message to the context to display on the template
            context = {
                "error": "Invalid OTP. Please try again."
            }
            return render(request, 'otp_verification.html', context)
    
    except LoginDetails.DoesNotExist:
        print("User with this email does not exist")
        context = {
            "error": "User with this email does not exist."
        }
        return render(request, 'otp_verification.html', context)

    # In case of GET request or other methods, render the OTP verification page
    return render(request, 'otp_verification.html')

def email_login(request):
    return render(request,"email_login.html")

def email_login_otp(request):
    return render(request,"email_login_otp.html")

