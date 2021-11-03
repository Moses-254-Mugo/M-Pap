from django.shortcuts import redirect, render
from .models import Room, Message
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists(): # if the room name that was inputed exits
        return redirect('/'+room+'/?username='+username) # Redirect to the room
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)