from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

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




def task_list(request, id):
    project = Project.objects.get(id=id)

    if project is not None:
        tasks = project.tasks.all()
        projects = Project.objects.all()

        deadline = request.GET.get("deadline")
        if deadline:
            tasks = tasks.filter(deadline__lte=deadline)

        status_filter = request.GET.getlist("status")
        if status_filter:
            tasks = tasks.filter(status__in=status_filter)


        sort = request.GET.get("sort")
        if sort == "asc":
            tasks = tasks.order_by("deadline")
        elif sort == "desc":
            tasks = tasks.order_by("-deadline")

        view = request.GET.get("view", "table")

        return render(request, "tasks.html", {"project": project, "tasks": tasks, "projects": projects, "view": view})
    
    return redirect("home")


def create_task(request, id):
    project = Project.objects.get(id=id)
    
    if project is None:
        return redirect("home")

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect(f"/tasks/{id}")

    form = TaskForm()

    projects = Project.objects.all()

    return render(request, "create_task.html", {"form": form, "project": project, "projects": projects})


def edit_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return redirect("home")

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            project_id = task.project.id

            return redirect(f"/tasks/{project_id}")
    
    projects = Project.objects.all()
    project = task.project

    return render(request, "edit_task.html", {"form": form, "projects": projects, "project": project})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    
    if task is not None:
        project_id = task.project.id
        task.delete()

    return redirect(f"/tasks/{project_id}")
