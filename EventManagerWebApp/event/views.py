from asyncio.windows_events import NULL
from twilio.rest import Client
import smtplib
#from django.dispatch import receiver
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
def sendEmail(email, msg):
    sender_email = "eventmanager21108@gmail.com"
    receiver_email = email
    password = "Woc@EventManager26"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)
    print('login successfull!')
    server.sendmail(sender_email, receiver_email, msg)
    print('Email sent')

def sendSms(pnumber,msg):
    account_sid = "AC08b217ac0b9b8d4bd9506c1fbfb759f5"
    auth_token = "c179b994b89041d37de6a010cfc6d45c"

    client = Client(account_sid, auth_token)

    sms = client.messages.create(
        body = msg,
        from_ = '+18045717572',
        to = pnumber
    )
    print(sms.sid)

def index(request):
    return render(request, 'index.html')

def logout(request):
    request.session['hEmail'] = NULL
    return render(request, 'index.html')

def events(request):
    if request.method=="POST" :
        #print("this is post")
        email = request.POST['hemail']
        psw = request.POST['hpass']
        try :
            event_data = event_tbl.objects.filter(email=email, password=psw)
            if event_data :
                request.session['hEmail'] = email
                params = {'data':event_data}
                #print (event_data.name)
                #eventDashboard(request)
                return render(request, 'eventDashboard.html', params)
            else :
                messages.success(request, "Login Failed!!")

        except :
            messages.error(request, "Login Failed!!")
    return render(request, 'events.html')

def eventDashboard(request):
    return render(request, 'eventDashboard.html')

def participantDetails(request, name):
    print(name)
    event_data = participant_tbl.objects.filter(event_name=name)
    params = {'data':event_data}
    return render(request, 'participantDetails.html', params)

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
            msg = "Hello "+hemail+", you are registered the new event named "+name+"\n\nThis all are the information about your event! \nEvent Name :"+name+"\nDescription :"+desc+"\nPoster Link"+plink+"\nStart Date :"+fromdt+"\nEnd Date :"+todt+"\nDeadline :"+deadline+"\nEvent-Password :"+hpass
            sendEmail(hemail, msg)
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
            msg = "Hello "+pemail+", You have registered in an event called "+ename+"\n\nYour Registered details \nName : "+name+"\nContact : "+contact+" \nRegisteration Type : "+rtype+"\nTotal Number of. People : "+str(ppl)
            sendEmail(pemail, msg)
            event_data = event_tbl.objects.get(name=ename)
            sms_msg = "Hey "+name+", \n You have registered in an event called "+event_data.name+"\n\nYour Regsitered details \nEvent Unique ID : "+str(event_data.id)+ "\nEvent Description : "+event_data.desciption+"\nEvent Poster : "+ event_data.poster_link +"\nStart Date : " + str(event_data.from_dt) + "\nEnd Date : "+ str(event_data.to_dt) +"\nIf you have any query then contcat, Host Email : " + event_data.email
            ph = "+91"+str(contact)
            try :
                sendSms(ph, sms_msg)
            except :
                messages.success(request, "This mobile number is not verified on twilio, so can't send the sms!!")
                
            messages.success(request, "Registration Successfull!!")
        else :
            messages.success(request, "You can't apply twice to this event!!")
            
    return render(request, 'participantRegistration.html', params)
    
def about(request):   
    return render(request, 'about.html')

def contact(request):   
    return render(request, 'contact.html')
    