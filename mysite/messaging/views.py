from django.shortcuts import render
from django.db import connection

from django.contrib.auth.models import User
from .models import Message

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        
        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/index.html', context)
    if request.method == 'POST':
        mymessage = request.POST.get('mymessage')
        a_user = User.objects.get(username=request.user)
        print(a_user.id)

        query = f"INSERT INTO messaging_message (user_id,text) VALUES ({a_user.id}," + f"'{mymessage}');"
        
        with connection.cursor() as cursor:
            cursor.executescript(query)
            #Should be just cursor.execute!

        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/index.html', context)