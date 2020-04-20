"""testrun_back URL Configuration

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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('create_post',views.PostCreate.as_view(),name='post_create'),
    path('drafts/',views.Draftview.as_view(),name='drafts'),
    path('posts/',views.PublishedPosts.as_view(),name='posts'),
    path('posts/<slug>/',views.PostDetail.as_view(),name='detail'),
    path('delete/<slug>',views.PostDelete.as_view(),name='delete'),
    path('publish/<slug>',views.publish,name='publish'),
    path('prototype/designs',views.DesignsView.as_view(),name='designs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)