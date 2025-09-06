from django.shortcuts import render
from .models import Project, Tag
from myapps.faq.models import Faq
from .forms import ProjectForm, TagForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    projects = Project.objects.all()    

        
    context = {
        'projects': projects
    }
    
    return render(request, 'portafolios/home.html', context)

def projectsList(request):
    
    projects = Project.objects.all()    
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


def create_project(request):
    
    project_form = ProjectForm()
    
    context = {
        'project_form': project_form
    }
    
    return render(request, 'portafolios/createProject.html', context)

