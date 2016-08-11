from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$',views.log_in,name='log_in'),
    url(r'^signin$',views.sign_in,name='sign_in'),
    url(r'^logout$',views.log_out,name='log_out'),
    url(r'^pwdchange$',auth_views.password_change),
    url(r'assistant',views.assistant,name='assistant'),
    url(r'queue',views.queue,name='queue'),
    url(r'register',views.register,name='register')
]