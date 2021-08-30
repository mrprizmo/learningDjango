from django.contrib import admin
from django.urls import path, include, re_path
from qa.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', test),
    path('signup/', test),
    path('popular/', test),
    path('ask/', test),
    re_path(r'^question/(<?P<id>[1-9]+[0-9]*>)/', include('qa.urls'))
]
