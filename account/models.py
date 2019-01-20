from django.db import models

class UserFile(models.Model):
	name = models.CharField(max_length = 50)
	first_name = models.CharField(max_length = 50)
	password = models.CharField(max_length=50)
	email_address = models.EmailField(max_length= 100)

	class Meta:
		verbose_name="userfile"
		ordering = ['name']

	def __str__(self):
		return self.name

# Create your models here.
