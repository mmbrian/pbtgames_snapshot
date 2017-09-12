from django.http import HttpResponseRedirect
import pygeoip

from myproject.pbtgames_fa.models import Game

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
    	ips = x_forwarded_for.split(',') 
    	if len(ips) > 1:
        	ip = ips[1]
        else:
        	ip = ips[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip.lstrip()

class LanguageRedirectMiddleware:

	gi = None
	def initGeoDB(self):
		self.gi = pygeoip.GeoIP('/home/mmbrian/webapps/pbtgames_static/other/GeoIP.dat')

	def process_request(self, request):
		admin_request = request.path.startswith('/admin')
		notif_request = request.path.startswith('/notification')
		fa_request = request.path.startswith('/fa')
		en_request = request.path.startswith('/en')
		robots = request.path.startswith('/robots.txt')
		if not (admin_request or notif_request or fa_request or en_request or robots):
			redirect_to = request.path

			if request.path.count('/') < 2: # e.g. /barfak
				# check if this url is short url for a game
				games = Game.objects.filter(published = True)
				for game in games:
					if request.path.startswith('/' + game.slug):
						redirect_to = '/game/' + str(game.id)
						break

			if not self.gi:
				self.initGeoDB()
			my_ip = get_client_ip(request)
			if self.gi.country_code_by_addr(my_ip) == 'IR':
				# redirect to the fa page
				redirect_to = '/fa' + redirect_to
			else:
				# redirect to the en page
				redirect_to = '/en' + redirect_to
			return HttpResponseRedirect(redirect_to)
		if fa_request or en_request:
			stripped = request.path.replace('/en/', '').replace('/fa/', '')
			if len(stripped) > 3: # assuming a game name is longer than 3 characters
				game_name = stripped.rstrip("/")
				if not '/' in game_name and not game_name in ['about', 'contact', 'tools']: # e.g. /en/barfak/, /en/barfak
					en = '/en/' in request.path
					lang_code = 'en' if en else 'fa'
					# check if this url is short url for a game
					if en:
						games = Game.objects.filter(published = True, allowed_on_en = True)
					else:
						games = Game.objects.filter(published = True)
					for game in games:
						if request.path.startswith('/' + lang_code + '/' + game.slug):
							redirect_to = '/' + lang_code + '/game/' + str(game.id)
							break
					return HttpResponseRedirect(redirect_to)
		if fa_request:
			if not self.gi:
				self.initGeoDB()
			my_ip = get_client_ip(request)
			if self.gi.country_code_by_addr(my_ip) != 'IR':
				# fa request from outside of Iran >> sibche must be hidden!
				request.session['hide_sibche'] = True
			else:
				request.session['hide_sibche'] = False