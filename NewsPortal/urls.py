from django.urls import path, include
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostsSearch

urlpatterns = [
    path('', PostsList.as_view(), name='news_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', PostsSearch.as_view(), name='news_search'),
]
