from django.shortcuts import render

# Create your views here.
from .models import Interests
def home(request):
    interests =  Interests.objects.all(),
    return render(request, 'portfolio/home.html', {'interests':interests})
