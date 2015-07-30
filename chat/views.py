from socketio import socketio_manage
from chat.sockets import ChatNamespace
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
def index(request):
	return render(request,'index.html')