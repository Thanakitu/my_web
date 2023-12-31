from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from wed_users.forms import  RegisterForm
from wed_users.models import CustomUser
from django.http import HttpRequest, HttpResponseRedirect
from wed_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm
from wed_users.utils.activation_token_generator import activation_token_generator
# Create your views here.
def register(request: HttpRequest):
    #POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
          user: CustomUser = form.save(commit=False)
          user.is_active = False
          user.save()
          
          context = {
                "protocol": request.scheme,
                "host": request.get_host(),
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user),
            }
          
          email_body = render_to_string(
                "wed_users/activate_email.html", context=context
            )
          
            #login(request, user)
          email = EmailMessage(
                to=[user.email],
                subject="Activate account หน่อยครับ",
                body=email_body
            )
          email.send()
          
          
           
          return HttpResponseRedirect(reverse("register_thankyou"))
    else:
        form = RegisterForm()
        
    #GET
    context = {"form": form}
    return render(request, "wed_users/register.html",context)    
        
def register_thankyou(request:HttpRequest):
    return render(request, "wed_users/register_thankyou.html")           
            
def activate(request: HttpRequest, uidb64: str, token: str):
    title = "Activate account เรียบร้อย"
    content = "คุณสามารถเข้าสู่ระบบได้เลย"
    id = urlsafe_base64_decode(uidb64).decode()
    try:
        user = CustomUser.objects.get(id=id)
        if not activation_token_generator.check_token(user,token):
            raise Exception("Check token false")
        user.is_active = True
        user.save()
    except:
        print("Activate ไม่ผ่าน")
        title = "Activate account ไม่ผ่าน"
        content = "ลิ้งค์ไม่ถูกต้อง หรือหมดอายุไปแล้ว"
        
    context = {"title": title, "content": content} 
    return render(request,"wed_users/activate.html",context)

@login_required
def dashboard(request: HttpRequest):
    favorite_location_pivots = request.user.favorite_location_pivot_set.order_by("-level")
    context = {"favorite_location_pivots": favorite_location_pivots}
    return render(request, "wed_users/dashboard.html",context)

@login_required
def profile(request: HttpRequest):
    user = request.user
    #POST
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            extended_form = ExtendedProfileForm(request.POST)
            is_new_profile = True
        
        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
               profile = extended_form.save(commit=False)
               profile.user = user
               profile.save()
            else:
                extended_form.save()
                
            response = HttpResponseRedirect(reverse("profile"))
            response.set_cookie("is_saved", "1")
            return response
    else: 
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:     
            extended_form = ExtendedProfileForm()
                      
    #GET      
    is_saved = request.COOKIES.get("is_saved") == "1"
    flash_message = "บันทึกเรียบร้อย" if is_saved else None  
    context = {
        "form": form,
        "extended_form": extended_form,
        "flash_message": flash_message,
    }
    response = render(request, "wed_users/profile.html", context)
    if is_saved:
        response.delete_cookie("is_saved")
    return response
