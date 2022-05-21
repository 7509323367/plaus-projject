from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.views import View
from .models import Job
from .models import Candidate
from .models import Registration
from .models import Fupload
from .models import portpho
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView
from django.urls import reverse


def job(request):
    if (request.session.has_key("uid")):
        suid=request.session["uid"]
        data1 = Job.objects.all()
        return render(request,"plus/job.html",{"res":"data inserted succesfully","d":data1})
    else:
        return redirect("login")
    
def candidate(request):
    if (request.session.has_key('uid')):
        suid=request.session['uid']
        job = Job.objects.all()
        if request.method=="POST":
            s = Candidate(email =request.POST["txtemail"],jobid=request.POST["ddljob"],applydate=request.POST["applydate"],
            cname=request.POST["txtcandidate"])
            s.save()
            return render(request,"plus/candidate.html",{"res":job,"msg":"data inserted successsfully"})
        return render(request,"plus/candidate.html",{"res":job,"jid":int(request.GET["q"])})    

def registration(request):
    Qulification=["10th","12th","diploma","graduation","post graduation"]
    if request.method=="POST":
        r = Registration(email=request.POST["email"],password=request.POST["password"],
        mobileno =request.POST["mobileno"],technology=request.POST["technology"],
        candidatetype=request.POST["candidatetype"],higherquli=request.POST["education"])
        r.save()
        return render(request,"plus/registration.html",{"data": Qulification,"data1":"registration successsfully"})
    return render(request,"plus/registration.html",{"data":Qulification})

def login(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session['uid']=request.POST["email"]
            if request.POST["chk"]:
                res= HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location'] ='job'
                return res
            else:
                return render(request,"plus/login.html",{"res":"invalid user id password"})
    else:
        c1=""
        c2=""
        if request.COOKIES.get('ukey'):
          c1=request.COOKIES["ukey"]
          c2=request.COOKIES["upass"]
    return render(request,"plus/login.html",{"email":c1,"password":c2})

def logout(request):
   res = HttpResponse(status=302)
   res.delete_cookie('ukey',"/")
   res.delete_cookie('upass',"/")
   del request.session["uid"]
   res['Location']='login'
   return res 

def Home(request): 
    return render(request,"plus/Home.html")


def scookie(request):
    response = HttpResponse("cookise has been set")
    response.set_cookie('ckey','hello')
    return response

def gcookie(request):
    a = request.COOKIES['ckey']
    return HttpResponse("value is" +str(a))

def fileuplod(request):
    if request.method=="POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        furl = Fupload(filepath=filename)
        furl .save()
        furl = fs.url(filename)
        return render(request, 'plus/fileuplod.html',{'furl':Fupload.objects.all()})
    return render(request,'plus/fileuplod.html',{'furl':Fupload.objects.all()}) 

def port(request):
    if request.method=="POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        furl = portpho(filepath=filename,filetype=filename)
        furl.save()
        furl = fs.url(filename)
        return render(request,"plus/portpho1.html",{"furl":portpho.objects.all()})
    return render(request,"plus/portpho1.html",{"furl":portpho.objects.all()}) 


class UploadView(View):
    def get(self,request):
        return render(request,"plus/portpho1.html",{"furl":Fupload.objects.all()})
    def post (self,request):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj = Fupload(filepath=filename)
        obj.save()
        furl = fs.url(filename)
        return render(request,"plus/portpho1.html",{"furl":Fupload.objects.all()})


class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdiscription']

    def get_success_url(self):
        return reverse('login')





