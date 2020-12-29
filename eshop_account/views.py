from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render,redirect
from .forms import loginForm, registerForm, EditForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')

    login_form = loginForm(request.POST or None)
    context = {
        'login_form':login_form
    }
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=user_name , password=password)
        if user is not None:
            login(request,user)
            context['login_form'] = loginForm
            return redirect('/')
        else:
            login_form.add_error('user_name' ,'نامی با این نام کاربری وجود ندارد')

    return render(request,'account/login.html' , context)

def register_user(request):

    if request.user.is_authenticated:
        return redirect('/')

    register_form = registerForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=user_name,password=password,email=email)
        return redirect('/login')

    context = {
        'register_form':register_form
    }
    return render(request, 'account/register.html', context)

@login_required(login_url='/login')
def user(request):
    user_id = request.user.id
    user = User.objects.filter(id=user_id).first()
    return render(request, 'account/user.html', {'user':user})

@login_required(login_url='/login')
def user_edit(request):
    user_id = request.user.id
    user: User = User.objects.filter(id=user_id).first()
    editForm = EditForm(request.POST or None, initial={'firstName':user.first_name, 'lastName':user.last_name})
    if editForm.is_valid():
        user.first_name = editForm.cleaned_data.get('firstName')
        user.last_name = editForm.cleaned_data.get('lastName')
        user.set_password(editForm.cleaned_data.get('password'))
        user.save()

    return render(request, 'account/edit.html', {'form':editForm})

def user_sideBar(request):
    return render(request, 'account/user_sideBar_partialView.html', {})
