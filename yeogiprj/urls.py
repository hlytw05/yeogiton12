"""yeogiprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from venv import create
from django.conf import settings
from django.contrib import admin
from django.urls import path
import account.views
from yeogiapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('create_recomment/<int:post_id>/<int:comment_id>',views.create_recomment, name="create_recomment"),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
    path('postdetail/<int:post_id>', views.postdetail, name='postdetail'),
    path('postlike/<int:post_id>', views.postlike, name='postlike'),
    path('postupdate/<int:post_id>', views.postupdate, name='postupdate'),

    path('commentcreate/<int:post_id>', views.commentcreate, name='commentcreate'),
    path('commentdelete/<int:comment_id>', views.commentdelete, name='commentdelete'),
    path('commentupdate/<int:comment_id>', views.commentupdate, name='commentupdate'),

    path('account/login', account.views.login_view, name="login"),
    path('account/logout', account.views.logout_view, name="logout"),
    path('account/signup', account.views.signup_view, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
