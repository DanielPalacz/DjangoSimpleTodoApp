from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.todolist_index, name='main-todolist-index'),
    path('<int:pk>/', views.todolist_show_items, name='main-todolist-show_items'),
]
