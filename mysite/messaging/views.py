from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Message

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        #messagez = Message.objects.all()
        context = {'messages': "hey"}
        return render(request, 'site/index.html', context)