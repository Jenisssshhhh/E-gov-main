from contextvars import Context
import os
from urllib import response
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from News.views import *
from News.models import *
from .models import *
from .forms import card, CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    side_news = News.objects.all()[5:10]
    context = {'side_news': side_news}
    return render(request, 'index.html', context)


def slider(request):
    return render(request, 'inc/slider.html')


def footer(request):
    return render(request, 'inc/footer.html')


def downloads(request):
    file = FilesAdmin.objects.all()
    context = {'file': file}
    return render(request, 'downloads.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404


def contact(request):
    return render(request, 'inc/contact_us.html')


@login_required(login_url='login')
def services(request):
    return render(request, 'inc/services.html')


@login_required(login_url='login')
def regis(request):
    fm = card(request.POST or None)
    if request.method == "POST":
        fm = card(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/confirm')
            fm = card()
            # fm =form.cleaned_data['firstname']
            # mn =form.cleaned_data['middlename']
            # ln= form.cleaned_data['lastname']
            # dob = form.cleaned_data['dob']
            # bp = form.cleaned_data['birthplace']
            # cn = form.cleaned_data['citizenship_no']
            # iz = form.cleaned_data['issue_zone']
            # idate = form.cleaned_data['issue_date']
            # gn = form.cleaned_data['gender']
            # ms = form.cleaned_data['marital_status']
            # ed = form.cleaned_data['education']
            # pf = form.cleaned_data['profession']
            # cas = form.cleaned_data['caste']
            # rel = form.cleaned_data['religion']
            # Reg = Idcard(firstname=fm,middlename=mn,lastname=ln, dob=dob, birthplace=bp,citizenship_no=cn,issue_zone=iz,issue_date=idate,gender=gn,
            #              marital_status=ms,education=ed,profession=pf,caste=cas,religion=rel)
            # Reg.save()
    context = {'form': fm}
    return render(request, 'inc/regis.html', context)


def confirm(request):
    return render(request, 'inc/confirm.html')


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Register sucessfull!! Login to continue")
            return redirect('login')
    context = {'form': form}
    return render(request, 'auth/userregistration.html', context)
    # return render(request,'auth/userregistration.html')


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "you are already logged in")
        return redirect('/regis')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "logged in sucsessfully")
                return redirect('/regis')

            else:
                messages.error(request, "invalid usernname or password")
                return redirect('/login')
        return render(request, 'auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out")
    return redirect('/')


def loksewa(request):
    return render(request, 'ser/loksewa.html')


def marriage(request):
    return render(request, 'ser/marriage.html')


def birth(request):
    return render(request, 'ser/birth.html')


def gallery(request):
    gall = Gallery.objects.all()
    context = {'gall': gall}
    return render(request, 'gallery.html', context)
