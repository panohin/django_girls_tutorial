from django.shortcuts import render
from django.http import HttpResponse

from . import models


def post_list(request):
	context = models.Post.objects.all()
	return render(request, 'blog/post_list.html', context={})
