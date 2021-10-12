from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView

from .forms import NewUserForm, Home
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .models import Post


def main(request):
    if request.method == "POST":
        form = Home(request.POST)
        return render(request=request, template_name="main.html", context={"main_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Registration failed. Invalid data.")
    else:
        form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


class PostsListView(generic.DetailView):
    model = Post
    queryset = Post.objects.all()
    paginate_by = 10

    template_name = 'posts_list.html'
