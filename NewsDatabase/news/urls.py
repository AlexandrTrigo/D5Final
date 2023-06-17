from django.urls import path
from .views import PostList, PostSearch, PostDetail, \
    PostCreateView, PostUpdateView, PostDeleteView

# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>', PostDetail.as_view()),
#     path('search/', PostSearch.as_view())
# ]


urlpatterns = [
    path('', PostList.as_view(), name='overview'),  # Ссылка на страницу с общим списком новостей
    path('search/', PostSearch.as_view(), name='post_search'),  # Ссылка на страницу с фильтрами
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),  # Ссылка на страницу новости
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание новости
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),  # Ссылка на обновление новости
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')  # Ссылка на удаление новости
]