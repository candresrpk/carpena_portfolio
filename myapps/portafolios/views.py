from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portafolios/home.html')

def projectsList(request):
    return render(request, 'portafolios/projectsList.html')


def faq(request):
    return render(request, 'portafolios/faq.html')


