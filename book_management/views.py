from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    title_str = 'Hello'
    detail_str = 'Detail first time whit phyton'
    # template = loader.get_template('index.html')
    context = {
        'title' : title_str,
        'detail' : detail_str
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)