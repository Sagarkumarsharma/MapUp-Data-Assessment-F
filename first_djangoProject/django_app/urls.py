from re import A
from django.urls import path
from.import views
#import PostListView class from the django_app view
from .views import (PostListView, 
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    )


urlpatterns = [
    path('', PostListView.as_view(), name = 'home-app'),
    path('post1/<int:pk>/update/', PostUpdateView.as_view(), name = 'post1-update'), # post update view
    path('post1/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post1-delete'),
    path('post1/<int:pk>', PostDetailView.as_view(), name = 'post1-detail'), #key creation for the post details
    path('post/new', PostCreateView.as_view(), name = 'post-create'), # create a post from the user
    #path('', PostListView.as_view(), name = 'home-app'),
    path('about/',views.about, name = 'about-app'),
   
]
