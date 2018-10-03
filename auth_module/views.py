from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from auth_module.forms import SignUpForm, GetEmailForm
from ecommarce.slider_Model import GetEmail


# Create Account.


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'auth/registration.html', {'form': form})


def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get("username")
            password = request.POST.get("pwd")

            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')

    return render(request, 'auth/login.html')


def getlogout(request):
    logout(request)
    return redirect('login')


#
# def addCustomer(request):
#     if request.user.is_authenticated:
#         u = get_object_or_404(User, id=request.user.id)
#         cust = get_object_or_404(Customer, name=u)
#         if cust:
#             form = CustomerForm(request.POST or None, request.FILES or None, instance=cust)
#         else:
#             form = CustomerForm(request.POST or None, request.FILES or None)
#
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.name = u
#             instance.save()
#             return redirect('index')
#
#         return render(request, 'coustomer_reg.html', {'form': form})
#     else:
#         return redirect('registration')
def get_email(request):
    if request.method == 'POST':
        form = GetEmailForm(request.POST)
        if form.is_valid():
            obj = GetEmail()  # gets new object
            obj.email = form.cleaned_data['email']
            obj.save()
            return redirect('index')
    return redirect('index')
