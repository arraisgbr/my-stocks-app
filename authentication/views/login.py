from django.views.generic.edit import FormView
from authentication.forms.login import LoginForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class LoginView(FormView):
    template_name = 'authentication/pages/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('stock:stock_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)