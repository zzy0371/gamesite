from django.conf.urls import url
from . import views
app_name = 'game'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^game/$',views.game,name='game'),
    url(r'^join/$',views.join,name='join'),
    url(r'^work/$',views.work,name='work'),
    url(r'^contact/$',views.contact,name='contact'),
]

# TODO 介入百度地图