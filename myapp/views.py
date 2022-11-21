from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import User

# Create your views here.


def index(req):
    rob = User("Rob", 40)
    tod = User("Tod", 30)
    users = [rob, tod]
    context = {
        "users": users
    }
    # return HttpResponse('<h1>Test Works</h1>') # before having templates
    # after creating templates
    return render(req, 'index.html', context)


def counterGET(req):
    text = req.GET['text']
    context = {
        'numWords': len(text.split())
    }
    return render(req, 'counter.html', context)
    

def counterPOST(req):
    text = req.POST['text']
    context = {
        'numWords': len(text.split())
    }
    return render(req, 'counter.html', context)
