from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_project/", views.create_project),
    path("delete_project/<int:id>", views.delete_project),
    path("edit_project/<int:id>", views.edit_project),
    path("tasks/<int:id>", views.task_list),
    path("create_task/<int:id>", views.create_task),
    path("edit_task/<int:id>", views.edit_task),
    path("delete_task/<int:id>", views.delete_task),

]