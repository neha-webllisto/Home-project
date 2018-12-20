from django.shortcuts import render, HttpResponse
from First.models import Home 

# Create your views here.
def my_test(request):
	return render(request, 'Register.html')

def entry(request):
	email=(request.GET['email'])
	pass1=(request.GET['pass'])
	repass=(request.GET['repass'])
	f = Home(email=email,pass1=pass1,repass=repass)
    f.save()
    return render(request,'Register.html)