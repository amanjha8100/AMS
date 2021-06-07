from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    #path('subject/class/',views.class_date,name="classdate"),
    path("allowattend/",views.allowattend,name="allow"),
    path("subject/",views.sub,name="subject"),
    path("subject/attendance/",views.a_form,name="attend"),
    path("subject/attendance/ajax-load-sub/",views.load_sub,name="ajax_load_sub"),
    path('subject/attendance/download',views.export,name="download"),
    path('filter/',views.attendancefilter,name="filter"),
]