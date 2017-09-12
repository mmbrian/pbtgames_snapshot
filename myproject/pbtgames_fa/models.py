from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Game(models.Model):
	addition_date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=144, blank=False)
	name_en = models.CharField(max_length=144, blank=True)
	slug = models.CharField(max_length=144, blank=False)
	release_date = models.DateTimeField()
	overview = models.TextField(blank=False)
	overview_en = models.TextField(blank=True)

	# Only published games will appear on the website
	published = models.BooleanField(default=False) 
	allowed_on_en = models.BooleanField(default=True) # not every game is international
	portrait_only = models.BooleanField(default=False) # this changes page layout if screenshots
													   # are portrait. if game also has 
													   # landscape mode you have to only upload
													   # screenshots in landscape and leave this 
													   # property to False
	is_premiered = models.BooleanField(default=True)
	premier_title = models.TextField(blank=True)
	premier_title_en = models.TextField(blank=True)
	premier_description = models.TextField(blank=True)
	premier_description_en = models.TextField(blank=True)
	premier_image = models.ImageField(upload_to='premier_images/', blank=True)

	preloader = ProcessedImageField(upload_to='preloaders/',
								processors=[ResizeToFill(64, 64)],
								format='PNG',
								null=True)

	# Screenshots have to be added independently
	icon = models.ImageField(upload_to='icons/')

	googleplay_link = models.CharField(max_length=300, blank=True)
	appstore_link = models.CharField(max_length=300, blank=True)
	bazaar_link = models.CharField(max_length=300, blank=True)
	sibche_link = models.CharField(max_length=300, blank=True)
	windows_link = models.CharField(max_length=300, blank=True)
	mac_link = models.CharField(max_length=300, blank=True)
	linux_link = models.CharField(max_length=300, blank=True)

	facebook_like_embedded_link = models.TextField(blank=True)
	googleplus_embedded_link = models.TextField(blank=True)

	def __unicode__(self):
		return unicode(self.name)


class ScreenShot(models.Model):
	title = models.CharField(max_length=144, blank=True)
	title_en = models.CharField(max_length=144, blank=True)
	overview = models.TextField(blank=True)
	overview_en = models.TextField(blank=True)
	image = models.ImageField(upload_to='screenshots/')
	game = models.ForeignKey(Game, related_name="screenshots")

	def __unicode__(self):
		return unicode(self.title + " - " + self.game.name)

class ContactMessage(models.Model):
	sender = models.CharField(max_length=144, blank=False)
	email = models.CharField(max_length=144, blank=False)
	body = models.TextField(blank=True)
	subscribed = models.BooleanField(default=True)

	def __unicode__(self):
		return unicode(self.body[:33] + ("..." if len(self.body) > 32 else ""))

class Profile(models.Model):
	'''
	A model to store extra info for each user
	'''
	user = models.OneToOneField(User, related_name='profile')
	name_fa = models.CharField(max_length=144, blank=False)

	title = models.CharField(max_length=144, blank=False)
	title_fa = models.CharField(max_length=144, blank=False)
	desc = models.TextField(blank=False)
	desc_fa = models.TextField(blank=False)
	photo = models.ImageField(upload_to='profile_photos/', blank=False)

	def __unicode__(self):
		return unicode(self.user.username)





