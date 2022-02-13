from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import context
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import TalkForm,UsernameChangeForm, EmailChangeForm, PasswordChangeForm, ImageChangeForm, FindForm
from django.db.models import Q
from .models import Talk
from django.urls import reverse_lazy



User = get_user_model()



class IndexView(TemplateView):
    template_name='myapp/index.html'



class FriendsView(LoginRequiredMixin,ListView):
    model=User
    template_name="myapp/friends.html"

    def get(self, request, *args, **kwargs):
        user=request.user
        form=FindForm()
        friends = User.objects.exclude(id=user.id)
        context={
            'form':form,
            "friends":friends,
        }
        return render(request, "myapp/friends.html", context)

    def post(self, request, *args, **kwargs):
        user=request.user
        form=FindForm(request.POST)
        str=request.POST['find']
        friends=User.objects.exclude(id=user.id).filter(username__contains=str)
        context={
            'form':form,
            "friends":friends,
        }
        return render(request, "myapp/friends.html", context)


class TalkRoomView(LoginRequiredMixin,ListView):
    model=Talk
    template_name="myapp/talk_room.html"

    def get(self, request, user_id):
        user=request.user
        friend=get_object_or_404(User,id=user_id)
        talk=Talk.objects.filter(Q(talk_from=user,talk_to=friend)|Q(talk_to=user,talk_from=friend)).order_by("time")
        form=TalkForm()
        context={
            "friend":friend,
            "form":form,
            "talk":talk
        }
        return render(request, "myapp/talk_room.html", context)
    
    def post(self, request, user_id):
        user=request.user
        friend=get_object_or_404(User,id=user_id)
        talk=Talk(talk_from=user,talk_to=friend)
        form=TalkForm(request.POST,instance=talk)
        context={
            "friend":friend,
            "form":form,
            "talk":talk
        }   
        if form.is_valid():
            form.save()
            return redirect("talk_room", user_id)
        return render(request, "myapp/talk_room.html", context)



class SettingView(LoginRequiredMixin, TemplateView):
    template_name="myapp/setting.html"



class UserNameChangeView(LoginRequiredMixin,View):
    template_name="myapp/username_change.html"

    def get(self, request,  *args, **kwargs):
        user=request.user
        form=UsernameChangeForm(instance=user)
        context={
            "form":form,
        }
        return render(request, "myapp/username_change.html", context)

    def post(self, request,  *args, **kwargs):
        user=request.user
        form=UsernameChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("username_change_done")
        return render(request, "myapp/username_change.html", context)



class UsernameChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name="myapp/username_change_done.html"
    


class EmailChangeView(LoginRequiredMixin,View):
    template_name="myapp/email_change.html"

    def get(self, request,  *args, **kwargs):
        user=request.user
        form=EmailChangeForm(instance=user)
        context={
            "form":form,
        }
        return render(request, "myapp/email_change.html", context)

    def post(self, request,  *args, **kwargs):
        user=request.user
        form=EmailChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("email_change_done")
        context={
            "form":form,
        }
        return render(request, "myapp/email_change.html", context)   



class EmailChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name="myapp/email_change_done.html"



class ImageChangeView(LoginRequiredMixin,View):
    template_name="myapp/image_change.html"

    def get(self, request,  *args, **kwargs):
        user=request.user
        form=ImageChangeForm(instance=user)
        context={
            "form":form,
        }
        return render(request, "myapp/image_change.html", context)

    def post(self, request,  *args, **kwargs):
        user=request.user
        form=ImageChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("image_change_done")
        context={
            "form":form,
        }
        return render(request, "myapp/image_change.html", context)   

class ImageChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name="myapp/image_change_done.html"

class PasswordChange(LoginRequiredMixin,PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('password_change_done')
    template_name='myapp/password_change.html'

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name='myapp/password_change_done.html'


