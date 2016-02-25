from django.shortcuts import render


def index(request):
	"""Serve the app's index page."""
	return render(request, 'views/index.html')
