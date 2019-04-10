from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from tablib import Dataset

from .forms import *
from .models import *
from .resources import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)



def about(request):
    context = {}
    return render(request, 'about.html', context)



def report(request):
    context = {}
    return render(request, 'report.html', context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {
        'form': form,
    }
    return render(request, 'feedback.html', context)

@login_required
def profile(request):
    verified = VerificationCard.objects.filter(user=request.user)
    if verified.exists():
        form = VerificationCardForm()
        redirect('profile')
    else:
        if request.method == 'POST':
            form = VerificationCardForm(request.POST)
            if form.is_valid:
                verify = form.save(commit=False)
                verify.user = request.user
                verify.student_information = StudentInformation.objects.get(user=request.user)
                verify.save()
                redirect('profile')
        else:
            form = VerificationCardForm()

    card = StudentInformation.objects.filter(user=request.user)
    all_cards = StudentInformation.objects.all()
    context = {
        'card': card,
        'form': form,
        'verified': verified,
        'all_cards': all_cards,
    }
    return render(request, 'profile.html', context)


def page404(request):
    context = {}
    return render(request, '404.html', context)


def page500(request):
    context = {}
    return render(request, '500.html', context)

def excel_data_upload(request):
    pass

def admissions(request):
    context = {}
    return render(request, 'admission.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def calendar(request):
    context = {}
    return render(request, 'school_calendar.html', context)