# Importing necessary modules and functions from Django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# A Django view that is only accessible to logged-in users, due to the @login_required decorator
# It simply renders the 'homepage.html' template


@login_required
def homepage(request):
    return render(request=request, template_name="homepage.html")

# A Django view that renders the 'coverpage.html' template


def coverpage(request):
    return render(request=request, template_name="coverpage.html")

# A Django view that handles user registration
# It receives POST parameters (username, password, email, etc.), validates them,
# creates a new User object if everything is correct, and then redirects the user to the sign in page


def Register(request):
    user_name = request.POST.get("uname")
    password = request.POST.get("pass1")
    re_password = request.POST.get("pass2")
    email = request.POST.get("email")
    # Note: This variable isn't actually used anywhere
    phone_no = request.POST.get("phone number")

    # Check if the username already exists
    if User.objects.filter(username=user_name).exists():
        messages.error(request=request, message="User name already taken")
        return redirect("register")

    # Check if the password matches the repeated password
    if password != re_password:
        messages.error(request=request,
                       message="Password doesn't Match \n please Try again !")

    # Check if the request is a POST request
    # If it is, then create a new User object and save it
    if request.method == "POST":
        user = User.objects.create_user(
            username=user_name, email=email, password=password)
        user.save()
        return redirect("signin")

    # If the request is not a POST request, then render the registration form
    return render(request=request, template_name="register.html")

# A Django view that handles user login
# It receives POST parameters (username and password), authenticates the user,
# and if successful, logs them in and redirects them to the homepage


def Signin(request):
    user_name = request.POST.get("uname")
    password = request.POST.get("pass")

    user = authenticate(request=request, username=user_name, password=password)

    # Check if the request is a POST request
    # If it is, then authenticate the user and log them in
    if request.method == "POST":
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request=request,
                           message="please Register Yourself !")

    # If the request is not a POST request, then render the login form
    return render(request=request, template_name="signin.html")

# A Django view that handles user logout
# It logs the user out and then redirects them to the sign in page


def signout(request):
    logout(request=request)
    return redirect("signin")
