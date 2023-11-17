from django.shortcuts import render, redirect,get_object_or_404
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user, allowed_users,realtors_only
from django.contrib.auth.models import Group
from .forms import ListForm, CreateUserForm, RealtorForm
from . filters import PropertyFilter

from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

from django.core.paginator import Paginator

# Create your views here.




   




@unauthenticated_user
def registrationPage(request):
    
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")
                
                #group = Group.objects.get(name = "realtor")
                #user.groups.add(group)
                #Realtor.objects.create(user=user)
                
                messages.success = (request, "Account was created for" + username)
                
                return redirect("login")
                
    else:
            form = CreateUserForm()      
            
    context = {"form":form}
    return render(request,'realestate/register.html',context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request,user)
            return redirect('agent')
        
        else:
            messages.info(request, 'Username or Password is Incorrect')
            
    
    context = {}
    return render(request,'realestate/login.html',context)
    
    
    
    
def logoutUser(request):  
    logout(request)
    return redirect('home')


@allowed_users(allowed_roles=["realtor","admin"])
def userPage(request): 
    user = request.user
    realtor = user.realtor
    
    
    form = RealtorForm(instance=realtor) 
    
    if request.method== "POST":
        form = RealtorForm(request.POST,request.FILES, instance=realtor)
        if form.is_valid():
            form.save()
            return redirect("agent")


    context ={"form":form}
    return render(request,'realestate/user.html',context)
    






def index(request):
    
    properties = Property.objects.all()[2:6]
    
    #myFilter = PropertyFilter(request.GET,queryset = properties)
    #properties = myFilter.qs
    
    
    context = {
        
        "properties":properties,
        #"myFilter": myFilter
        
        
    }
    return render(request,'realestate/index.html',context)
 



def about_us(request):
    return render(request,'realestate/about.html')




def blog(request):
    
    return render(request,'realestate/blog-grid.html')



def blogSingle(request):
    
    return render(request,'realestate/blog-single.html')



def property(request):
    properties = Property.objects.all()
    properties_count = properties.count()
    myFilter = PropertyFilter(request.GET, queryset = properties )
    properties = myFilter.qs
    
    #set patination
    p = Paginator(Property.objects.all(), 6)
    page_list = request.GET.get('page')
    page =p.get_page(page_list)
    
    context ={
        "properties":properties,
        "properties_count": properties_count,
        "myFilter": myFilter,
        "page": page
    }
    
    return render(request,'realestate/property-grid.html',context)






def propertySingle(request,pk):
    
    propertyy = Property.objects.get(id = pk)
    
    
    context = {
        "propertyy":propertyy,
        
    }
   
    return render(request,'realestate/property-single.html',context)


    

def contact(request):
    return render(request,'realestate/contact.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=["realtor","admin"])
def agentSingle(request):
    
    current_user = request.user
    
    current_realtor = get_object_or_404(Realtor, user = current_user)
    
    properties =current_realtor.properties.all()
    
    properties_count = properties.count()
    
    context = {
        "current_realtor":current_realtor,
        "properties":properties,
        "properties_count":properties_count,
         
    }
    
    return render(request,'realestate/agent-single.html',context)


    
@login_required(login_url='login')  
def agent(request):
    return render(request,'realestate/agents-grid.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=["realtor","admin"])
def createListing(request):
    
    realtor = request.user.realtor
    
    print("REALTOR IS:", realtor)
    
    form = ListForm(initial={"realtor":realtor})
   
    
    
    if request.method =="POST":
        
        form = ListForm(request.POST,request.FILES)
        print("Form ni :",form)
        
        if form.is_valid():
            form.save()
            return redirect("agent")
    
    context = {
            "form": form
              }
    return render(request,'realestate/list_form.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=["realtor","admin"])
def updateListing(request,pk):
    
    
    current_user = request.user
    
    
   
    
    current_realtor = get_object_or_404(Realtor, user = current_user)
    propertyy =current_realtor.properties.get(id=pk)
    
    
    
    form = ListForm(instance = propertyy)
    if request.method =="POST":
        form = ListForm(request.POST,request.FILES, instance=propertyy)
        if form.is_valid():
            form.save()
            return redirect("agent")
        
    context = {
       "form": form
    }
    return render(request,'realestate/list_form.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=["realtor","admin"])
def deleteProperty(request, pk):
    
    current_user = request.user
    
    
   
    
    current_realtor = get_object_or_404(Realtor, user = current_user)
    property =current_realtor.properties.get(id=pk)
    
    
    
    if request.method =="POST":
        property.delete()
        return redirect("agent")
        
    context ={
        "property":property,
        "current_user":current_user,
        }
    return render(request,'realestate/delete.html',context)



def mpesa(request):
    
    current_user = request.user
    
    current_realtor = get_object_or_404(Realtor, user = current_user)
    
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = 'current_realtor.phone_no'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    #transaction_desc = 'pay 50 shs to abode to list your property'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)




    

