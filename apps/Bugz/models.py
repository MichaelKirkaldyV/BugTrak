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

class Query(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	company = models.CharField(max_length=30)
	message = models.CharField(max_length=150)
	objects = QueryManager()