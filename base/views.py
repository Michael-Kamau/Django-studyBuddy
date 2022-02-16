from django.shortcuts import render
from django.http import HttpResponse
 
from .models import Room


# rooms = [
#     {'id':1, 'name':'Welcome to the future of programming'},
#     {'id':2, 'name':'Another of the best tutorials'},
#     {'id':3, 'name':'Never give up Mot'}
# ]

def home(request):

    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}
    return render(request,'base/room.html', context)
