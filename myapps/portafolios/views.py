from django.shortcuts import render, redirect
from .models import Project, Tag
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


def create_project(request):
    
    project_form = ProjectForm()
    context = {
        'project_form': project_form
    }
    
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
            project_form = ProjectForm()
            return redirect('portafolios:projectsList')
        else:
            context['errors'] = project_form.errors
            return render(request, 'portafolios/createProject.html', context)            
            
    return render(request, 'portafolios/createProject.html', context)

