from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
import rufirst.views
from rufirst.views import home

urlpatterns = [
    url(r'^$', rufirst.views.home),
    url(r'^login', django.contrib.auth.views.login, {'template_name':'ruru.html'}, name='login'),
    # url(r'^login', rufirst.views.login, name='login'),
    url(r'^newpost', rufirst.views.newpost, name='newpost'),
    url(r'^register', rufirst.views.register, name='register'),
    # url(r'^global', rufirst.views.globalstream, name='global'),
    url(r'^profile/(?P<username>\w+)$',rufirst.views.profile, name='profile'),
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^global', rufirst.views.home, name = 'global'),
    # url(r'^',rufirst.views.profile),

]