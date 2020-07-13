from django.shortcuts import render

# Create your views here.
from .models import Skills
def home(request):
    skills =  Skills.objects.all(),
    return render(request, 'portfolio/home.html', {'skills':skills})
