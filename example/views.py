from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from example.models import Button, ButtonSubGroup, ButtonGroup

class ButtonListView(TemplateView):

    template_name = "example/buttons_list_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = Button.objects.all().select_related("sub_group")
        context["button_groups"] = ButtonGroup.objects.all()
        context["button_sub_groups"] = ButtonSubGroup.objects.all().select_related("group")

        return context
