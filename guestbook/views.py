from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	msg = 'my name is cdecide'
	return render(request,'hello.html',{'message':msg})