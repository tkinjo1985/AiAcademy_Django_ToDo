from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('new/', views.New.as_view(), name='new'),
    path('datail/<int:todo_id>', views.Detail.as_view(), name='detail'),
    path('done/<int:todo_id>', views.Done.as_view(), name='done'),
    path('delete/<int:todo_id>', views.Delete.as_view(), name='delete'),
]
