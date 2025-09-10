from django.shortcuts import render, redirect
from .models import Faq, Tag, Faq_tag, Faq_detail
from .forms import FaqForm, FaqDetailForm
from django.contrib import messages



# Create your views here.


def home(request):
    
    faq = Faq.objects.all()
    
    context = {
        'faq': faq
    }
    
    return render(request, 'faq/faq.html', context)


def Question_detail(request, pk):
    
    question = Faq.objects.get(id=pk)
    details = Faq_detail.objects.filter(faq=question).order_by('order')
    content_form = FaqDetailForm()
    
    context = {
        'question': question,
        'details': details,
        'content_form': content_form
    }
    
    return render(request, 'faq/detail.html', context)


def Create_question(request):
    
    context = {
        'form': FaqForm()
    }
    
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Question created successfully!")
            return redirect('faq:home')
        else:
            context['form'] = form
            messages.error(request, "Error creating question.")
            return render(request, 'faq/create.html', context)
        
    context['form'] = FaqForm()
    return render(request, 'faq/create.html', context)


def add_content(request, pk):
    
    
    faq = Faq.objects.get(id=pk)
    
    if request.method == "POST":
        form = FaqDetailForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.faq = faq
            content.save()
            messages.success(request, "Content added successfully!")
            return redirect('faq:detail', pk=faq.id)
        else:
            messages.error(request, "Error adding content.")
            return redirect('faq:detail', pk=faq.id)
        
    return redirect('faq:detail', pk=faq.id)





    
    
    
    