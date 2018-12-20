# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from users.views import LoginView,RegisterView,AciveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogoutView
from organization.views import OrgView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
from users.views import IndexView


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #处理静态文件
    url('^$', IndexView.as_view(),name="index"),
    #login登录文件处理
    url('^login/$', LoginView.as_view(),name="login"),
    #退出的登录的login
    url('^logout/$', LogoutView.as_view(),name="logout"),
    url('^register/$', RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    #课程机构的url配置
    url(r'^org/', include('organization.urls', namespace="org")),
    #课程相关url的配置
    url(r'^course/', include('courses.urls', namespace="course")),
    #讲师的url的配置
    #url(r'^teacher/', include('courses.urls', namespace="course")),
    #配置media上传文件访问配置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    #url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),
    #配置用户中心
    url(r'^users/', include('users.urls', namespace="users")),
    #富文本url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]


#全局404页面的配置
handler404 = 'users.view.page_not_found'
#全局变量500页面配置
handler500 = 'users.views.page_error'