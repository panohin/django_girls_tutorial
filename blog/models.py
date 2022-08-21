from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		ordering = ['-created_date']

# class Author:
# 	name = models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.name