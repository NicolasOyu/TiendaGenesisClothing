from django.urls import path
from . import views
app_name = "informacion"
urlpatterns = [
    path('', views.PostListView.as_view(), name='lista'),
    path('categoria/<slug:slug>/', views.PostByCategoryView.as_view(), name='por_categoria'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detalle'),
]