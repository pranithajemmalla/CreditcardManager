from django.urls import path
from creditcards.Views import Addcreditcard,homepage,Viewcardlist,UpdateCreditcard,Deletecreditcard
from creditcards.Forms.auth import LoginforView
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.base import TemplateView
app_name="Creditcardapp"
urlpatterns = [
    path(r'addcard/<int:user_id>',Addcreditcard.as_view(),name="addcard"),
    path(r'updatecard/<int:pk>',UpdateCreditcard.as_view(),name="updatecard"),
    path(r'deletecard/<int:pk>', Deletecreditcard.as_view(), name="deletecard"),
    path(r'cardlist/',Viewcardlist.as_view(),name="cardlist"),
    #path(r'home/',homepage.as_view(),name="home"),
    path(r'login/',views.login,{'template_name':'registration/login.html'},name="login"),
    path(r'logout/', views.logout, {'template_name': 'registration/login.html'}, name="logout"),
    path(r'',TemplateView.as_view(template_name='home.html'),name="home")
]