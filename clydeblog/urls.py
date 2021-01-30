"""clydeblog URL Configuration

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
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('arch_blog/', include('arch_blog.urls')),
    path('code_blog/', include('code_blog.urls')),
    path('diary/', include('diary.urls')),
    path('architecture/', include('architecture.urls')),
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('test', views.test, name='test'),
    path('ckeditor', include('ckeditor_uploader.urls')),    # 添加上传功能
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),  # 退出登录
    path('register/', views.register, name='register'),
    path('comment/', include('comment.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
