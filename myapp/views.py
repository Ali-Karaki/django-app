from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    context = {
        'name': "Robert",
        'age': 83
    }
    # return HttpResponse('<h1>Test Works</h1>') # before having templates
    # after creating templates
    return render(req, 'index.html', context)