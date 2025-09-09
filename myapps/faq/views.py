from django.shortcuts import render
from .models import Faq, Tag, Faq_tag, Faq_detail


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
    
    context = {
        'question': question,
        'details': details
    }
    
    return render(request, 'faq/detail.html', context)



    
    
    
    