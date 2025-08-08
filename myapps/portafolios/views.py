from django.shortcuts import render
from .models import Portafolio, Tag
from myapps.faq.models import Faq

# Create your views here.

def home(request):
    projects = Portafolio.objects.all()    

        
    context = {
        'projects': projects
    }
    
    return render(request, 'portafolios/home.html', context)

def projectsList(request):
    
    projects = Portafolio.objects.all()    
    tags = Tag.objects.all()
    
    if request.GET.get('tag'):
        projects = projects.filter(tag__name=request.GET.get('tag'))
        
    context = {
        'projects': projects,
        'tags': tags
    }
    
    return render(request, 'portafolios/projectsList.html', context)


def faq(request):
    
    faq = Faq.objects.all()
    
    context = {
        'faq': faq
    }
    
    return render(request, 'portafolios/faq.html', context)


