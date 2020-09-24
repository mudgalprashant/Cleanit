from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile,Drives
from .forms import NewUserForm
import json

def home(request):
	return render(request, 'home.html')
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.success(request, f'logged in as {username}')
			return redirect('home-page')
		else:
			messages.info(request, "Invalid user credentials")
			return render(request, 'login.html')

	else:
		messages.success(request, 'Login to explore more!')
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	messages.success(request, 'Logged out Successfully!!')
	return redirect('home-page')

def register(request):
	if request.method=='POST':

		form=NewUserForm(request.POST)
	
		
		name=request.POST.get('username')		
		email=request.POST.get('email')
		password=request.POST.get('loginpsw')
		confirm_psw=request.POST.get('confirmpsw')
		if User.objects.filter(username=name).exists():
			messages.error(request,"Username already exists!!")
			return redirect('sigup-page')
		elif User.objects.filter(email=email).exists():
			messages.error(request,"Email already exists!!")
			return redirect('sigup-page')
		elif password!=confirm_psw:
			messages.error(request,"Password and confirm password are different :(")
			return redirect('signup-page')
		elif len(password)<8:
			messages.info(request, "Password too short!!")
		else:
			user=User.objects.create_user(name,email,password)
			user.save()
			user_info = Profile(username=name, email = email)
			user_info.save()
			messages.info(request, f'Successfully created account for {name}!!')
			return redirect('home-page');
					
	else:		
	    form=NewUserForm()
	return render(request,'register.html',{'form':form})
			

def profile(request):
	info = Profile.objects.filter(username = request.user.username).first()
	return render(request, 'profile.html',{'info':info})
	
def myContribution(request):
	user = request.user.username
	drives = Drives.objects.filter(creator = user)
	return render(request, 'myContribution.html', {'drives':drives, 'user':user})

def edit(request):
	user = request.user
	profile = Profile.objects.filter(username = user.username).first()
	if request.method == 'POST':
		email = request.POST.get('email')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		address = request.POST.get('address')
		profession = request.POST.get('profession')
		contact = request.POST.get('contact')
		img =  request.POST.get('img')
		name = request.POST.get('name')
		if email:
			if User.objects.filter(email= email).exists():
				messages.info(request, 'Email Already Taken!!')
				return render(request, 'edit.html', {'user':profile})
			else:
				profile.email = email
		if age:
			profile.age=age
		if gender:
			profile.gender = gender.capitalize()
		if address:
			new_add = [part.capitalize() for part in address.split()]
			address = " ".join(new_add)
			profile.address = address
		if profession:
			profile.profession = profession
		if contact:
			profile.contact = contact
		if img:
			profile.img = img
		if name:
			profile.name = name
		profile.save()
		info = Profile.objects.filter(username = request.user.username).first()
		return render(request, 'profile.html',{'info':info})
			


	else:
		return render(request, 'edit.html', {'user':profile})

def create_team(request):
	print(request.user)
	if request.user:
		if request.method == 'POST':
			name = request.POST['teamname'],
			city = request.POST['city'],
			place = request.POST['venue'],
			date = request.POST['date'],
			details = request.POST['body'],
			if Drives.objects.filter(name = name).exists():
				info.messages(request, 'Drive name taken')
				return render(request, 'create.html')
			this_place_drives = Drives.objects.filter(place=place).all()
			for drive in this_place_drives:
				if drive.city == this.city.capitalize():
					if abs(drive.date-date)<=28:
						messages.info(request, 'Sorry! A drive already exist for same place within 4 weeks!!')
						return render(request, 'create.html')

			

			Drives.objects.create(creator = request.user,
								name = request.POST['teamname'],
								city = request.POST['city'],
								place = request.POST['venue'],
								date = request.POST['date'],
								details = request.POST['body'],
				)

			
			messages.info(request, 'Drive initiated Successfully!!')
			return render(request, 'home.html')
		else:
			return render(request, 'create.html')
	else:
		return render(request, 'create.html')

def join(request):
	return render(request, 'join.html')