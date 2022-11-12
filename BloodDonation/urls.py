"""BloodDonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('RaktKosh/', views.home),
    path('RaktKosh/Register', views.register),
    path('RaktKosh/Register/SignUp', views.signup),
    path('RaktKosh/Register/SignUp/Verify', views._signup),
    path('RaktKosh/ForgotPassword', views.forgot),
    path('RaktKosh/_Forgot',views._forgot),
    path('RaktKosh/Profile/FindDonor', views.finddonor1),
    path('RaktKosh/Profile', views.profile),
    path('RaktKosh/FindDonor', views.finddonor),
    path('RaktKosh/Profile/FindNearestBloodBank', views.findnearestbloodbank),   
    path('RaktKosh/FindNearestBloodBank', views.findnearestbloodbank),
    path('RaktKosh/Profile/BloodRequest', views.bloodrequest),
    path('RaktKosh/Profile/BloodRequest/Request', views.bloodrequest),
    path('RaktKosh/Profile/Update', views.update), 

]
