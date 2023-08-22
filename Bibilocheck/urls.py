from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.landing_page,name="landing_page"),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutuser,name='logout'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('searchresultpage',views.searchresultpage,name="searchresultpage"),
    path('Bookpage/<str:value>',views.Bookpage,name="Bookpage"),
    path('followrequest/<str:profile>/',views.followrequest,name='followrequest'),
    path('home/lists/',views.lists,name="lists"),
    path('home/<str:id>/',views.Bookdbpage,name='Bookdbpage'),
    path('home/statusdelete/<str:id>/',views.statusuploaddelete,name='statusuploaddelete'),
    path('followaccept/<str:profile>/',views.followaccept,name='followaccept'),
    path('profile/',views.profile,name='profile'),
    path('deletefollower/<str:follower>',views.deletefollower,name='deletefollower'),
    path('deletefollowing/<str:followin>',views.deletefollowing,name="deletefollowing"),
    path("Forum/",views.forum,name="forum"),
    path("subscription/",views.subscription,name="subscription")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
