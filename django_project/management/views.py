
from django.shortcuts import render,redirect,HttpResponseRedirect# type: ignore
from .models import userdata,Doctorinfo,Patientdetails,Doctorlogin
from django.contrib import messages # type: ignore
# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    if request.method=="POST":
        mail=request.POST.get('inserted_mail')
        pass_word=request.POST.get('inserted_password')
        authorized_user=userdata.objects.filter(email=mail,password=pass_word)
        if authorized_user.exists():
            request.session['email']=mail
            return redirect('/home/')
        else:
            messages.error(request,"check email & password")
        
    return render(request,'login.html')
    

def signup_page(request):
    if request.method=="POST":
        mail=request.POST.get('inserted_mail')
        pass_word=request.POST.get('inserted_password')
        con_pass=request.POST.get('inserted_con_password')
        login_img=request.POST.get('inserted_image')
        authorized_user=userdata.objects.filter(email=mail)
        if authorized_user.exists():
            messages.error(request,"username already taken")
        elif pass_word != con_pass:
             messages.error(request,"check password")
        else:
            userdata.objects.create(email=mail,password=pass_word,login_image=login_img)
        return render(request,'login.html')
 
    return render(request,'signup.html')


def home(request):
    username=request.session['email']
    login=request.session.get('login_image')
    Dc_detail=Doctorinfo.objects.all()
    return render(request,'home.html',{'u_name':username,'profile':login,'Doctors':Dc_detail})

def register(request):
    if request.method=="POST":
        
        name=request.POST.get('inserted_name')
        patname=request.POST.get('inserted_patname')
        age=request.POST.get('inserted_age')
        date=request.POST.get('inserted_date')
        problem=request.POST.get('inserted_problem')
        # authorized_user=Patientdetails.objects.filter(dc_name=name)
        # if authorized_user.exists():
        #     messages.error(request,"Please check our doctor details!")
        # else:
        Patientdetails.objects.create(dc_name=name,patname=patname,age=age,date=date,problem=problem)
        return render(request,'success.html')
    
    return render(request,'register.html')

def patients(request):
    # username=request.session['email']
    Patient_detail=Patientdetails.objects.all()
    return render(request,'patinfo.html',{'Patients':Patient_detail})


def doctorlogin(request):
    if request.method=="POST":
        username=request.POST.get('inserted_username')
        id=request.POST.get('inserted_user_identity')
        authorized_user=Doctorlogin.objects.filter(username=username,identity=id)
        if authorized_user.exists():
            request.session['username']=username
            patient=Patientdetails.objects.filter(dc_name=username)
            return render(request,'patinfo.html',{'particular_pa':patient})
        else:
            messages.error(request,"check username & id ")
        
    return render(request,'doctorlogin.html')

def delete_data(request, id):
    if request.method == 'POST':
        pi = Patientdetails.objects.get(pk=id)
        pi.delete()
    return render(request,'success.html')