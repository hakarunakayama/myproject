from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
# from ..models.siteimage import Siteimage

class NewcounselorView(TemplateView):
    template_name = "newcounselor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "侍太郎"
        context['image'] = "media/images/reception.png"

        return context

# all = Siteimage.objects.all()




    