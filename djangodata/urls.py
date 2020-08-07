"""djangodata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authapp.views as authview
import sysapp.views as sysview
import blogapp.views as blogview

urlpatterns = [
    path('admin/', admin.site.urls),  # django自带的后台管理功能的首页地址
    path('', authview.index),         #
    path('login/', authview.goLogin),  #
    path('slogin/', authview.login),  #
    path('newuser/', authview.goNewUser),  #
    path('regnewuser/', authview.regNewUser),
    path('checkUserName/', authview.checkUserName),
    path('userlist/', sysview.getUserList),
    path('goclasslist/', blogview.goBlogClass),
    path('classlist/', blogview.getBlogClass),
    path('gobloglist/', blogview.goBlogList),
    path('bloglist/', blogview.blogList),
    path('gowriteblog/', blogview.goWriteBlog),
    path('upload/', blogview.uploadFile),
    path('goupdateblog/', blogview.goUpdateBlog),
    path('goindex/', authview.goIndex),
    path('logout/', authview.logout),
    path('viewblog/',  blogview.viewBlog),
]
