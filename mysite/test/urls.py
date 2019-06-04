from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^helloworld/$', views.helloworld),
    url(r'^time/$', views.current_time),
    url(r'^time2/$', views.current_time2),
    url(r'^time3/$', views.current_time3),
    url(r'^time4/$', views.current_time4),
    url(r'^time5/$', views.current_time5),
    url(r'^time6/$', views.current_time6),
    url(r'^baidu/$', views.baidu),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^time2/plus/(\d{1,2})/$', views.hours_ahead2),
]
