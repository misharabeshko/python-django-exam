from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProjectForm()

    projects = Project.objects.all()

    return render(request, "create_project.html", {"form": form, "projects": projects})


def edit_project(request, id):
        try:
            project = Project.objects.get(id=id)
        except Project.DoesNotExist:
            return redirect("home")

        form = ProjectForm(instance=project)

        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)

            if form.is_valid():
                form.save()
                return redirect("home")
        projects = Project.objects.all()

        return render(request, "edit_project.html", {"form": form, "projects": projects})


def delete_project(request, id):
    project = Project.objects.get(id=id)

    if project is not None:
        project.delete()

    return redirect("home")




