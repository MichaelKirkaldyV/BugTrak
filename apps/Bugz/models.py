from django.db import models

class QueryManager(models.Manager):
	def validate_query(request, postData):
		errors = {}

		if len(postData['name']) < 3:
			errors['name'] = "Name must be longer than 3 characters"

		if len(postData['email']) < 3:
			errors['email'] = "Email must be longer than 3 characters"

		if len(postData['company']) < 4:
			errors['company'] = "Company must be longer than 4 characters"

		if len(postData['message']) < 10:
			errors['message'] = "Message must be longer than 10 characters"

		return errors

class UserManager(models.Manager):
	def validate_user(request, postData):
		errors = {}

		if len(postData['u_email']) < 3:
			errors['u_email'] = "Email must be longer than 3 characters"

		if len(postData['username']) < 4:
			errors['username'] = "Username must be longer than 4 characters"

		if len(postData['password']) < 8:
			errors['password'] = "Password must be at longer than 7 characters"

		if postData['password'] != postData['cnfrm_password']:
			errors['cnfrm_password'] = "Passwords do not match"
		
		return errors

class ProjectManager(models.Manager):
	def validate_project(request, postData):
		errors = {}

		if len(postData['title']) < 4:
			errors['title'] = "Title must be longer than 4 characters"

		if postData['typ'] == None:
			errors['type'] = "Please select a type"

		if postData['manager'] == None:
			errors['manager'] = "Please select a manager"

		if len(postData['frontend']) < 3:
			errors['frontend'] = "Frontend name must be longer than 4 characters"

		if len(postData['backend']) < 3:
			errors['backend'] = "Backend name must be longer than 4 characters"

		if len(postData['client']) < 3:
			errors['client'] = "Client name must be longer than 4 characters"

		if len(postData['description']) < 8:
			errors['description'] = "Description must be longer than 8 characters"

		return errors

class BugManager(models.Manager):
	def validate_bug(request, postData):
		errors = {}

		if len(postData['title']) < 4:
			errors['title'] = "Title must be longer than 4 characters"

		if postData['project'] == None:
			errors['project'] = "Please select a project"

		if postData['typ'] == None:
			errors['type'] = "Please select a type"

		if postData['assigned_to'] == None:
			errors['assigned_to'] = "Please select an assignment"
		
		if postData['status'] == None:
			errors['status'] = "Please select the status of the bug"

		if len(postData['start_date']) < 4:
			errors['start_date'] = "Start date must be longer than 4 characters"
		elif len(postData['start_date']) == None:
			errors['start_date'] = "Please enter a start date"

		if len(postData['due_date']) < 4:
			errors['due_date'] = "Due date must be longer than 4 characters"
		elif len(postData['due_date']) == None:
			errors['due_date'] = "Please enter a due date"

		if len(postData['description']) < 8:
			errors['description'] = "Description must be longer than 8 characters"

		return errors


class Query(models.Model):
	name = models.CharField(max_length=20)
	company = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	message = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Inherits the Query Manager
	objects = QueryManager()

class User(models.Model):
	name = models.CharField(max_length=20)
	u_email = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	mobile_no = models.IntegerField(null=True)
	password = models.CharField(max_length=20)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Inherits the User Manager
	objects = UserManager()

class Project(models.Model):
	title = models.CharField(max_length=20)
	typ = models.CharField(max_length=20)
	manager = models.CharField(max_length=15)
	frontend = models.CharField(max_length=10)
	backend = models.CharField(max_length=10)
	client = models.CharField(max_length=15)
	description = models.CharField(max_length=120)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ProjectManager()

class Bug(models.Model):
	name = models.CharField(max_length=20)
	typ = models.CharField(max_length=20)
	status = models.CharField(max_length=20)
	start_date = models.CharField(max_length=20)
	due_date = models.CharField(max_length=20)
	description = models.CharField(max_length=120)
	# Dynamic dropdown menu to choose which user a bug is assigned too
	assigned_to = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Dynamic dropdown menu to choose which project it belongs too.
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	objects = BugManager()

