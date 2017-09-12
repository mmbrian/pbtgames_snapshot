from django.db import models

class Notification(models.Model):
	pub_date = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=False)
	published = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.content[:20] + '...' if self.content else 'Empty')