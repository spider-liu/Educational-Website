# -*- coding: utf-8 -*-
__author__ = 'spiderliu'
__date__ = '2018/11/13 21:01'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import Banner
from .models import UserProfile
#from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset,Main,Side,Row


# class UserProfileAdmin(UserAdmin):
#     pass

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    #头名
    site_title="spiderliu教育管理系统"
    #底名
    site_footer="spiderliu"
    #左侧栏项目收齐
    menu_style="accordion"

class EmailVerifyRecordAdmin(object):
    #显示栏中各个项目
    list_display=['code','email','send_type','send_time']
    #搜索功能
    search_fields=['code','email','send_type']
    #过滤器功能
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields=['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
#xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
