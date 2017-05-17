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

#Proxy Table 1.
class ReportToday(user_data):
    class Meta:
        proxy = True

#Filter query for present day.
class Query_Today(User_dataAdmin):
    def get_queryset(self, requests):
        return self.model.objects.filter(Updated_on = datetime.date.today())

#Proxy Table 2.
class ReportYear(user_data):
    class Meta:
        proxy = True

#Filter query for year.
class Query_Year(User_dataAdmin):
    Updated = datetime.date.today()
    def get_queryset(self, requests):
        return self.model.objects.filter(Updated_on__year__lte= datetime.datetime.today().year)

#Proxy Table 3.
class ReportMonth(user_data):
    class Meta:
        proxy = True

#Filter query for month.
class Query_Month(User_dataAdmin):
    def get_queryset(self, requests):
        return self.model.objects.filter(Updated_on__month__lte= datetime.datetime.today().month).exclude(Updated_on__month__lt= ((datetime.datetime.today().month)- 1))


#Registering Tables for admin page.
admin.site.register(user_data, User_dataAdmin)
admin.site.register(ReportToday, Query_Today)
admin.site.register(ReportYear, Query_Year)
admin.site.register(ReportMonth, Query_Month)
