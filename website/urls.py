from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('record/<str:Bulb_Issue>',views.bulbissue, name='record'),
    path('record/<str:Curr_Leak>',views.currleak, name='record2'),
    path('record/<str:Brok_Wire>',views.brokwire, name='record2'),
    path('record/<str:No_Sgnl>',views.nosignal, name='record2'),
]