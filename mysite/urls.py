from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
]
