from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(Topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic data inserted successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        TO=Topic.objects.get(Topic_name=topic)

        WO=Webpage.objects.get_or_create(Topic_name=TO,Name=name,Url=url,Email=email)[0]
        WO.save()
        return HttpResponse('webpage data inserted done')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    LOT=Webpage.objects.all()
    d={'webpages':LOT}

    if request.method=='POST':
        Name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(Name=Name)
        AO=AccessRecord.objects.get_or_create(Name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('AccessRecord insertion is done Successfully')

    return render(request,'insert_access.html',d)