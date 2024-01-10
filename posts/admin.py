from django.contrib import admin
from .models import Profile
# Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     readonly_fields = ('date_of_birth',)

admin.site.register(Profile)