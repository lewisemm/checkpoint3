from django.shortcuts import render


def index(request):
	"""Render the index html page"""
	return render(request, 'index.html')
