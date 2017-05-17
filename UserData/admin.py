#Author - Shivam Kapoor

#Importing Essentials
from __future__ import unicode_literals
from django.contrib import admin
import datetime
from datetime import date
from .models import user_data


#Creating Admin Table Layout.
class User_dataAdmin(admin.ModelAdmin):
    list_display = ['Thumbnail', 'Idx','User_name', 'Full_name', 'Location', 'Blog', 'Public_repos', 'Public_gists', 'Email', 'Followers', 'Following', 'Updated_on']
    search_fields = ['Idx','User_name', 'Full_name', 'Location', 'Blog', 'Public_repos', 'Public_gists', 'Email', 'Followers', 'Following', 'Updated_on']

    class Meta:
        model = user_data

#Registering Tables for admin page.
admin.site.register(user_data, User_dataAdmin)
