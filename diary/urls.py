from django.urls import path
from . import views
from .views import IndexView
from django.contrib.auth import views as auth_views

from . import user_info



app_name = 'diary'

urlpatterns = [    
    path('', views.TopView.as_view(), name='top'),
    path('index/', views.IndexView.as_view(), name='index'),  # URL名を 'index' に設定
    path('prompt/', views.prompt, name='prompt'),
    
    path('login/', views.Login.as_view(), name='login'), # 追加
    path('logout/', views.Logout.as_view(), name='logout'), # 追加
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'), # 追加
    path('signup/', views.Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', views.SignupDone.as_view(), name='signup_done'), # サインアップ完了
    path('user_info/', user_info.my_view, name='user_info'),

]