from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterForm, LoginForm

# Create your views here.

    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            request.session["user_id"] = user.id

            return redirect("home")

    return render(request, "register.html", {"form": RegisterForm()})



def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.authenticate()
            if user:
                request.session["user_id"] = user.id
                return redirect("home")
            
            form.add_error(None, "Невірний логін або пароль!")
        
        return render(request, "login.html", {"form": form})


    return render(request, "login.html", {"form": LoginForm()})


def logout(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    
    return redirect("/user/login")
