from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^image/$', views.add_image, name='upload_image'),
    url(r'^how/$', views.how_it_works, name='how'),

]
