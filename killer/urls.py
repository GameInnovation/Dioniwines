"""killer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from greek.views import homegreek, greekfeedback, greekallmyfeedback, greekviewfeedback, \
    greekdeletedfeedback, greekviewdeletedfeedback, greekdeletefeedback, greeksignupuser, \
    greekloginuser, greekorder, greekallmyorders, greekvieworder, greekdeleteorder, greekdeletedorders, greekreviewdeletedorders, greekdeletedeletedorder, greeklogoutuser
from django.contrib import admin
from django.urls import path
from web import views
path('greek/signup/', greeksignupuser, name='greeksignupuser'),
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    
    # Greek
    path('greek/', homegreek, name="homegreek"),
    path('greek/login/', greekloginuser, name='greekloginuser'),
    path('greek/signup/', greeksignupuser, name='greeksignupuser'),
    path('greek/greeklogoutuser/', greeklogoutuser, name='greeklogoutuser'),
    path('greek/feedback/', greekfeedback, name="greekfeedback"),
    path('greek/allmyfeedback/', greekallmyfeedback, name="greekallmyfeedback"),
    path('greek/viewfeedback/<int:feedback_pk>', greekviewfeedback, name='greekviewfeedback'),
    path('greek/deleted', greekdeletedfeedback, name='greekdeletedfeedback'),
    path('greek/viewdeleted/<int:feedback_pk>', greekviewdeletedfeedback, name='greekviewdeletedfeedback'),
    path('greek/viewfeedback/<int:feedback_pk>/delete', greekdeletefeedback, name='greekdeletefeedback'),

    # Greek Order
    path('greek/order/', greekorder, name='greekorder'),
    path('greek/allmyorders/', greekallmyorders, name='greekallmyorders'),
    path('greek/vieworder/<int:order_pk>', greekvieworder, name='greekvieworder'),
    path('greek/deleteorder/<int:order_pk>', greekdeleteorder, name='greekdeleteorder'),
    path('greek/deletedorders/', greekdeletedorders, name='greekdeletedorders'),
    path('greek/reviewdeletedorders/<int:order_pk>', greekreviewdeletedorders, name='greekreviewdeletedorders'),
    path('greek/deletedeletedorder/<int:order_pk>', greekdeletedeletedorder, name='greekdeletedeletedorder'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('homelogout/', views.homelogoutuser, name='homelogoutuser'),
    
    # FeedBack
    path('feedback/', views.feedback, name='feedback'),
    path('welcomefeedback/', views.welcomefeedback, name='welcomefeedback'),
    path('allmyfeedback/', views.allmyfeedback, name='allmyfeedback'),
    path('viewfeedback/<int:feedback_pk>', views.viewfeedback, name='viewfeedback'),
    path('viewfeedback/<int:feedback_pk>/delete', views.deletefeedback, name='deletefeedback'),
    path('deleted', views.deletedfeedback, name='deletedfeedback'), # Δοκίμαζε μια με / μια χωρίς /. Με έχει πρήξει.
    path('viewdeleted/<int:feedback_pk>', views.viewdeletedfeedback, name='viewdeletedfeedback'),  
    
    #Order
    path('order/', views.order, name='order'),
    path('allmyorders/', views.allmyorders, name='allmyorders'),
    path('vieworder/<int:order_pk>', views.vieworder, name='vieworder'),
    path('deleteorder/<int:order_pk>', views.deleteorder, name='deleteorder'),
    
    path('deleteorder/<int:order_pk>', views.deletedeletedorder, name='deletedeletedorder'), 
    
    path('deletedorders/', views.deletedorders, name='deletedorders'),  
    path('reviewdeletedorders/<int:order_pk>', views.reviewdeletedorders, name='reviewdeletedorders'),

    # mobilelist
    path('mobilelist/', views.mobile, name='mobile'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
