from django.shortcuts import render
from django.http import JsonResponse
import dash_core_components

import requests, json, sys
from .serializers import *

from .models import *

#TwitchAPI
twitch_client_id = ''
twitch_client_secret = ''


def get_twitch(request):

    #Get oath2 token from Twitch
    twitch_endpoint = 'https://id.twitch.tv/oauth2/token?'
    twitch_token_url = twitch_endpoint + 'client_id=' + twitch_client_id + '&client_secret=' + twitch_client_secret + '&grant_type=client_credentials'

    response = requests.post(twitch_token_url)
    twitch_token_return = response.json()

    #Token saved for get requests
    twitch_access_token = twitch_token_return['access_token']

    #Authorization Credentials for get requests
    headers = {"client-id": twitch_client_id, "authorization": 'Bearer ' + twitch_access_token}

    #Top Games on Twitch
    topgames_url = 'https://api.twitch.tv/helix/games/top'
    top_games_request = requests.get(topgames_url, headers=headers).json()

    #Get Games Analytics
    getgamesanalytics_url = 'https://api.twitch.tv/helix/games'
    getgames_request = requests.get(getgamesanalytics_url, headers=headers).json()



    #Data returning
    context = {"twitch_token_return": twitch_token_return, 'twitch_access_token': twitch_access_token, 'top_games_request': top_games_request, 'getgames_request':getgames_request}

    return render(request, 'gamesdata/main.html', context)
