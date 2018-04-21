from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.login),
    url(r'^users/login/', views.login),
    url(r'^users/logout/', views.logout),
    url(r'^users/ranked/',views.rankedUser),

]
urlpatterns = format_suffix_patterns(urlpatterns)
