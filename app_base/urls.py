from django.urls import path
from .views.BaseView import BaseView

app_name = 'app_base'

urlpatterns = [
    path('', BaseView.as_view(), name='base')
]
