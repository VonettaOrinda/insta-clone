from django.contrib import admin
from django.urls import re_path, path
from.import views
from instagram import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.home,name = 'home'),
     path('search/',views.search_results, name= 'search'),
     re_path(r'^accounts/profile/', views.add_profile, name='add_profile'),
     re_path(r'^profile/(\d+)', views.profile, name='profile'),
     re_path(r'^search/', views.search_results, name='search_results'),
     re_path(r'^image/(\d+)',views.get_image_by_id,name ='image'),
     re_path(r'^new/profile$', views.add_profile, name='add_profile'),
     re_path(r'^upload/', views.update_image, name='upload'),
     re_path(r'^comment/(?P<pk>\d+)',views.add_comment,name='comment'),
     re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
     re_path(r'^all/(?P<pk>\d+)', views.all, name='all'),

     # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     #      views.activate, name='activate'),
     re_path(r'^follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


     

