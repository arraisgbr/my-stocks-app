from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = 'app_base/pages/base.html'
