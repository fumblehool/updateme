from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# mapping for our app.
app_name = 'app'
urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    # /app/register/
    url(r'^register/$', views.register, name='register'),
    # /app/login/ using template = templates/app/login.html
    url(r'^login/$', auth_views.login,
        {'template_name': 'app/login.html'},
        name='login'),
    # /app/logout/ using template = templates/app/index.html
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'app/index.html'},
        name='logout'),
    # /app/feed/<category> 
    url(r'^feed/(?P<name>[a-z]+)/$', views.feedname, name='feed')
]
