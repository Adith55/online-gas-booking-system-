from django.shortcuts import render, redirect,HttpResponse
from .models import User
from .models import Booking
from .models import Employees
from .models import Profile
from django.contrib import messages
from .forms import Employeeform
from twilio.rest import Client

# Create your views here.
def main(request):
    return render(request,"index.html")

def new_connection(request):
    return render(request,"new_connection.html")

def book_cylinder(request):
    return render(request,"book_cylinder.html")

def signup(request):
    sname=request.POST.get("logname")
    semail=request.POST.get("logemail")
    spass=request.POST.get("logpass")
    user_obj=User(name=sname,email=semail,password=spass)
    user_obj.save()
    messages.success(request,"User Created Succesfully")
    return redirect('home')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('logpass')
        user = User.objects.filter(email=email).first()
        if user is not None:
            if password == user.password:
                messages.success(request,"Login Succesfully")
                request.session['email'] = email
                return redirect('dashboard')
            else:
                messages.error(request, "Password Doesnt Match")
                return redirect('home')


        else:
            messages.error(request, "User Doesnt Exist")
            return redirect('home')
    elif request.method == "GET":
        return render(request, "index.html")
    
def logout(request):
    request.session.clear()
    return redirect("/")


def dashboard(request):
    if request.method == "GET":
        return render(request, 'dashboard.html')

def book_cylinder(request):
    if request.method =='POST':
        Name=request.POST.get('customerName')
        Number=request.POST.get('contactNumber')
        Address=request.POST.get('deliveryAddress')
        cylinder=request.POST.get('cylinderType')
        n_quantity=request.POST.get('quantity')
        Booking.objects.create(customerName=Name,contactNumber=Number,deliveryAddress=Address,cylinderType=cylinder,quantity=n_quantity)
        # return redirect('booking_histroy')
    return render(request,"book_cylinder.html")

def booking_histroy(request):
    email=request.session.get('email')
    user=User.objects.filter(email=email).first()
    if user:
        name=user.name
        bookings=Booking.objects.filter(customerName=name)
        return render(request,'booking_histroy.html' , {'bookings':bookings})
    else:
        return redirect('home')

########################### ADMIN ############################   

def create_admin(request):
    try:
        obj = User(email="admin@gmail.com" , password="admin5" , role="admin")
        obj.save()
    except:
        print("email or password error")

    return redirect('/')


def admin_login(request):
     
     if request.method =="POST":
        print('hh')
        email = request.POST.get('email')
        password = request.POST.get('logpass')
        print(email,password)
        user = User.objects.get(email=email)
        if user is not None:
           
            if user.password and user.password == password and user.role == 'admin':
                print('not none')
                return render(request,'admin_base.html')
            else:

                response =f"""
                            <script>
                            window.alert('wrong username and password')
                            window.location.href = '/admin_login/';
                            </script>
                            """
                return HttpResponse(response)
            
        else:
            response =f"""
                            <script>
                            window.alert('no user found')
                            window.location.href = '/admin_login/';
                            </script>
                            """


         
     
     return render(request,"admin_login.html")
    

def admin_base(request):
    return render(request,"admin_base.html")

def admin_users(request):
    user=User.objects.all()
    return render(request,"admin_users.html",{'user':user})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    user=User.objects.all()
    return render(request,"admin_users.html",{'user':user})

def admin_adduser(request):
    if request.method == "GET":
        return render(request,'admin_adduser.html')

    elif request.method == "POST":

        sname=request.POST.get("logname")
        semail=request.POST.get("logemail")
        spass=request.POST.get("logpass")
        srole=request.POST.get("role")
       

        user_obj=User(name=sname,email=semail,password=spass,role=srole)
        user_obj.save()
        user=User.objects.all()
        return render(request,"admin_users.html",{'user':user})
    

def employee_list(request):
    context= {'employee_list':Employees.objects.all()}
    return render(request,"employee_list.html",context)

def employee_form(request):
    if request.method =="GET":

        form = Employeeform()
        return render(request,"employee_add.html",{"form":form})
    else:
        form = Employeeform(request.method=="POST")
        if form.is_valid():
            form.save()
        return redirect("/employee_list")

def employee_delete(request,empCode):
    employee=Employees.objects.get(empCode = empCode)
    employee.delete()
    # context=Employees.objects.all()
    return redirect('employee_list')

def bookings(request):
    bookings=Booking.objects.all()
    return render(request,'bookings.html',{'bookings':bookings})
    

def approve(request,number):
    account_sid = 'AC02c946558d693b23cab9182fa8276222'
    auth_token = '456b39efb9cfbd1dc1fe608500414bd2'
    client = Client(account_sid, auth_token)

   
    user_phone_number = f" +91{number}" 
    print("Number ", user_phone_number) # Replace with the user's phone number
    message = client.messages.create(
        body='YOUR ORDER IS APPROVED WILL BE DELIVERED IN 1-2 DAYS THANKYOU E-FLARE',
        from_='+12403802761',
        to=user_phone_number
    )

    return render(request, 'bookings.html',{'message': message.body})

def reject(request ,number):
    account_sid = 'AC02c946558d693b23cab9182fa8276222'
    auth_token = '456b39efb9cfbd1dc1fe608500414bd2'
    client = Client(account_sid, auth_token)

    user_phone_number = f" +91{number}"  # Replace with the user's phone number
    message = client.messages.create(
        body='YOUR ORDER IS REJECTED...THANKYOU E-FLARE',
        from_='+12403802761',
        to=user_phone_number
    )
    return render(request, 'bookings.html',{'message': message.body})
def profile(request):
    if request.method == "POST":
        pname=request.POST["profilename"]
        print(pname)
        pemail=request.POST.get("profileemail")
        pdob=request.POST.get("profiledob")
        pmarital_status=request.POST.get("profilemarital_status")
        paddress=request.POST.get("profileaddress")
        pdocument=request.POST.get("profiledocument")
        data=Profile(name=pname,email=pemail,dob=pdob,marital_status=pmarital_status,address=paddress,document=pdocument)
        data.save()
    email=request.session['email']
    print(email)
    daa=Profile.objects.get(email=email)
    



    return render(request,'profile.html',{'daa':daa})

