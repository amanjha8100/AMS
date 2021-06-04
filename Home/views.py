from django.shortcuts import render,redirect
from .models import student,attendanceclass,subject,time,attendance
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from .forms import AttendanceForm
from django.http import HttpResponse
import csv
# Create your views here.
dateg = datetime.date.today() - datetime.timedelta(days=1)
print("dekh")
print(dateg)
def index(request):
    return render(request, 'home/index.html',{
        "students":student.objects.order_by('roll')
    })

@login_required
def class_date(request):
    n = timezone.now()
    k = datetime.datetime.now()
    global dateg
    print(dateg)
    status = 0
    date = datetime.date.today()
    time = k.strftime("%H%M")
    datec = datetime.date.today() - datetime.timedelta(days=1)
    if time >= "0001" and dateg == datec:
        if(date.weekday()==1 or date.weekday==3):
            status=1
        else:
            status=0
        dateg = date
        reg = attendanceclass(date = date , status = status)
        reg.save()
    ob = attendanceclass.objects.all()
    #base = datetime.datetime.today()
    #numdays=31
    #date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
    return render(request, 'home/t_class_date.html',{
        "status":ob
    })


def sub(request):
    sub=subject.objects.order_by('sub')
    return render(request, 'home/t_clas.html',{
        "sub":sub
    })

@login_required
def a_form(request):
    form = AttendanceForm()
    if request.method == "POST":
        form=AttendanceForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            form.save()
            #messages.success(request,"Your Attendance is recorded.")
            return redirect('attend')
    return render(request,"home/attendance_form.html",{'form':form})

@login_required
def attend(request):
    name=request.user.get_full_name()
    firstname=request.user.get_short_name()
    return render(request, 'home/t_attendance.html',{
        "name":name,"firstname":firstname
    })

@login_required
def load_sub(request):
    sub_id=request.GET.get('sub_id')
    print(sub_id)
    times = time.objects.filter(sub_id=sub_id)
    return render(request, "home/sub_dropdown.html",{
        "times":times
    })

@login_required
def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Name','Roll Number','Date','Subject','WeekDay'])
    today = datetime.date.today()
    today_filter = attendance.objects.filter(date__year=today.year,date__month=today.month,date__day=today.day)
    for attend in today_filter.values_list('name','roll','date','sub','time'):
        writer.writerow(attend)
    response['Content-Disposition']='attachment; filename="attendance.csv"'
    return response
    #writer.writerow(['name','roll','date','sub','time'])

@login_required
def attendancefilter(request):
    qs=attendance.objects.all()
    nameq = request.GET.get('name')
    rollq = request.GET.get('roll')
    dateq = request.GET.get('date')
    if nameq != '' and nameq is not None:
        qs=qs.filter(name=nameq)
    if rollq != '' and rollq is not None:
        qs=qs.filter(roll__icontains=rollq)
    # if subjectq != '' and subjectq is not None:
    #     qs=qs.filter(sub__icontains=subjectq)
    if dateq != '' and dateq is not None:
        qs=qs.filter(date=dateq)
    context = {
        'qs':qs,
        'nameq':nameq,
        'rollq':rollq,
        'dateq':dateq,
    }
    return render(request, 'home/attendance_filter.html',context)
