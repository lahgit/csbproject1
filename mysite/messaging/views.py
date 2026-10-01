from django.shortcuts import render, redirect
from django.db import connection

from django.contrib.auth.models import User
from .models import Message, PrivateMessage

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        
        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/index.html', context)
    if request.method == 'POST':
        mymessage = request.POST.get('mymessage')
        the_user = User.objects.get(username=request.user)
        print(the_user.id)

        query = f"INSERT INTO messaging_message (user_id,text) VALUES ({the_user.id}," + f"'{mymessage}');"


        #JUST USE THIS ONE BELOW. Yes I included the fixed SQL also, but I would prefer this anyway.
        #Message.objects.create(user=request.user, text=mymessage)
        
        with connection.cursor() as cursor:
            cursor.executescript(query)

            #Should be just with sql
            #cursor.execute("INSERT INTO messaging_message (user_id,text) VALUES (?,?)",(the_user.id, mymessage))
            #cursor.commit()

        

        messagez = Message.objects.all()
        context = {'messages': messagez}
        return render(request, 'site/index.html', context)


#    context = {'usrr': userr}
#
#    if request.method == 'GET':
#        if request.user == userr:
#            return render(request, 'site/settings.html', context)
#        else:
#             return redirect('/messaging')


#    if request.method == 'POST':
#
#        if request.user == userr:
#        
#            fontsize = request.POST.get('fontsize')
#            try:
#                Fontsize.objects.create(user = userr.id, size = fontsize)
#            except:
#                a = Fontsize.objects.get(user = userr.id)
#                a.size = fontsize
#                a.save()
#
#            return render(request, 'site/settings.html', context)
#        
#        else: return redirect('/messaging')


def private(request,pk):
    private_messages = PrivateMessage.objects.all()
    context = {'messages': private_messages}
    
    userr = User.objects.get(id=pk)

    return render(request, 'site/privatechats.html', context)


def send(request,pk):
    a = request.session['text'] = request.GET.get('text')
    b = request.session['name'] = request.GET.get('name')
    print(a,b)
    return redirect('private', pk=pk)


    