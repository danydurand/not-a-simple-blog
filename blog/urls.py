from django.urls import path
from . import views


app_name='blog'

urlpatterns = [
    path('<int:post_id>/share/', views.post_share, name='post-share'),
    # path('', views.PostListView.as_view(), name='post-list'),
    path('', views.post_list, name='post-list'),
    path('tag/<slug:tag_slug>', views.post_list, name='post-list-by-tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
        views.post_detail, name='post-detail'),
    
]
