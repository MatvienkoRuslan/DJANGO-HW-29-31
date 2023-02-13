from django.urls import path

from task import views

urlpatterns = [
    path('task_all/', views.task_all, name='task_all'),
    path('task_add/', views.task_add, name='task_add'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
