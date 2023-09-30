from django.views.generic.edit import FormView
from authentication.forms.register import SignUpForm
from django.contrib.auth import login


class SignUpView(FormView):
    template_name = 'authentication/pages/signup.html'
    form_class = SignUpForm
    sucess_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)