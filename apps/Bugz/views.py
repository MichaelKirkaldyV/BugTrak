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

def register_admin_process(request):
    # Sets errors to dictionary in validation_user in models.py
    errors = User.objects.validate_admin_user(request.POST)

    # Checks to see if there are errors and passes them to the template.
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/register')

    else:
        # Creates a User and saves to database.
        name = request.POST['name']
        u_email = request.POST['u_email']
        username = request.POST['username']
        password = request.POST['password']

        # Makes the user created at Registry an admin using the hidden input field.
        is_admin = request.POST['is_admin']

        # Uses bcyrpt to hash and salt the password entered and saves the hashed password in the database for security. 
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print("HASH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", hashed_pw)
        newU = User.objects.create(name = name, u_email = u_email, username = username, password = hashed_pw.decode('utf-8'), is_admin = is_admin)
        print(newU)
        # Gets the user entered by its username previously entered and sets its session id to the id given on creation.
        user = User.objects.get(username = username)
        request.session['id'] = user.id
        return redirect('/login')

def login_process(request):
    username = request.POST['username']
    password = request.POST['password']

    # Checks if user is in the database
    user = User.objects.filter(username = username)

    if len(user) > 0:   
        # Checks to see if the password entered matches the password in the database.
        print("USERRRRRRRRR", user[0].password)
        this_password = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if this_password:
            request.session['id'] = user[0].id
            print("You are logged in")
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect username/password combination")
            return redirect('/login')
    else:
        messages.error(request, "User does not exist")
        return redirect('/login')

def logout(request):
    request.session.clear()
    return redirect('/login')

def dashboard(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
            # Get returns one value - while filter returns multiple values
            "user": User.objects.get(id = request.session['id'])
        }
        return render(request, "Bugz/dashboard.html", context)

def add_project(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        return render(request, "Bugz/add_project.html")

def project_report(request):
    return render(request, "Bugz/project_report.html")

def add_bug(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
            # Filter users who are staff!
            "users": User.objects.filter(is_staff = True),
            "projects": Project.objects.all()
        }
        return render(request, "Bugz/add_bug.html", context)

def bug_report(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
            "bugs": Bug.objects.all()
        }
    return render(request, "Bugz/bug_report.html", context)

def add_user(request):
    return render(request, "Bugz/add_user.html")

def user_report(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
            "users": User.objects.all()
        }
        return render(request, "Bugz/user_report.html", context)

def add_project_process(request):
    errors = Project.objects.validate_project(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/add_project')
    else:
        title = request.POST['title']
        typ = request.POST['typ']
        manager = request.POST['manager']
        backend = request.POST['backend']
        frontend = request.POST['frontend']
        client = request.POST['client']
        description = request.POST['description']

        project = Project.objects.create(title = title, typ = typ, manager = manager, backend = backend, frontend = frontend, client = client, description = description)
        print("PROJECT CREATED", project)
        return redirect('/dashboard')

def add_bug_process(request):
    errors = Bug.objects.validate_bug(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/add_bug')
    else:
        name = request.POST['name']
        typ = request.POST['typ']
        status = request.POST['status']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']
        description = request.POST['description']
        project = Project.objects.get(id = request.POST['project'])
        user = User.objects.get(id = request.POST['assigned_to'])
        bug = Bug.objects.create(name = name, typ = typ, status = status, start_date = start_date, due_date = due_date, description = description, assigned_to = user, project = project)       
        print("BUG CREATED", bug.name, bug.assigned_to)
        return redirect('/dashboard')

def add_user_process(request):
    errors = User.objects.validate_user(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/add_user')
    else:
        name = request.POST['name']
        u_email = request.POST['u_email']
        password = request.POST['password']
        mobile_no = request.POST['mobile_no']
        user = User.objects.create(name = name, u_email = u_email, password = password, mobile_no = mobile_no)
        print("USER CREATED", user)
        return redirect('/dashboard')

def edit_bug(request, id):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
           "bug": Bug.objects.get(id = id),
            # Filter users who are staff!
            "users": User.objects.all(),
            # Shows projects from db with dropdown in template.
            "projects": Project.objects.all()
        }
        return render(request, "Bugz/edit_bug.html", context)

def edit_user(request, id):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        context = {
           "user": User.objects.get(id = id)
        }
        return render(request, "Bugz/edit_user.html", context)
    

def delete_bug(request, id):
    bug = Bug.objects.get(id = id)
    bug.delete()
    return redirect('/bug_report')

def delete_user(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/user_report')

def delete_project(request, id):
    project = Project.objects.get(id = id)
    project.delete()
    return redirect('/project_report')

def update_project_process(request, id):
    errors = Project.objects.validate_project(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/add_project')
    else:
        title = request.POST['title']
        typ = request.POST['typ']
        manager = request.POST['manager']
        backend = request.POST['backend']
        frontend = request.POST['frontend']
        client = request.POST['client']
        description = request.POST['description']

        Project.objects.filter(id = id).update(title = title, typ = typ, manager = manager, backend = backend, frontend = frontend, client = client, description = description)
        return redirect('/project_report')

def update_user_process(request, id):
    errors = User.objects.validate_user(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/edit_user/' + id)
    else:
        name = request.POST['name']
        u_email = request.POST['u_email']
        password = request.POST['password']
        mobile_no = request.POST['mobile_no']

        User.objects.filter(id = id).update(name = name, u_email = u_email, password = password, mobile_no = mobile_no)
        return redirect('/user_report')

def update_bug_process(request, id):
    errors = Bug.objects.validate_bug(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/edit_bug/' + id)
    else:
        name = request.POST['name']
        typ = request.POST['typ']
        status = request.POST['status']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']
        description = request.POST['description']
        project = Project.objects.get(id = request.POST['project'])
        user = User.objects.get(id = request.POST['assigned_to'])

        Bug.objects.filter(id = id).update(name = name, typ = typ, status = status, start_date = start_date, due_date = due_date, description = description, assigned_to = user, project = project)
        return redirect('/bug_report')