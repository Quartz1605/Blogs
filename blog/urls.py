from django.urls import path 
#from .views import post_list,post_detail
from .views import BlogDetailView,BlogListView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
  #path("",post_list,name="home"),
  #path("post/<int:pk>/",post_detail,name="post_detail")

  path("",BlogListView.as_view(),name="home"),
  path("post/<int:pk>/",BlogDetailView.as_view(),name="post_detail"),
  path("post/new/",BlogCreateView.as_view(),name="post_new"),
  path("post/<int:pk>/edit/",BlogUpdateView.as_view(),name="post_edit"),
  path("post/<int:pk>/delete/",BlogDeleteView.as_view(),name="post_delete")


]