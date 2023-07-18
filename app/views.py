from django.shortcuts import render
import datetime 
# Create your views here.
def built_in_filters(request):
    de=datetime.datetime.now()
    d={'data':'we are django students','c':10,'de':de}
    return render(request,'built_in_filters.html',d)
