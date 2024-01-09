from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('cbv-index',views.IndexView.as_view(),name='cbv-index')
]

