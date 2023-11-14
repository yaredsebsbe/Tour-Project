from django.shortcuts import render,redirect
from .models import Package,Guide
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

#home
def home(request):
    return render(request,'index.html')

#package list
def package(request):
    packages=Package.objects.all()
    context={'packages': packages}

    return render(request,'package.html',context)

#creating a package
def create_package(request):
    if request.method=='POST':
        pname=request.POST['pname']
        plocation=request.POST['plocation']
        pfeature=request.POST['pfeature']
        pprice=request.POST['pprice']
        pimage=request.FILES['img']
        pdesc=request.POST['description']
        creator=request.session.get('gid')
        if len(pimage)!=0:
            Package.objects.create(packageName=pname,packageFeature=pfeature,packageLocation=plocation,packagePrice=pprice,packageImage=pimage,packageDescription=pdesc,creator_id=creator)
            return redirect('/')
        else:
            Package.objects.create(packageName=pname,packageFeature=pfeature,packageLocation=plocation,packagePrice=pprice,packageDescription=pdesc,creator_id=creator)
            return redirect('/')
    else:
        return render(request,'create_package.html')


#search
def search(request):
    if request.method=='POST':
        searchInp=request.POST['search']
        searched=Package.objects.filter(packageName=searchInp)
        context={'searched': searched}
        return render(request,'search.html',context)


#guides list    
def guides(request):
    guides=Guide.objects.all()
    context={'guides':guides}
    return render(request,'guides.html',context)


#guide register
def guideReg(request):
    if request.method=='POST':
        gfname=request.POST['gfname']
        glname=request.POST['glname']
        gqual=request.POST['gqual']
        gphone=request.POST['gphone']
        gemail=request.POST['gemail']
        gpass=request.POST['gpass']
        gimage=request.FILES['gimg']
        if len(gimage)!=0:

            Guide.objects.create(guideFname=gfname,guideLname=glname,guideQualification=gqual,guidePhone=gphone,guidePic=gimage,guideEmail=gemail,guidePassword=gpass)
            request.session['gemail']=gemail
            return redirect('/forget_q')
        else:
            Guide.objects.create(guideFname=gfname,guideLname=glname,guideQualification=gqual,guidePhone=gphone,guideEmail=gemail,guidePassword=gpass)
            return redirect('/createPackage')
    else:
        return render(request, 'guide_register.html')


#guide login
def guideLog(request):
    if request.method=='POST':
        userInp=request.POST['ginp']
        userPas=request.POST['gpass']
        try:
            user=Guide.objects.get(Q(guideEmail=userInp) | Q(guidePhone=userInp))
            if user.guidePassword == userPas:
                request.session.clear()
                request.session['gid']=user.id
                request.session['gname']=user.guideFname
                
                return redirect('/')
        except ObjectDoesNotExist:
            return redirect('guideLog')
    return render(request,'guide_login.html')


#guide verification Q&A
def guideV(request):
    if request.method == 'POST':
        email=request.session.get('gemail')
        question=request.POST['question']
        answer=request.POST['answer']
        Guide.objects.filter(guideEmail=email).update(forQuestion=question, forAnswer=answer)
        return redirect('guideLog')

    return render(request,'forget_q.html')


#guide Forget password
def guideForget(request):
    if request.method == 'POST':
        gemail=request.POST['gemail']
        gquest=request.POST.get('question')
        ganswer=request.POST['answer']

        if len(gemail) > 0 and len(gquest) > 0 and len(ganswer)>0:
        
            try:
                user=Guide.objects.get(guideEmail=gemail)
                if quest == gquest and ans == ganswer:
                    quest=user.forQuestion
                    ans=user.forAnswer
                    return redirect('createPackage')
                else:
                    return redirect('guideForget')
            except ObjectDoesNotExist:
                return redirect('guideForget')   
        else:
            return redirect('guideForget')
        
    return render(request,'gforget.html')
    

#deleter
def deleter(request):
    if request.method=="POST":
        id=request.POST['del']
        try:
            user=Guide.objects.get(id=id)
            user.delete()
            return redirect('deleter')
        except Guide.DoesNotExist:
            return redirect('deleter')
    return render(request,'deleter.html')

#logout
def logout(request):
    request.session.clear()
    return redirect('/')


#list of package for guide
def list_package(request):
    packages=Package.objects.filter(creator_id=request.session.get('gid'))
    context={'packages':packages}
    return render(request,'listPackages.html',context)

def redirLog(request):
    return render(request,'redirLog.html')


def redirSign(request):
    return render(request,'redirSign.html')

def booked(request):
    return render(request,'booked.html')

def book(request):
    if request.session.get('tid'):
        return render(request,'book.html')
    else:
        return render(request,'userLogin.html')
    