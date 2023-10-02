from django.urls import path
from app_base.views import BaseView

app_name = 'app_base'

urlpatterns = [
    path('', BaseView.as_view(), name='base')
]
