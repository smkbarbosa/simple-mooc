from django.conf.urls import url

from mooc.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/', views.contact, name='contato'),
]
