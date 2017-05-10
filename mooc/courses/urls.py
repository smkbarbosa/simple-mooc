from django.conf.urls import url

from mooc.courses import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.details, name='details')
    #url(r'^contato/', views.contact, name='contato'),
]
