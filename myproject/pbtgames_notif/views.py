from django.http import HttpResponse
from .models import Notification

from datetime import datetime

# Returns all notifications after a given time (no pagination)
# Return format is yyyy-MM-dd HH:mm:ss,<notification_content_1>,<notification_content_2>,...
# Where the initial date and content correspond to the last update
def get_notifs_after(request, timestamp):
	# timestamp is in this format: yyyy-MM-dd HH:mm:ss
	format = '%Y-%m-%d %H:%M:%S'
	date = datetime.strptime(timestamp, format) # https://docs.python.org/2/library/datetime.html
	notifs = Notification.objects.filter(published = True).filter(pub_date__gt = date).order_by('-pub_date')
	if notifs:
		latest_update = notifs[0].pub_date
		ret = latest_update.strftime(format) + ','
		for notif in notifs: ret += notif.content + ','
		ret = ret[:-1] # remove final comma
		return HttpResponse(ret)
	else:
		return HttpResponse("")


def get_all_notifs(request, page):
	pass