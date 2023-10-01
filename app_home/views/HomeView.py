from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'app_home/pages/home.html'
