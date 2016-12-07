from django.conf.urls import url

from . import views

app_name = 'afisha'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex: /events/5/
    url(r'^event/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #ex: /events/5/add_comment
    url(r'^event/(\d+)/add_comment/$', views.add_comment, name='add_comment'),

]
