from django.shortcuts import render
from django.views.generic import TemplateView

from library import models


class DashboardView(TemplateView):
    template_name = "admin_panel/admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context["books"] = models.Books.objects.all()
        context["authors"] = models.Authors.objects.all()
        context["publishers"] = models.Publishers.objects.all()
        context["translators"] = models.Translators.objects.all()
        return context
