from django.http import HttpResponse

def index(request):
    return HttpResponse("Society Members Index")