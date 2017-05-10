from django.conf.urls import url

from mooc.courses import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details')
    #url(r'^(?P<pk>\d+)/$', views.details, name='details')
    #url(r'^contato/', views.contact, name='contato'),
]
