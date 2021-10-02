from django.contrib import admin
from django.urls import path, include, re_path
from qa.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    re_path(r'^login/?$', test),
    re_path(r'^signup/?$', test),
    re_path(r'^popular/?$', test),
    re_path(r'^ask/', test),
    re_path(r'^question/(<(?P<id>[1-9]+[0-9]*)>)/?$', include('qa.urls'))
]
