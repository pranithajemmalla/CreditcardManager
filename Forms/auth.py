from django.contrib.auth import authenticate
from django.views import View
from creditcards.models import *
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.forms import ModelForm
from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate

class Loginform(forms.Form):
        username=forms.CharField(required=True,widget=forms.TextInput())
        password = forms.CharField(required=True, widget=forms.PasswordInput())

class LoginforView(View):
    def get(self,request):
        form=Loginform()
        return render(request, template_name="login.html", context={'form': form})

    def post(self, request,*args,**kwargs):
        form = Loginform(request.POST)
        username=""
        password=""
        import ipdb
        ipdb.set_trace()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
        user_id=User.objects.filter(username=username,password=password).values('id')
        return redirect('cardlist',user_id=user_id)
