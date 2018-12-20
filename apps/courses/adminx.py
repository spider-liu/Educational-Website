# -*- coding: utf-8 -*-
__author__ = 'spiderliu'
__date__ = '2018/11/14 9:53'

from .models import Course,Lesson,Video,CourseResourse,BannerCourse
import xadmin
from organization.models import CourseOrg

#在课程中添加嵌套章节一栏
class LessonInline(object):
    model=Lesson
    extra=0


#在课程中添加嵌套课程资源一栏
class CourseResourceInline(object):
    model=CourseResourse
    extra=0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time','get_zj_nums','go_to']
    search_fields=['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    #排序
    ordering=['-click_nums']
    #只读
    readonly_fields=['click_nums']
    # 在此项上面可以进行直接修改编辑
    list_editable=['degree','desc']
    #在xamin中隐藏点击数
    exclude=['fav_nums']
    #引入class的lessoninline
    inlines=[LessonInline,CourseResourceInline]
    #连接富文本
    style_fields={"detail":"ueditor"}
    #excel导入文件变量
    import_excel = True

    def queryset(self):
        qs=super(CourseAdmin,self).queryset()
        #使用了is_banner
        qs=qs.filter(is_banner=False)
        return qs
    #xadmin中定时刷新
    refresh_times = [3,5]
    #重载方法进行保存课程的时候统计课程机构的课程数
    def save_models(self):
        obj=self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org=obj.course_org
            course_org.course_nums=Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields=['name', 'desc', 'detail', 'degree','students','fav_nums','image','click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree','learn_times','students','fav_nums','image','click_nums','add_time']
    #排序
    ordering=['-click_nums']
    #只读
    readonly_fields=['click_nums']
    #在xamin中看不到
    exclude=['fav_nums']
    #引入class的lessoninline
    inlines=[LessonInline,CourseResourceInline]
    #重载方式显示轮播图与课程的分离的时候，轮播图可以显示选中课程的轮播图。
    def queryset(self):
        qs=super(BannerCourseAdmin,self).queryset()
        #使用了is_banner
        qs=qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields=['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields=['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourseAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields=['course', 'name', 'download']
    list_filter = ['course', 'name', 'download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResourse,CourseResourseAdmin)