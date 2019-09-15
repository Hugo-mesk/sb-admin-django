from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from example.models import Button, Form, Size, Color, FaStyle

class ButtonListView(TemplateView):

    template_name = "example/buttons_list_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = Button.objects.all()
        context["forms"] = Form.objects.all()
        context["sizes"] = Size.objects.all()

        return context
