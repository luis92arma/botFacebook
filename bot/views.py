import json, random, re, requests
from pprint import pprint
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#Access token
PAGE_ACCESS_TOKEN ='EAAE24wJsJdUBAAzJCzFZCXQXmofSPLDIOFTBbIghUdRhqsDBfV8ZBLXY5vI3VhipXiLjV6HHxbwfV7cwlU0hmN7GLBL0vPkToZAxZBbKajEaJIvowi9VyZBolFrygH8tZC9cqAXl9DhMzwTUbW9TOjGLewsAaJiKuYa34iQa3BngZDZD'
VERIFY_TOKEN = '961966336'
def post_facebook_messages(fbid, recived_message):
    #Cuando se manda llamar envia el mismo texto que se recibe
    post_messages_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({'recipient':{'id':fbid}, 'message':{'text':recived_message}})
    status = requests.post(post_messages_url, headers={'Content-Type':'application/json'},data=response_msg)
    pprint(status.json())

class BotMessenger(View):
    """docstring forBotMessenger"""
    def get(self, request):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        return generic.View.dispatch(self, request)

    def post(self, request):
        #Convierte el texto dentro de un diccionario
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    pprint(message)
                    post_facebook_messages(message['sender']['id'], message['message']['text'])
        return HttpResponse()
