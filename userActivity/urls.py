from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/$', views.snippet_list),
    url(r'^users/login/', views.snippet_list),
    url(r'^users/logout/', views.logout),

]
urlpatterns = format_suffix_patterns(urlpatterns)
