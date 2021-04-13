from django.shortcuts import render,redirect, HttpResponse
from django.db import models 
from user_login_app.models import User


# Create your views here.
def index(request):
    context={
        'user':User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'index.html',context)

def log_out(request):
    if 'email' in request.session:
        del request.session['email']
    elif 'first_name' in request.session:
        del request.session['first_name']
    return redirect('/')



