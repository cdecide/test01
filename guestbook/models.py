from django.db import models

# Create your models here.

class Post(models.Model):
	"""docstring for Post"models.Modelf __init__(self, arg):
		super(Post,models.Model.__init__()
		self.arg = arg"""
	username = models.CharField(max_length=40)
	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
