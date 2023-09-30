from django.views.generic.edit import FormView
from authentication.forms.login import LoginForm
from django.contrib.auth import login


class LoginView(FormView):
    template_name = 'authentication/pages/login.html'
    form_class = LoginForm
    sucess_url = '/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)