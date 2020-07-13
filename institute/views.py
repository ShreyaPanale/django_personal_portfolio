from django.shortcuts import render

# Create your views here.
from .models import Education
def home(request):
    institutes =  Education.objects.all(),
    return render(request, 'portfolio/home.html', {'institutes':institutes})
