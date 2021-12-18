from django.shortcuts import render, redirect
#from .forms import FormNewUser
from sampledepotapp.models import SampledepotappUsers
from sampledepotapp.models import Music, Genre
from Accounts.forms import searchForm
from django.db.models import Q 
from django.views.generic import TemplateView, ListView


def showform(request):
    #form= FormNewUser(request.POST or None)
    #if form.is_valid():
    #    form.save()                      
    #context= {'New User': form }
        #Music.objects.filter(music_id__in = [e.music_upload for e in users])
    users = Music.objects.all()
        #music_made = users.music_upload
    return render(request, 'sampledepot.html', {'music': users})

class SearchResultsView(ListView):
    model = Music
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        final =  Music.objects.filter(
            Q(title__icontains = query))
        print(query)
        print(final)
        return {"music": final}

def search_view(request):
    qs = Music.objects.all()
    title = request.GET.get('q')
    if title != "":
        qs = qs.filter(title__icontains=title)
    return render(request, "search_results.html", {"music": qs})
