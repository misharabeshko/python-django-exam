from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_project/", views.create_project),
    path("delete_project/<int:id>", views.delete_project),
    path("edit_project/<int:id>", views.edit_project),

]