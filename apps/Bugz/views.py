from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def homepage(request):
    return render(request, "Bugz/homepage.html")

def contact(request):
    return render(request, "Bugz/contact.html")

def about(request):
    return render(request, "Bugz/about.html")

def login(request):
    return render(request, "Bugz/login.html")

def process_inquery(request):
    # Sets errors to dictionary in validation_query in models.py.
    errors = Query.objects.validate_query(request.POST)

    # Checks to see if there are errors and passes them to the template.
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/contact')

    # Creates Query and saves to database.
    else:
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        message = request.POST['message']
        query = Query.objects.create(name = name, email = email, company = company, message = message)
        print("Query Created", query)
        print("Name", name)
        print("Email", email)
        print("Company", company)
        print("Message", message)
        messages.success(request, "Thank you! We will be in touch.")
        return redirect('/contact')

def register(request):
    return render(request, "Bugz/register.html")

def register_process(request):
    # Sets errors to dictionary in validation_user in models.py
    errors = User.objects.validate_user(request.POST)

    # Checks to see if there are errors and passes them to the template.
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/contact')

    else:
        # Creates a User and saves to database.
        u_email = request.POST['u_email']
        username = request.POST['username']
        password = request.POST['password']

        # Uses bcyrpt to hash and salt the password entered and saves the hashed password in the database for security. 
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(u_email = u_email, username = username, password = hashed_pw)

        # Gets the user entered by its username previously entered and sets its session id to the id given on creation.
        user = User.objects.get(username = username)
        request.session['id'] = user.id
        return redirect('/login')

