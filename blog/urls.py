from django.urls import path,include
from . import views
from django.views.generic import TemplateView

app_name="blog"

urlpatterns=[
    # path('cbv-index',views.IndexView.as_view(),name='cbv-index'),
    path('api/v1/',include('blog.api.v1.urls')),

]

