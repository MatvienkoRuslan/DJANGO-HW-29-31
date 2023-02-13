from django.urls import path

from task import views

urlpatterns = [
    path('task_all/', views.task_all, name='task_all'),
    path('task_add/', views.task_add, name='task_add'),
<<<<<<< HEAD
    path('category/<int:cat_id>/', views.show_category, name='category'),
=======
>>>>>>> 666576243dd841d35c4e348d8cd972000ae66d4d
]
