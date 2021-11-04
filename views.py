from django.shortcuts import render, redirect
#from .forms import FormNewUser
from sampledepotapp.models import SampledepotappUsers

def showform(request):
    #form= FormNewUser(request.POST or None)
    #if form.is_valid():
    #    form.save()                      
    #context= {'New User': form }
    users = SampledepotappUsers.objects.all()
    return render(request, 'sampledepot.html', {'users':users})
