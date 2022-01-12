
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.SignUp.as_view(), name='signup_view'),
    path('login', views.Login.as_view(), name='login_view'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:user_id>/', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('username_change',views.username_change,name='username_change'),
    path("username_change_done/", views.username_change_done, name="username_change_done"),
    path('email_change',views.email_change,name='email_change'),
    path("email_change_done/", views.email_change_done, name="email_change_done"),
    path('image_change',views.image_change,name='image_change'),
    path('image_change_done',views.image_change_done,name='image_change_done'),
    path('password_change', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('logout', views.Logout.as_view(), name="logout"),
]

