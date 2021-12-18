"""sampledepot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from Accounts import views as avw
from sampledepotapp import views as svw
urlpatterns = [
    path('admin/', admin.site.urls),
    path('showform/', svw.showform),
    path('', svw.showform, name="home"),
    path('login/', avw.login_view, name="login"),
    path('logout/', avw.logout_view, name = "logout"),
    path('new_user/', avw.register_view),
    path('profile/', avw.profile_view, name = "Profile"),
    path('upload/', avw.upload_view, name = "Upload"),
    path('search/', svw.search_view, name = "search")
]
