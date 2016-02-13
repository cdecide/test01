from django.db import models

# Create your models here.

class Post(models.Model):
	"""docstring for Post"models.Modelf __init__(self, arg):
		super(Post,models.Model.__init__()
		self.arg = arg"""
	username = models.CharField(max_length=40)
	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{date} 만들어진 {number} 번 글'.format(date=self.create_at, number=self.pk)