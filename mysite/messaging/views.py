from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Message, PrivateMessage

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        
        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/indextest.html', context) #FIX THE FILE
    if request.method == 'POST':
        mymessage = request.POST.get('mymessage')
        the_user = User.objects.get(username=request.user)
        print(the_user.id)

        query = f"INSERT INTO messaging_message (user_id,text) VALUES ({the_user.id}," + f"'{mymessage}');"
        #Test injection
        #'); INSERT INTO messaging_message (user_id,text) VALUES (1,"This was not me!"); --
        #'); DELETE FROM messaging_message WHERE user_id = 3 --


        #JUST USE THIS ONE BELOW. Yes I included the fixed SQL also, but I would prefer this anyway.
        #Message.objects.create(user=request.user, text=mymessage)
        
        with connection.cursor() as cursor:
            cursor.executescript(query)

            #Should be just with sql
            #cursor.execute("INSERT INTO messaging_message (user_id,text) VALUES (?,?)",(the_user.id, mymessage))
            #cursor.commit()

        

        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/indextest.html', context) #FIX THE FILE



def private(request,pk):
    try:
        userr = User.objects.get(id=pk)
    except:  return redirect('index')
    
    #if userr == request.user:
    private_messages = PrivateMessage.objects.all().filter(receiver=userr.username)
    
    
    context = {'messages': private_messages,
            'pk': pk}

    return render(request, 'site/privatechatsfixed.html', context)

    #else: return redirect('index')

"""
def send(request,pk):
    
    #User that you can get from pk
    userr = User.objects.get(id=pk)

    #The actual user you are logged in as
    the_user = request.user
    print(the_user)

    if userr == the_user:
        a = request.session['text'] = request.GET.get('text')
        b = request.session['name'] = request.GET.get('name')
        print(a,b)
        PrivateMessage.objects.create(user=the_user, receiver=b, text=a)
        return redirect('private', pk=pk)
    else:
        return redirect('index')
"""

def send(request,pk):
    if request.method == 'GET':
        return redirect('index')

    if request.method == 'POST':
        #User that you can get from pk
        userr = User.objects.get(id=pk)

        #The actual user you are logged in as
        the_user = request.user


        if userr == the_user:
            a = request.session['text'] = request.POST.get('text')
            b = request.session['name'] = request.POST.get('name')
            print(a,b)
            PrivateMessage.objects.create(user=the_user, receiver=b, text=a)
            return redirect('private', pk=pk)
        else:
            return redirect('index')


    