import json, random, re
from pprint import pprint
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#Access token
PAGE_ACCES_TOKEN =''
VERIFY_TOKEN = '961966336'
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
        return HttpResponse()
