from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import Predmet, Category
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import *
# # Create your views here.

def index(request):
    return render(request,'index.html' )


def catalog(request, pk=None):
    cat = Category.objects.all()
    if pk:
        predmet = Predmet.objects.filter(category_id=pk)
    else:
        predmet = Predmet.objects.all()
    
    return render(request,'catalog.html',{'predmet':predmet, 'category':cat})
    



@login_required(login_url='vxod')
def cart(request):
    return render(request,'cart.html')


def contact(request):
    return render(request, 'contact.html')  



def vxod(request):
    if request.method == 'GET':
        return render(request,'vxod.html')
    
    else:
        logined_form = LoginForm(request.POST)
        if logined_form.is_valid():
            username = logined_form.cleaned_data['username']
            password = logined_form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('cart')

            return render(request,'vxod.html')



def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        registered_form = Register(request.POST)

        if registered_form.is_valid():
            username = registered_form.cleaned_data['username']
            password = registered_form.cleaned_data['password']
            re_password = registered_form.cleaned_data['re_password']

            if password != re_password:
                return render(request,'register.html')

            User(username=username, password=make_password(password)).save()

            return redirect('vxod')
        print(registered_form)



class TovarDetailView(DetailView):
    model = Predmet
    template_name = 'contact.html'
    context_object_name = 'predmet'



