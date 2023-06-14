from django.shortcuts import render,redirect
from .models import*
import random
from django.core.mail import send_mail
from django.conf import Settings
import razorpay

# Create your views here.
def index(request):
  if "email" in request.session:

        uid = User.objects.get(email=request.session['email'])
        context ={
            'uid' : uid
        }
        return render(request, "ecomapp/index.html",context)

  else:
    
        return render(request, "ecomapp/login.html")
  
  
  

def login(request):
  if "email" in request.session:
         uid = User.objects.get(email=request.session['email'])
         context = {
             'uid' : uid
         }
         return render(request, "ecomapp/login.html",context)
  try:
         if request.POST:
             email = request.POST['email']
             password = request.POST['password']
            
             uid = User.objects.get(email=email,)
             if uid.password == password:

                 request.session['email'] = uid.email

                 context = {

                     'uid' : uid
                 }

                 return render(request, "ecomapp/index.html",context)
             else:
                 e_msg = "INVALID PASSWORD"
                 context = {

                      "e_msg" : e_msg
                 }
                 return render(request, "ecomapp/login.html",context)
         else:
             return render(request, "ecomapp/login.html")
  except:
          e_msg = "INVALID EMAIL"
         
          context ={
           'e_msg' : e_msg
         }
          return render(request,"ecomapp/login.html",context)

def logout(request):
     if "email" in request.session:
         del request.session["email"]
         return render(request, "ecomapp/login.html")
     else:
  
        return render(request,"ecomapp/login.html")
      
def register(request):
   if request.POST:
         email = request.POST['email']
         password = request.POST['password']
        

         uid = User.objects.create(email=email,
                                   password=password,
                                
                                 )
         context ={
            'uid' :uid
         }

         return render(request, "ecomapp/register.html",context)
   else:
      return render(request,"ecomapp/register.html")
    
def forget_password(request):
  if request.POST:
    email=request.POST['email']
    otp = random.randint(111,999)
    try:
      uid =User.objects.get(email=email)
      uid.otp=otp
      uid.save()
      send_mail ("forgot password", " your otp is" +str(otp), "gohiljayb10@gmail.com",[email])
      

      context ={
        'email' : email
      }
      return render(request,"ecomapp/confirm.html",context)
    
    except:
      p_msg = "INVALID EMAIL"
      
      context = {
        'p_msg' : p_msg
      }
      
      return render (request,"ecomapp/forget_password.html",context)
     
  return render(request,"ecomapp/forget_password.html")

def confirm(request):
  if request.POST:
    email = request.POST['email']
    otp = request.POST['otp']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    
    uid = User.objects.get(email=email)
    if str(uid.otp) == otp:
      if new_password == confirm_password:
        uid.password = new_password
        uid.save()
        
        context ={
          'email' : email
        }
        return render(request, "ecomapp/login.html",context)
      else:
        context ={
          'n_msg' : "INVALID PASSWORD"
        }
        return render(request, "ecomapp/confirm.html",context)
    else:
        
        e_msg = "INVALID OTP"  
        context ={
          'e_msg' : e_msg
        }
        return render(request, "ecomapp/confirm.html",context)
      
  return render(request,"ecomapp/confirm.html")    

def about(request):
  return render(request,"ecomapp/about.html")

def index_2(request):
  return render(request,"ecomapp/index_2.html")

def cart(request):
  cid = Add_to_cart.objects.all()
  context = {
    'cid' : cid
  }
  return render(request,"ecomapp/cart.html",context)

def checkout(request):
  
  
  
  cid = Add_to_cart.objects.all()
  
  lis = []
  sub_total = 0
  total = 1 
  
  for i in cid:
    x = i.price*i.quantity
    lis.append(x)
    sub_total = sum(lis)
    total = sub_total+50
    
    
    amount = total*100 
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({

                                    'amount':amount,
                                   'currency':'INR',
                                   'payment_capture':1
                                   
    })
    print(response,"*******************************")
  
      
  context = {
      'cid' : cid,
      'sub_total' : sub_total,
      'total' : total,
      'response' : response,
     
      
      
      
    }
  return render(request,"ecomapp/checkout.html",context) 




def contact(request):
  if request.POST:
    email = request.POST['email']
    contact = request.POST['contact']
    message = request.POST['message']
    name = request.POST['name']
    subject = request.POST['subject']
    
    
    cid = contact_up.objects.create(
      
                                  email = email,
                                  contact = contact,
                                  message = message,
                                  name = name,
                                  subject = subject

      
    )
    context = {
      
      'cid' : cid
    }
    
    return render (request,"ecomapp/contact.html",context)
  else:
    return render (request,"ecomapp/contact.html")


def news(request):
  return render(request,"ecomapp/news.html")

def shop(request):
  uid = Add_products.objects.all()
  context = {
    'uid': uid
  }
  return render(request,"ecomapp/shop.html",context)

def add_to_cart(request,id):
  if  'email' in request.session:
    
    uid = User.objects.get(email= request.session['email'])
    pid = Add_products.objects.get(id=id)
    
    cid = Add_to_cart.objects.create(user_id = uid,
                                     product_id = pid,
                                     name = pid.name,
                                     price  = pid.price,
                                     pic = pid.pic,
                                     total_price = pid.price*pid.quantity
                                     
                                     
                                     )
    return redirect('cart')
     
def remove(remove,id):
   
  did = Add_to_cart.objects.get(id=id)
  
  did.delete()
  return redirect('cart')
  
def cart_minus(request,id):
  
  cid = Add_to_cart.objects.get(id=id)
  
  if cid.quantity == 1:
    cid.delete()
    return redirect ('cart')
  else:
    if cid:
      
      cid.quantity = cid.quantity-1
      cid.total_price = cid.quantity*cid.price
      cid.save()
      return redirect('cart')
      
def cart_plus(request,id):
  
  cid = Add_to_cart.objects.get(id=id)
 
  
  if cid:
    cid.quantity = cid.quantity+1
    cid.total_price = cid.quantity * cid.price
   
    cid.save()
    
    
    return redirect ('cart')
  
  
  

   
  