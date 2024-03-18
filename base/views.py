from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
             user = User.objects.get(username = username)
            
        except:
                messages.error(request, "Invalid username or password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
        
    context = {"page": page}
    return render(request, r'base/login-register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.user == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(comit = False)
            user.username = user.username.lower()
            login(request, user)
            return redirect('home')
        else:
            messages.error("An error occured during registration")
    context = {'form':form}
    return render(request, 'base/login-register.html',context)

def room(request,pk):
    room = Room.objects.get(id = pk )
    
    context = {'room': room}
    return render(request, r'base/room.html', context)
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.all()
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        
        )
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics':topics,'room_count':room_count }
    return render(request, r'base/home.html',context)

@login_required(login_url = 'login-register')
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

@login_required(login_url = 'login-register')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    if request.user != room.host:
        return HttpResponse("Access restricted")

    if request.method == "POST":
        form = RoomForm(request.POST, instance= room)
    if form.is_valid():
        form.save()
        return redirect("home")
    
    context = {"form": form}
    return render(request, r'base/room_form.html', context)

@login_required(login_url = 'login-register')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("Access restricted")
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {'obj':room}
    return render(request, r'base/delete.html', context)
