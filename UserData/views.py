#Author - Shivam Kapoor

#Importing Essentials
from __future__ import unicode_literals
from django.shortcuts import render
import requests , datetime, json, dateutil.parser
from datetime import date
from .models import *

#View to retrieve user data from GithubAPI.
def userdata_retrieval(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('user')

        #Giving request to GithubAPI and converting to JSON format.
        req = requests.get('https://api.github.com/users/'+username)
        content = req.json()
        retrievedList = []
        retrievedList.append(json.loads(req.content))
        content['created_at'] = dateutil.parser.parse(content['created_at'])

        #Adding data retrieved to Table - user_data.
        for entry in retrievedList:
            get_previous_entry=user_data.objects.filter(Idx=retrievedList[0]['id'])
            get_previous_entry.delete()
            data_into_table = user_data(Idx=retrievedList[0]['id'], User_name=str(retrievedList[0]['login']),Full_name=str(retrievedList[0]['name']),
                                        Location=str(retrievedList[0]['location']), Blog=str(retrievedList[0]['blog']), Public_repos=retrievedList[0]['public_repos'],
                                        Public_gists=retrievedList[0]['public_gists'], Email=str(retrievedList[0]['email']), Followers=retrievedList[0]['followers'],
                                        Following=retrievedList[0]['following'], Updated_on=date.today())
            data_into_table.save()

    return render(request, 'UserData/userdata.html', content)
