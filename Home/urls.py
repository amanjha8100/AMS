from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name="index"),
    #path('subject/class/',views.class_date,name="classdate"),
    path("subject/",views.sub,name="subject"),
    path("subject/attendance/",views.a_form,name="attend"),
    path("subject/attendance/ajax-load-sub/",views.load_sub,name="ajax_load_sub"),
]