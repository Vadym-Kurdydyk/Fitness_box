from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


def loginPage(request):
    context = {}
    return render(request, r'base/login-register.html', context)

def room(request,pk):
    room = Room.objects.get(id = pk )
    
    context = {'room': room}
    return render(request, r'base/room.html', context)
def home(request):
    rooms = Room.objects.all()
    return render(request, r'base/home.html',{'rooms': rooms })

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        print(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    context = {"form": form}
    return render(request, r'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance= room)
    if form.is_valid():
        form.save()
        return redirect("home")
    
    context = {"form": form}
    return render(request, r'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {'obj':room}
    return render(request, r'base/delete.html', context)
