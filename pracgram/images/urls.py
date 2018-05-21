from django.conf.urls import url
from django.conf.urls import include,url
from django.urls import include, path
from . import views

app_name = "images"
urlpatterns = [

    url(
        regex=r'^all/$',
        view=views.ListAllImages.as_view(),
        name='all_images'
    ),

    url(
        regex=r'^comments/$',
        view=views.ListAllComments.as_view(),
        name='all_comments'
    ),

    url(
        regex=r'^likes/$',
        view=views.ListAllLikes.as_view(),
        name='all_likes'
    ),

]
