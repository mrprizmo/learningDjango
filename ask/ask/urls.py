from django.contrib import admin
from django.urls import include, url
from qa.views import test

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', test),
    url(r'^login/?$', test),
    url(r'^signup/?$', test),
    url(r'^popular/?$', test),
    url(r'^ask/', test),
    url(r'^question/(<(?P<id>[1-9]+[0-9]*)>)/?$', include('qa.urls'))
]
