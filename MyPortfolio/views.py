from django.shortcuts import render,HttpResponse,redirect
from Projects.models import ProjectShow
from ServicesView.models import ServicesSec
from Certificates.models import Certificate
from skills.models import Skills
from django.views.generic import View

from django.template.loader import render_to_string

from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.mail import BadHeaderError,send_mail
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMessage
import email.message , email.policy , email.utils, sys

import threading

class EmailThread(threading.Thread):
    def __init__(self,email_message):
        self.email_message=email_message
        threading.Thread.__init__(self)
    def run(self):
        self.email_message.send()







def index(request):
    
    Projectsdata= ProjectShow.objects.all()
    ServicesData= ServicesSec.objects.all()
    CertificatesData= Certificate.objects.all()
    SkillsData = Skills.objects.all()
    print(Projectsdata)
    data={
        'Projectsdata':Projectsdata,
        'ServicesData':ServicesData,
        'CertificatesData':CertificatesData,
        'SkillsData':SkillsData,

    }
    return render(request,'index.html',data)

def ProjectHandle(request,myid):
    ProjectDetails=ProjectShow.objects.filter(id=myid)
    ProDetails=ProjectShow.objects.all()
    print(ProDetails)
    return render(request, 'project-detail.html',{'ProjectDetails':ProjectDetails[0]})


class MessageHandler(View):
    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        email_subject="[You have an New message from your portfolio]"
        message=render_to_string('sendmessage.html',{
        
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        
        })
        
        
        email_message= EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,["MadhukarShroti2108@gmail.com"],)
        EmailThread(email_message).start()    
        return redirect("/")


