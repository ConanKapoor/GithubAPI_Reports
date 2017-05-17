#Author - Shivam Kapoor

#Importing Essentials
from __future__ import unicode_literals
from django.shortcuts import render
import requests, json, dateutil.parser
from .models import *

#View to retrieve user data from GithubAPI.
def userdata_retrieval(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('user')

        #Giving request to GithubAPI and converting to JSON format.
        req = requests.get('https://api.github.com/users/'+username)
        content = req.json()
        content['created_at'] = dateutil.parser.parse(content['created_at'])

    return render(request, 'UserData/userdata.html', content)
