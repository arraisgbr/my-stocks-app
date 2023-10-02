from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class Logout(LogoutView):
    next_page = reverse_lazy('app_base:base')