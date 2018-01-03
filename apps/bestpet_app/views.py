# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Pet

# Create your views here.

def index(request):
    context = {
    'newPets' : Pet.objects.all()
    }
    return render(request, 'bestpet_app/index.html', context)

def process(request):
    Pet.objects.create(pet_name = request.POST['pet_name'])
    return redirect('/')