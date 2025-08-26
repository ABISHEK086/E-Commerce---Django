from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json


def demoPage(request):
    return HttpResponse("demo Page")

def demoPageTemplate(request):
    return render(request,"demo.html")

def adminLogin(request):
    return render(request,"admin_templates/signin.html")

def adminLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("admin_login"))

def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successfully!")
    return HttpResponseRedirect(reverse("admin_login"))

def admin_home(request):
    return render(request, "admin_templates/dashboard.html")

@csrf_exempt
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        try:
            request.user.profile_picture = request.FILES['profile_picture']
            request.user.save()
            return JsonResponse({'success': True, 'message': 'Profile picture updated successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'No file provided'})

@csrf_exempt
def save_system_settings(request):
    if request.method == 'POST':
        try:
            return JsonResponse({'success': True, 'message': 'System settings saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
def update_features(request):
    if request.method == 'POST':
        try:
            return JsonResponse({'success': True, 'message': 'Feature settings updated successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
def update_password(request):
    if request.method == 'POST':
        try:
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            
           
            if new_password != confirm_password:
                return JsonResponse({'success': False, 'error': 'New password and confirm password do not match!'})
            
           
            if not request.user.check_password(current_password):
                return JsonResponse({'success': False, 'error': 'Current password is incorrect!'})
            
            
            if len(new_password) < 8:
                return JsonResponse({'success': False, 'error': 'Password must be at least 8 characters long!'})
            
            
            request.user.set_password(new_password)
            request.user.save()
            
            
            update_session_auth_hash(request, request.user)
            
            return JsonResponse({'success': True, 'message': 'Password updated successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
def save_security_settings(request):
    if request.method == 'POST':
        try:
            # Process security settings here
            # two_factor_auth = request.POST.get('two_factor_auth')
            # session_timeout = request.POST.get('session_timeout')
            return JsonResponse({'success': True, 'message': 'Security settings saved successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
