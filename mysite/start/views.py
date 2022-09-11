from django.shortcuts import render
#from .models import *

def hi(request):
    return render(request, 'start\home.html')
    #return HttpResponse(template.render(context, request))
