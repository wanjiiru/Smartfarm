from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^profile/$', views.update_profile, name="update_profile"),
]
