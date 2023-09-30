from django.views.generic.edit import FormView
from authentication.forms.register import SignUpForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class SignUpView(FormView):
    template_name = 'authentication/pages/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('authentication:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)