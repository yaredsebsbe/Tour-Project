from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

def userReg(request):
    if request.method=='POST':
        uname=request.POST['uUname']
        passw=request.POST['uPassw']
        email=request.POST['uEmail']
        user=User.objects.create_user(username=uname, password=passw,email=email)
        return redirect('/')
    return render(request,'userReg.html')
def ulogin(request):
    if request.method=='POST':
        uname=request.POST['uUname']
        passw=request.POST['uPassw']
        user = auth.authenticate(request, username=uname, password=passw)
        if user is not None:
            auth.login(request,user)
            request.session.clear()
            request.session['tid']=user.id
            request.session['tuser']=user.username
            return redirect("/")
        else:
            return redirect("userLogin")
    return render(request,'userLogin.html')

