from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat

def home(request):
    data = Chat.objects.raw('SELECT c.id id, c.message message, u.username username FROM chat_chat c, auth_user u where c.user_id=u.id ') 
    return render(request, "templates/home.html", {'chat': data})

def post(request):
    if request.method == "POST":
        message = request.POST.get('message', None)
        raw = Chat(user=request.user, message=message)
        if message:
            raw.save()
        return HttpResponseRedirect('/home/')

def login_user(request):
    print request
    if request.method == "POST":
        user = request.POST['username']
        pas = request.POST['password']
        user_auth = authenticate(username=user, password=pas)

        if user_auth is not None:
            if user_auth.is_active:
                login(request, user_auth)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    return render(request, "templates/login.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

