from django.contrib import admin
from accounts.models import UserProfile, ErrorLogging
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ErrorLogging)
