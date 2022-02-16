from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name':'Welcome to the future of programming'},
    {'id':2, 'name':'Another of the best tutorials'},
    {'id':3, 'name':'Never give up Mot'}
]

def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request):
    return render(request,'base/room.html')
