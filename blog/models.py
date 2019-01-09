from django.db import models

# Create A Blog model
# title
# pub date
# Text body
# image

class Blog(models.Model):
	title=models.CharField(max_length=300)
	pub_date=models.DateTimeField()
	body=models.TextField()
	image = models.ImageField(upload_to='images/')

# Add Blog app to settings 
# python manage.py makemigrations if ok
# python manage.py migrate

# Create a migrate

# Migrate

# Add to the admin
