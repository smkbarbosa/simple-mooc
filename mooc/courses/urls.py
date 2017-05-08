from django.conf.urls import url

from mooc.courses import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^contato/', views.contact, name='contato'),
]
