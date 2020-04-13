from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^form/', views.userForm, name='uform'),
]