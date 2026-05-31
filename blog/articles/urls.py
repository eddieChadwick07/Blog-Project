from django.urls import path
from .import views

urlpatterns = [
    path('', views.ArticleListView.as_view(),
         name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('article/new/', views.ArticleNewView.as_view(),
         name='article_new'),
    path('article/edit/<int:pk>', views.ArticleEditView.as_view(),
         name='article_edit'),
]