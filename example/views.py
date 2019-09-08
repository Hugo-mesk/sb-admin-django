from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from example.models import Button

class ButtonListView(ListView):

    model = Button
    context_object_name = "Buttons"
