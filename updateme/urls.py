from django.conf.urls import include, url
from django.contrib import admin

# Url patterns mapping.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Included mapping present in app/urls.py
    url(r'^app/', include('app.urls')),
    url(r'^', include('app.urls', namespace='some_app')),
]
