from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('record/bulbissue/<str:Bulb_Issue>',views.bulbissue, name='problem1'),
    path('record/currleak/<str:Curr_Leak>',views.currleak, name='problem2'),
    path('record/brokwire/<str:Brok_Wire>',views.brokwire, name='problem3'),
    path('record/nosignal/<str:No_Sgnl>',views.nosignal, name='problem4'),
]