from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(),name='single'),
]
