from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('new/', views.New.as_view(), name='new'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('done/<int:pk>', views.Done.as_view(), name='done'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
]
