from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'app/index.html'}, name='logout'),
    url(r'^feed/(?P<name>[a-z]+)/$', views.feedname, name='feed')
]
