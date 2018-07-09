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
        username=forms.CharField()
        password = forms.CharField(required=True, widget=forms.PasswordInput)

class LoginforView(View):
    def get(self,request):
        form=Loginform()
        return render(request, template_name="login.html", context={'form': form})

    def post(self, request):
        form = Loginform(request.POST)
        username=""
        password=""
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
        user_id=User.objects.filter(username=username,password=password).values('id')
        return redirect('cardlist',user_id=user_id)

class homepage(View):
    def get(self,request):
        return render(request,template_name="home.html",context=None)

class Addcard(forms.ModelForm):
    class Meta:
        model=creditcard
        exclude=['id','user']
        widgets={
            'friendly_name':forms.TextInput(),
            'name_on_card':forms.TextInput(),
            'expiry_date':forms.TextInput(),
            'type':forms.TextInput(),
            'cvv':forms.TextInput(),
            'card_no':forms.TextInput()
        }
class Viewcardlist(LoginRequiredMixin,ListView):
    model=creditcard
    context_object_name = 'cards'
    template_name = 'card_list.html'

    def get_object(self,queryset=None):
        return get_object_or_404(creditcard,**self.kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(Viewcardlist,self).get_context_data(**kwargs)
        context['cards']=self.model.objects.filter(user=self.request.user).values()
        context.update({'user_permissions':self.request.user.get_all_permissions})
        return context


class Addcreditcard(LoginRequiredMixin,CreateView):
    template_name = 'create_card.html'
    model = creditcard
    form_class = Addcard
    success_url = reverse_lazy('index.html')
    # import ipdb
    # ipdb.set_trace()
    def get_context_data(self, **kwargs):
        context = super(Addcreditcard, self).get_context_data(**kwargs)
        context.update({
            'form': context.get('form'),
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('user_id'))
        userform = Addcard(request.POST)

        if userform.is_valid():
          card = userform.save(commit=False)
          card.user=user
          card.save()
        return redirect('/cardlist/')

class UpdateCreditcard(LoginRequiredMixin,UpdateView):
    model=creditcard
    template_name = 'create_card.html'
    form_class = Addcard
    success_url = reverse_lazy('Creditcardapp:cardlist')

class Deletecreditcard(LoginRequiredMixin,DeleteView):
    model = creditcard
    template_name = 'deleteconfirm.html'
    form_class=Addcard
    success_url = reverse_lazy('Creditcardapp:cardlist')


