from django.urls import path
from authentication.views import SignUpView, LoginView, Logout

app_name = 'authentication'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
