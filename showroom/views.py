from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def mainPage(request):
    brands = Brand.objects.all()
    return render(request, 'showroom/brands.html', {'brands':brands})

from django.shortcuts import render, get_object_or_404
from .models import Brand, Model

def models_by_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    models = Model.objects.filter(brand=brand)
    return render(request, 'showroom/models.html', {'models': models})

def car_features(request, model_id):
    model = get_object_or_404(Model, id=model_id)
    return render(request, 'showroom/features.html', {'model': model})

def ourteam(request):
    staff_members = Staff.objects.all()
    return render(request, 'showroom/team.html', {'staff_members': staff_members})
