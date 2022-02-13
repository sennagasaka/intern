
from . import views
from django.urls import path

urlpatterns = [
    path('',  views.IndexView.as_view(), name='index'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('talk_room/<int:user_id>/', views.TalkRoomView.as_view(), name='talk_room'),
    path('setting', views.SettingView.as_view(), name='setting'),
    path('username_change',views.UserNameChangeView.as_view(),name='username_change'),
    path("username_change_done/", views.UsernameChangeDoneView.as_view, name="username_change_done"),
    path('email_change',views.EmailChangeView.as_view(),name='email_change'),
    path("email_change_done/", views.EmailChangeDoneView.as_view, name="email_change_done"),
    path('image_change',views.ImageChangeView.as_view(),name='image_change'),
    path('image_change_done',views.ImageChangeDoneView.as_view,name='image_change_done'),
    path('password_change', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done', views.PasswordChangeDone.as_view(), name='password_change_done'),
]

