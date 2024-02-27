from django.shortcuts import render
from .models import Room

def room(request,pk):
    room = Room.objects.get(id = pk )
    
    context = {'room': room}
    return render(request, r'base/room.html', context)
def home(request):
    rooms = Room.objects.all()
    return render(request, r'base/home.html',{'rooms': rooms })
