from django.shortcuts import render
from .models import Project
from institute.models import Education
from skills.models import Skills
from interests.models import Interests

def home(request):
    projects = Project.objects.all()
    institutes = Education.objects.all()
    skills = Skills.objects.all()
    interests = Interests.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects
                                                   , 'institutes':institutes
                                                   , 'skills':skills
                                                   , 'interests':interests})
