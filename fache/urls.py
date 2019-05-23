"""fache URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from tongzhidan import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('create/', views.create, name='create'),

    path('about/', views.About.as_view(), name='about'),


    path('list/<pk>/', views.detail, name='detail'),
    # path('list/<pk>/delete/', views.delete, name='delete'),
    path('list/<pk>/delete/', views.FacheDelete.as_view(), name='delete'),

    path('list/<pk>/update/', views.update, name='update'),

    path('list/', views.index, name='list'),

    path('admin/', admin.site.urls),


    path('huowu/', views.HuowuList.as_view(), name='huowu_list'),
    path('huowu/create/', views.HuowuCreate.as_view(), name='huowu_create'),
    path('huowu/update/<pk>', views.HuowuUpdate.as_view(), name='huowu_update'),
    path('huowu/delete/<pk>', views.HuowuDelete.as_view(), name='huowu_delete'),
    path('huowu/detail/<pk>', views.HuowuDetail.as_view(), name='huowu_detail'),

    path('daozhan/', views.DaozhanList.as_view(), name='daozhan_list'),
    path('daozhan/create/', views.DaozhanCreate.as_view(), name='daozhan_create'),
    path('daozhan/update/<pk>', views.DaozhanUpdate.as_view(), name='daozhan_update'),
    path('daozhan/delete/<pk>', views.DaozhanDelete.as_view(), name='daozhan_delete'),
    path('daozhan/detail/<pk>', views.DaozhanDetail.as_view(), name='daozhan_detail'),

    path('fachekehu/', views.FachekehuList.as_view(), name='fachekehu_list'),
    path('fachekehu/create/', views.FachekehuCreate.as_view(), name='fachekehu_create'),
    path('fachekehu/update/<pk>', views.FachekehuUpdate.as_view(), name='fachekehu_update'),
    path('fachekehu/delete/<pk>', views.FachekehuDelete.as_view(), name='fachekehu_delete'),
    path('fachekehu/detail/<pk>', views.FachekehuDetail.as_view(), name='fachekehu_detail'),


    path('guige/', views.GuigeList.as_view(), name='guige_list'),
    path('guige/create/', views.GuigeCreate.as_view(), name='guige_create'),
    path('guige/update/<pk>', views.GuigeUpdate.as_view(), name='guige_update'),
    path('guige/delete/<pk>', views.GuigeDelete.as_view(), name='guige_delete'),
    path('guige/detail/<pk>', views.GuigeDetail.as_view(), name='guige_detail'),

    path('baozhuang/', views.BaozhuangList.as_view(), name='baozhuang_list'),
    path('baozhuang/create/', views.BaozhuangCreate.as_view(), name='baozhuang_create'),
    path('baozhuang/update/<pk>', views.BaozhuangUpdate.as_view(), name='baozhuang_update'),
    path('baozhuang/delete/<pk>', views.BaozhuangDelete.as_view(), name='baozhuang_delete'),
    path('baozhuang/detail/<pk>', views.BaozhuangDetail.as_view(), name='baozhuang_detail'),

]



# urlpatterns += staticfiles_urlpatterns()