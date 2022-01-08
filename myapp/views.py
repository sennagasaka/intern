from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm, SignUpForm, TalkForm,UsernameChangeForm, EmailChangeForm, PasswordChangeForm, ImageChangeForm
from django.db.models import Q
from .models import Talk
from django.urls import reverse_lazy



User = get_user_model()

def index(request):
    return render(request, "myapp/index.html")

class SignUp(CreateView):
    def post(self, request, *args, **kwargs):
        form=SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'myapp/signup.html', {'form':form})

    def get(self, request, *args, **kwargs):
        form=SignUpForm(request.POST)
        return render(request, 'myapp/signup.html', {'form':form})

signup=SignUp.as_view()

class Login(LoginView):
    authentication_form=LoginForm
    template_name='myapp/login.html'

def friends(request):
    user=request.user
    friends=User.objects.exclude(id=user.id)
    return render(request,"myapp/friends.html", {"friends":friends})


def talk_room(request,user_id):
    user=request.user
    friend=get_object_or_404(User,id=user_id)
    talk=Talk.objects.filter(Q(talk_from=user,talk_to=friend)|Q(talk_to=user,talk_from=friend)).order_by("time")
    form=TalkForm()
    context={
        "friend":friend,
        "form":form,
        "talk":talk
    }
    if request.method=="POST":
        new_talk=Talk(talk_from=user,talk_to=friend)
        form=TalkForm(request.POST,instance=new_talk)
        if form.is_valid():
            form.save()
            return redirect("talk_room", user_id)
    return render(request, "myapp/talk_room.html", context)

def setting(request):
    return render(request, "myapp/setting.html")

def username_change(request):
    user=request.user
    form=UsernameChangeForm(instance=user)
    if request.method=="POST":
        form=UsernameChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("username_change_done")
    context={
        "form":form,
    }
    return render(request, "myapp/username_change.html", context)

def username_change_done(request):
    return render(request, "myapp/username_change_done.html")


def email_change(request):
    user=request.user
    form=EmailChangeForm(instance=user)
    if request.method=="POST":
        form=EmailChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("setting")
    context={
        "form": form,
    }
    return render(request, "myapp/email_change.html", context)

def email_change_done(request):
    return render(request, "myapp/email_change_done.html")


def image_change(request):
    user=request.user
    form=ImageChangeForm(instance=user)
    if request.method=="POST":
        form=ImageChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("setting")
    context = {
        "form": form,
    }
    return render(request, "myapp/image_change.html", context)

def image_change_done(request):
    return render(request, "myapp/image_change_done.html")


class PasswordChange(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('password_change_done')
    template_name='myapp/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name='myapp/password_change_done.html'


class Logout(LogoutView):
    template_name='logout.html'