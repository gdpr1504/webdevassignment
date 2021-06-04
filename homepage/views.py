from django.http.response import HttpResponse
from django.shortcuts import render
from homepage.models import login,record
def create_record(request,username):
    if(request.method=="POST"):
        records=record(emp_id=request.POST['emp_id'],emp_name=request.POST['emp_name'],designation=request.POST['designation'],salary=request.POST['salary'],city=request.POST['city'])
        records.save()
        rec=record.objects.all()
        return render(request,'home.html',{'rec':rec,'user1':username})
    else:
        return render(request,'createrec.html',{'user1':username})

def delete_record(request,id,username):
    rec=record.objects.get(emp_id=id)
    rec.delete()
    rec=record.objects.all()
    return render(request,'home.html',{'user1':username,'rec':rec})

def update_record(request,id,username):
    rec=record.objects.get(emp_id=id)
    if(request.method=="POST"):
        rec.delete()
        records=record(emp_id=id,emp_name=request.POST['emp_name'],designation=request.POST['designation'],salary=request.POST['salary'],city=request.POST['city'])
        records.save()
        rec1=record.objects.all()
        return render(request,'home.html',{'rec':rec1,'user1':username}) 
    else:
        return render(request,'update.html',{'user1':username,'rec':rec})


def homepage(request):
    rec=record.objects.all()
    return render(request,'home.html',{'rec':rec})
def loginpage(request):
    if (request.method)=="POST":
        username=request.POST['Username']
        password =request.POST['pwd']
        log=login.objects.all()
        for i in log:
            if(username==i.username):
                if(password==i.password):
                    rec=record.objects.all()
                    return render(request,'home.html',{'user1':username,'rec':rec})
                else:
                    return render(request,'login.html',{'data':'Invalid Credentials!'})
        else:
            return render(request,'login.html',{'data':'User Not Found!'})
    else:
        return render(request,'login.html')