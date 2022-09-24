from django.shortcuts import render,redirect
from .models import user_detail
# Create your views here.

def signup(request):
	return render(request,'signup.html')
def login(request):
	if request.session.get('user'):
		return redirect('dashboard')
	else:
		return render(request,'login.html')
def logout(request):
	del request.session['user']
	return redirect('login')

def register(request):
	fname=request.POST['fname']
	mname=request.POST['mname']
	lname=request.POST['lname']
	gender=request.POST['gender']
	email=request.POST['email']
	mobile=request.POST['mobile']
	password=request.POST['password']
	rpassword=request.POST['rpassword']

	if password!=rpassword:
		return render(request,'signup.html',{'error':'Password Does Not matched'})
	else:
		if len(user_detail.objects.filter(email=email))==1:
			return render(request,'signup.html',{'error':'Email is already exist'})
		else:
			res=user_detail(fname=fname,mname=mname,lname=lname,email=email,mobile=mobile,password=password,gender=gender,salary="0")
			res.save()
			request.session['user']=email
			return redirect('dashboard')


def authenticate_user(request):
	email=request.POST['email']
	password=request.POST['password']
	if len(user_detail.objects.filter(email=email,password=password))==1:
		request.session['user']=email
		return redirect('dashboard')
	else:
		return render(request,"login.html",{'error':'Email or Password is Incorrect'})
def update_profile(request):
	if request.session.get('user'):
		fname=request.POST['fname']
		mname=request.POST['mname']
		lname=request.POST['lname']
		gender=request.POST['gender']
		email=request.POST['email']
		mobile=request.POST['mobile']
		salary=request.POST['salary']
		if request.session.get('user')==email:
			data=user_detail.objects.get(email=email)
			data.fname=fname
			data.lname=lname
			data.mname=mname
			data.gender=gender
			data.mobile=mobile
			data.salary=salary
			data.save()
			request.session['error']="Profile Upadted Successfully."
			return redirect('myprofile')
	else:
		return redirect('login')

def change_password(request):
	if request.session.get('user'):
		return render(request,"change_password.html")
	else:
		return redirect('login')
def updating_password(request):
	if request.session.get('user'):
		password=request.POST['password']
		rpassword=request.POST['rpassword']
		if password==rpassword:
			email=request.session.get('user')
			data=user_detail.objects.get(email=email)
			data.password=password
			data.save()
			del request.session['user']
			return render(request,"processing.html")
		else:
			return render(request,"change_password.html",{'error':'Oops! Both password does not matched.'})
	else:
		return redirect('login')

