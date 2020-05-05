from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import socket
from django.shortcuts import Http404
from django.views.generic import TemplateView

# Create your views here.
@login_required
def home(request):
    return render(request,'remote.html')


@login_required
def client(request):
    global OUTPUT
    host_name = "MY WEB HOST IP"
    port = 5000
    c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c_socket.connect((host_name,port))
    completede = print('Access Success\n---------------------------\n')

    if request.method == 'POST':

        msg = request.POST.get('message')
        while msg != 'q' and bool(msg) != False:
            c_socket.send(msg.encode())
            recv_data = c_socket.recv(1024).decode()
            OUTPUT = recv_data

    return render(request,'remote.html',{'OUTPUT':OUTPUT,'completede':completede})



def Logout(request):
    logout(request)
    return Http404