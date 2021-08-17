from django import template
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('core/index.html')
    
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('core/contact.html')
    
    return HttpResponse(template.render({}, request))

def publications(request):
    template = loader.get_template('core/publications.html')
    
    return HttpResponse(template.render({}, request))

def documents(request):
    template = loader.get_template('core/documents.html')
    
    return HttpResponse(template.render({}, request))