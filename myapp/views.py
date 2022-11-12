from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user
from django.conf import settings
from django.core.mail import send_mail
import random as r
from datetime import datetime as d



# Create your views here.

def home(req):
 if 'uemail' and 'upassword' in req.session:
  req.session.pop('uemail')
  req.session.pop('upassword')
 print(req.session)
 return render(req,'home.html',{})

def register(req):
 return render(req,'register.html',{})


def signup(req): 
 x=list(user.objects.filter(email=req.POST['email']))
 if(len(x)==0):
  if req.POST['password']!=req.POST['rpassword']:return HttpResponse("Password didn't match..<a href=/RaktKosh/Register>back</a>")
  otp=r.randint(1000,9999)
  send_mail('noreply',str(otp),settings.EMAIL_HOST_USER,[req.POST['email']])
  d={'otp':otp,'name':req.POST['name'],'age':req.POST['age'],'gender':req.POST['gender'],'fathername':req.POST['fathername'],'state':req.POST['state'],'district':req.POST['district'],'pincode':req.POST['pincode'],'address':req.POST['address'],'email':req.POST['email'],'password':req.POST['password'],'number':req.POST['number'],'bloodgroup':req.POST['bloodgroup'],'confirm':req.POST['confirm'],'city':req.POST['city']}
  return render(req,'signup.html',d)
 else:  
  return HttpResponse('Email Already exists..<a href=/RaktKosh/Register>back</a>')

def _signup(req):
 if(req.POST['otp']!=req.POST['votp']):return HttpResponse('invalid otp..<a href=/RaktKosh/Register/SignUp>back</a>')
 user(req.POST['name'],req.POST['age'],req.POST['bloodgroup'],req.POST['gender'],req.POST['fathername'],req.POST['state'],req.POST['district'],req.POST['city'],req.POST['pincode'],req.POST['address'],req.POST['email'],req.POST['password'],req.POST['number'],req.POST['confirm']).save() 
 #user('ketan','21','a+','address','hariomg gupta','alwar','male','hbhj@hgkb','301001','password','a+','yes','1234567890','confirm').save()
 return HttpResponse('Account Successfully Created  <a href=/RaktKosh>SignIn</a>')


def forgot(req):
 return render(req,'forgot.html',{})
 
def _forgot(req):
 uemail=req.POST['uemail']
 print(uemail)
 try:
  l=user.objects.get(email=uemail)
 except BaseException as e:
  print(str(e))
  return HttpResponse('invalid credentials..<a href=/RaktKosh/ForgotPassword>back</a>') 
 send_mail('noreply',l.password,settings.EMAIL_HOST_USER,[uemail])
 html='''Password sent on mail<a href=/RaktKosh>SignIn</a>'''
 return HttpResponse(html) 
 
 
def profile(req):
 if 'uemail' not in req.session:
  req.session['uemail']=req.POST['uemail']
  req.session['upassword']=req.POST['upassword'] 
 email=req.session['uemail']
 l=list(user.objects.filter(email=email))
 password=req.session['upassword']
 if len(l)==0:return HttpResponse("wrong Email or Password <a href='/RaktKosh'>try again</a>")
 return render(req,'profile.html',{'email':email,'password':password,'l':l[0]}) 

def finddonor(req):
 if 'city' in req.POST:
  l=list(user.objects.filter(bloodgroup=req.POST['bloodgroup'],state=req.POST['state'],district=req.POST['district'],city=req.POST['city'],confirm="yes").values())
  print(l)
  #if len(l)==0:  
  #return HttpResponse('No Data Found..<a href="/RaktKosh/FindDonor">back</a>')
  return render(req,'finddonor.html',{'l':l,'bloodgroup':req.POST['bloodgroup'],'state':req.POST['state'],'district':req.POST['district'],'city':req.POST['city'],'b':False})
 return render(req,'finddonor.html',{'b':True}) 

def finddonor1(req):
 if 'city' in req.POST:
  l=list(user.objects.filter(bloodgroup=req.POST['bloodgroup'],state=req.POST['state'],district=req.POST['district'],city=req.POST['city'],confirm="yes").values())
  print(l)
  return render(req,'finddonor1.html',{'l':l,'bloodgroup':req.POST['bloodgroup'],'state':req.POST['state'],'district':req.POST['district'],'city':req.POST['city'],'b':False})
 return render(req,'finddonor1.html',{'b':True}) 
 

def donor(req):
 return render(req,'donor1.html',{})
   

def findnearestbloodbank(req):
 return render(req,'nearbloodbank.html',{}) 

def bloodrequest(req):
 if 'district' in req.POST :
  l=list(user.objects.filter(bloodgroup=req.POST['bloodgroup'],state=req.POST['state'],district=req.POST['district']).values())
  #print(l)
  if len(l)!=0: 
   x=list(map(lambda c:c['email'],l))
   print(x)
   msg='''HELP'''
   send_mail('noreply',msg,settings.EMAIL_HOST_USER,x)
 return render(req,'bloodrequest.html',{})


def update(req):
 user(req.POST['name'],req.POST['age'],req.POST['bloodgroup'],req.POST['gender'],req.POST['fathername'],req.POST['state'],req.POST['district'],req.POST['city'],req.POST['pincode'],req.POST['address'],req.POST['email'],req.POST['password'],req.POST['number'],req.POST['confirm']).save()
 return redirect('/RaktKosh/Profile')
 #return render(req,'profile.html',{'l':list(user.objects.filter(email=req.POST['email']))[0]})
 

 









