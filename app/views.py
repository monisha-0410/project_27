from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(Topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'create_topic.html')

def create_web(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        u=request.POST['u']
        em=request.POST['em']
        TO=Topic.objects.get(Topic_name=tn)
        wo=WebPage.objects.get_or_create(Topic_name=TO,name=n,url=u,Email=em)[0]
        wo.save()
        QLWO=WebPage.objects.all()
        d1={'QLWO':QLWO}
        return render(request,'display_web.html',d1)
    return render(request,'create_web.html',d)

def select_multiple_web(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
    
        topic_list=request.POST.getlist('tn')
        QLWO=WebPage.objects.none()
        for topic_name in topic_list:
            QLWO=QLWO|WebPage.objects.filter(Topic_name=topic_name)
        d1={'QLWO':QLWO}
        return render(request,'display_web.html',d1)
    return render(request,'select_multiple_web.html',d)