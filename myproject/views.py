from django.http import HttpResponse
from django.shortcuts import render

def custom_page_not_found_view(request):
	en = '/en/' in request.path
	return render(request, '404.html')

def custom_error_view(request):
	en = '/en/' in request.path
	return render(request, '500.html')

def custom_permission_denied_view(request):
	en = '/en/' in request.path
	return render(request, '403.html')

def custom_bad_request_view(request):
	en = '/en/' in request.path
	return render(request, '400.html')


def robots(request):
	return HttpResponse("""
		User-Agent: *
		Disallow: 
		Allow: /contact
		Allow: /about
		Allow: /games/list
		Disallow: /admin
		Allow: /barfak
		Allow: /game
		"""
		)