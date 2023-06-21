from django.shortcuts import render, redirect, HttpResponse
from .models import RegisterData
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.urls import reverse


def login_page(request):
    if request.method == "POST" :
        fetched_data = RegisterData.objects.all()
        user_name = request.POST['userName']
        password = request.POST['userPassword']
        print("Username : ",user_name)
        print("")
        print("Password : ",password)
        # print(fetched_data)
        userData_dict = {}
        for x in reversed(fetched_data):
            userData_dict.update({x.username : x.password })
        # print(userData_dict)
        if user_name not in userData_dict:
            messages.success(request, 'User not found..!')
        elif password not in userData_dict.values() : 
            messages.success(request,'Password is incorrect...!')
        else : 
            messages.success(request, 'Logged In..!')
            return redirect('landingPage/')
    return render(request,'index.html')
        


def AnotherLoginPage(request):
    return render(request, 'another_index.html')

def signup(request):
    global register_data
    register_data = RegisterData()
    if request.method == "POST" :
        print(request.POST)
        email = request.POST['userName']
        password = request.POST['userPassword']
        confirmPassword = request.POST['ConfirmUserPassword']
        signup_gpt(request)
        return redirect('registerpage')
    else :
        pass
    return render(request,'register.html')

def homePage(request,email):
    email = email
    subject = "Registration Confirmation"
    message = '''
        Dear {},

        Thank you for registering with our service. We are excited to have you on board!

        To complete the registration process, please click on the following link:

        [Registration Confirmation Link]

        If you did not initiate this registration or have any concerns, please disregard this email.

        Welcome to our community!

        Best regards,
        Parth Patel,Smit Parikh.
        '''.format(email)
    from_email = "parthpatelaa19@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

User = get_user_model()

def signup_gpt(request):
    if request.method == "POST":
        global email
        global password
        global confirmPassword
        email = request.POST.get('userName')
        password = request.POST.get('userPassword')
        confirmPassword = request.POST.get('ConfirmUserPassword')

        # Save the registration data to the database
        user = User.objects.create_user(username=email, password=password)
        user.is_active = False
        user.save()

        # Generate a confirmation token
        token = default_token_generator.make_token(user)

        # Construct the confirmation link
        confirmation_link = reverse('confirm_registration', args=[user.pk, token])
        confirm_url = request.build_absolute_uri(confirmation_link)

        # Send registration confirmation email
        send_registration_confirmation_email(email, confirm_url)

        messages.success(request, 'Registration successful! Please check your email for confirmation.')
        return redirect('registerpage')

    return render(request, 'register.html')

def send_registration_confirmation_email(email, confirm_url):
    subject = "Registration Confirmation"
    message = '''
        Dear {},

        Thank you for registering with our service. We are excited to have you on board!

        To complete the registration process, please click on the following link:

        {}

        If you did not initiate this registration or have any concerns, please disregard this email.

        Welcome to our community!

        Best regards,
        Parth Patel, Smit Parikh.
        '''.format(email, confirm_url)

    from_email = "parthpatelaa19@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def confirm_registration(request, user_id, token):
    user = User.objects.get(pk=user_id)
    if default_token_generator.check_token(user, token):
        # Update the user's registration status
        user.is_active = True
        user.save()

        print(email)
        register_data.username = email
        register_data.password = password
        register_data.confirmpassword = confirmPassword
        register_data.save()        

        messages.success(request, 'Registration confirmed! You can now log in.')
        return redirect('loginpage')

    messages.error(request, 'Invalid confirmation link.')
    return redirect('registerpage')


def LandingPage(request):
    return render(request,'portfolio_pages/index.html')

def ErrorPage(request):
    return render(request,'portfolio_pages/error_page.html')
