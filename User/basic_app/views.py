# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms


# Create your views here.

def base(request):
    return render(request, 'basic_app/base.html')

def index(request):
    return render(request, 'basic_app/index.html')

def userForm(request):
    u_form = forms.userForm()

    if request.method == 'POST':
        u_form = forms.userForm(request.POST)

        if u_form.is_valid():
            # DO SOMETHING CODE
            
            return index(request)

    return render(request, 'basic_app/forms.html',{'form': u_form})
