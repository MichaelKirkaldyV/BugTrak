from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def homepage(request):
    return render(request, "Bugz/homepage.html")

def contact(request):
    return render(request, "Bugz/contact.html")

def about(request):
    return render(request, "Bugz/about.html")

def login(request):
    return render(request, "Bugz/login.html")

def process_inquery(request):
    # Sets errors to dictionary in validation query.
    errors = Query.objects.validate_query(request.POST)
    print(errors)

    # Checks to see if there are errors.
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/contact')

    # Creates Query.
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
