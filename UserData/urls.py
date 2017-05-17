#Author - Shivam Kapoor

#Importing Essentials
from django.conf.urls import url
from UserData import views

#Forming URLs
urlpatterns = [
    url(r'^$', views.userdata_retrieval, name='userdata'),
]
