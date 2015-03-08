from django.shortcuts import render


def home(request):
	args = {}
	return render(request, 'events/home.html', args)