from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
	return HttpResponse("<h1 style='background-color:black;color:white'>Hello Good Morning to All</h1>"+"<br>"+"<script>alert('Hello welcome')</script>")

def roll(req,rl):
	return HttpResponse("Your Roll number is: "+str(rl))

def emp(req,i,na,sl):
	return HttpResponse("Your Id is: {} <br> Your name is: {} <br> Your salary is: {}".format(i,na,sl))

def person(request,name,roll):
	return render(request,'myApp/sample.html',{'r':name,'t':roll})

def student(request,i,n,a):
	return render(request,'myApp/student.html',{'id':i,'name':n,'age':a})