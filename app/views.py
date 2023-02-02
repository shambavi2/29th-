from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')

def webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        topic=request.POST.get('topic')
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is done')  
    return render(request,'Webpage.html',d)

def insert_access(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    if request.method=="POST":
        wp=request.POST['name']
        d=request.POST['date']
        
        W=Webpage.objects.get_or_create(name=W)[0]
        W.save()
        A=Access_Record.objects.get_or_create(name=W,dat=d)[0]
        A.save()
        return HttpResponse('insert_accessrecord created')
    return render(request,'insert_access.html',d)

def select_multiple(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        tos=request.POST.getlist('topic')
        print(tos)
        QSW=Webpage.objects.none()
        for i in tos:
            QSW=QSW|Webpage.objects.filter(topic_name=i)
        d1={'webpage':QSW}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple.html',d)

def checkbox(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'checkbox.html',d)































