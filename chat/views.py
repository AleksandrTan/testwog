from django.shortcuts import render
from django.views.generic.base import TemplateView


class VideoStream(TemplateView):
    template_name = 'chat/index.html'


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })