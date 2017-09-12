from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Game, ScreenShot, ContactMessage, Profile

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _


admin.site.register(Game)
admin.site.register(ScreenShot)
admin.site.register(ContactMessage)


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class NewUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_queryset(self, request):
        qs = super(NewUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username)

    def change_view(self, request, object_id, form_url='', extra_context=None):
     	if not request.user.is_superuser:
			self.fieldsets = self.fieldsets[:2] + self.fieldsets[4:] # removing permissions and dates
        return super(NewUserAdmin, self).change_view(request, object_id, form_url, extra_context)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)