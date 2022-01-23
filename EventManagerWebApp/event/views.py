from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
#from django.http import HttpResponse
from django.contrib import messages
from datetime import date
import datetime

#from event.models import event_tbl
#from . import models
from .models import event_tbl
from .models import participant_tbl

# Create your views here.
def index(request):
    return render(request, 'index.html')

def events(request):   
    return render(request, 'events.html')

def eventRegistration(request):
    params=dict()
    params['today_date'] = datetime.datetime.now()
    if request.method=="POST" :
        print("this is post")
        name = request.POST['ename']
        desc = request.POST['desc']
        plink = request.POST['plink']
        fromdt = request.POST['from']
        todt = request.POST['to']
        deadline = request.POST['deadline']
        hemail = request.POST['hemail']
        hpass = request.POST['hpass']
        print(name,desc,plink,fromdt,todt,deadline, hemail,hpass)
        data = event_tbl(name=name, desciption=desc, poster_link=plink, from_dt=fromdt, to_dt=todt, deadline=deadline, email=hemail, password=hpass)
        try:
            data.save()
            messages.success(request, "Registration Successfull!!")
        except:
            messages.error(request, "Event name should be distinct.")
        #params = {'submit':True}

    return render(request, 'eventRegistration.html', params)

def participantRegistration(request):
    allData = event_tbl.objects.all()
    print(allData)
    params = {'data':allData}
    '''
    for e in allData :
        if(e.deadline >= date.today()) :
            print(e.deadline)
    '''
    params['today_date'] = date.today()

    if request.method=="POST" :

        params['submit'] = False
        name = request.POST['name']
        contact = request.POST['contact']
        pemail = request.POST['pemail']
        ename = request.POST['ename']
        rtype = request.POST['rtype']
        try:
            ppl = request.POST['ppl']
        except MultiValueDictKeyError:
            ppl = 1
        #print(name, contact, pemail, ename, rtype, ppl)
        
        pdata = participant_tbl.objects.all()
        #print(pdata)
        status = True
        for p in pdata :
            if(p.event_name==ename and p.email==pemail) :
                status = False

        if(status) :
            data = participant_tbl(name=name, contact=contact, email=pemail, event_name=ename, reg_type=rtype, people=ppl)
            data.save()
            params['submit']=True
            messages.success(request, "Registration Successfull!!")
            
    return render(request, 'participantRegistration.html', params)
    
def about(request):   
    return render(request, 'about.html')

def contact(request):   
    return render(request, 'contact.html')
    