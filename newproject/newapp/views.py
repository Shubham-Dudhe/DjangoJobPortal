from django.shortcuts import render,redirect
from django import forms
from .models import JobPortals,ScheduleJob
from django.http import HttpResponse

def sidebar(request):
    jps = JobPortals.objects.values("company_name").distinct().order_by('id')
    context = {'navbar':jps}

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        jps = JobPortals.objects.get(company_name = company_name)
        jps_company = JobPortals.objects.values("company_name").distinct().order_by('id')
        context = {'jps':jps,'navbar':jps_company}    
        return render(request, 'sidebar.html',context)
    
    return render(request,'sidebar.html',context)

def post_data(request):
    if request.method == 'POST':
        json_dictionary = {}
        jps = JobPortals.objects.get(company_name = request.POST.get('company_name'))

        for i in request.POST:
            json_dictionary.update({i:request.POST.get(i)})
        
        keys = ['csrfmiddlewaretoken','datetime','company_name']
        for i in keys:
            json_dictionary.pop(i)

        scjob = ScheduleJob(schedule_time=request.POST.get('datetime'),parameter=[json_dictionary],job_portals=jps)
        scjob.save()
        return render(request, 'success.html')