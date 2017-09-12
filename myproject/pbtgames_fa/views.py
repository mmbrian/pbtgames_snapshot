from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token 
from .models import Game, ContactMessage
from django.contrib.auth.models import User

import random

from myproject.settings import STATIC_ROOT
import os
from search import search

def index(request):
	localized = True
	en = '/en/' in request.path
	published_premiered = []
	if en:
		published_premiered = Game.objects.filter(published = True, is_premiered=True, allowed_on_en=True).order_by('-addition_date')
	else:
		published_premiered = Game.objects.filter(published = True, is_premiered=True).order_by('-addition_date')
	premiered_game = None
	if published_premiered:
		premiered_game = published_premiered[0]
	if premiered_game:
		# Display game on main page
		if en:
			title = premiered_game.premier_title_en
			desc = premiered_game.premier_description_en
		else:
			title = premiered_game.premier_title
			desc = premiered_game.premier_description
		cover = premiered_game.premier_image.url
		preloader = premiered_game.preloader.url
		game_slug = premiered_game.slug
		return render_to_response('pbtgames_fa/main_page_with_full_scr_bg.html', locals())
	else:
		# Display an appropriate bg and text on main page, not premiering anything
		# TODO: load defaults from dynamic constants (use constance)
		return render_to_response('pbtgames_fa/main_page_with_full_scr_bg.html', locals())

def view_game(request, game_id):
	localized = True
	social = True
	en = '/en/' in request.path
	games = []
	if en:
		games = Game.objects.filter(published = True, id = game_id, allowed_on_en = True)
		recent_games = Game.objects.filter(published = True, allowed_on_en = True).exclude(id = game_id).order_by("addition_date")[:4]
	else:
		games = Game.objects.filter(published = True, id = game_id)
		recent_games = Game.objects.filter(published = True).exclude(id = game_id).order_by("addition_date")[:4]
	games_selected = True
	if games:
		game = games[0]
		preloader = game.preloader.url

		force_hide_sibche = request.session['hide_sibche'] if 'hide_sibche' in request.session else False
		if game.portrait_only:
			return render_to_response('pbtgames_fa/game_page_portrait.html', locals())
		else:
			return render_to_response('pbtgames_fa/game_page.html', locals())
	else:
		raise Http404

# def list_games(request, page): 
def list_games(request): #=> no pagination for now
	localized = True
	en = '/en/' in request.path
	games = []
	force_hide_sibche = request.session['hide_sibche'] if 'hide_sibche' in request.session else False
	if en:
		games = Game.objects.filter(published = True, allowed_on_en = True).order_by("addition_date")
	else:	
		games = Game.objects.filter(published = True).order_by("addition_date")
	games_selected = True
	return render_to_response('pbtgames_fa/list_games_page.html', locals())

@csrf_exempt
@requires_csrf_token 
def contact_us(request):
	contact_selected = True
	localized = True
	post_submit = False
	en = '/en/' in request.path
	if request.method.lower() == "post":
		captcha = request.POST['captcha']
		if captcha == str(request.session['captcha_result']):
			name = request.POST['fullname']
			email = request.POST['email']
			message = request.POST['message']
			subscribe = 'newsletter' in request.POST
			try:
				cmessage = ContactMessage(sender = name, email = email, body = message, subscribed = subscribe)
				cmessage.save()
				submit = True
				del request.session['captcha_result']
			except:
				submit = False
			post_submit = True
			# TODO: notify an admin about this new message
		else:
			wrong_captcha = True # use this inside template to display an error or sth
	
	op = random.choice([' + ', ' - '])
	math_expression = str(random.randint(0, 1000)) + op + str(random.randint(0, 1000))
	request.session['captcha_result'] = eval(math_expression)
	math_expression += " = ?"
	return render_to_response('contactus.html', locals(), context_instance = RequestContext(request))

def about_us(request):
	about_selected = True
	localized = True
	en = '/en/' in request.path
	users = User.objects.all()
	# return render(request, 'aboutus.html')
	return render_to_response('aboutus.html', locals())

def dev_tools(request):
	return render(request, 'dev_tools.html')

def mohsen_fireworks(request):
	return render(request, 'fireworks.html')

def mohsen_stars(request):
	return render(request, 'stars.html')

def mohsen_polygonal(request):
	return render(request, 'polygonal.html')

def mohsen_postprocessing_1(request):
	return render(request, 'postprocessing.html')	

def mohsen_pdf_search(request):
	contact_selected = True
	localized = True
	post_submit = False
	en = False

	final_results = []
	if request.method.lower() == "post":
		query = request.POST['message']
		post_submit = True

		containing_pdfs = []
		containing_paragraphs = []
		# perform search
		for pdf_file in os.listdir(os.path.join(STATIC_ROOT, 'pdf_data')):
			if pdf_file.endswith('.txt'): # content file
				froot = os.path.join(STATIC_ROOT, 'pdf_data', pdf_file)
				ret = search(froot, query)
				for result in ret:
					containing_pdfs.append(pdf_file)
					containing_paragraphs.append(unicode(result))
		final_results = zip(containing_pdfs, containing_paragraphs)

	math_expression = ''	
	return render_to_response('pdfsearch.html', locals(), context_instance = RequestContext(request))

def test(request):
	en = '/en/' in request.path
	return HttpResponse('English: ' + str(en))
	# return HttpResponse(get_client_ip(request))