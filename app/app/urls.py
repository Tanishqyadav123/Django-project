"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

#for display image
from django.conf.urls.static import static

#for import setting module
from  django.conf import settings
media_url = settings.MEDIA_URL


from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home), 
    path('Register/' , views.register), 
    path('userlist/' , views.userlist),
    path('login/' , views.login),
    path('adminhome/' , views.adminhome),
    path('addcourse/' , views.addcourse),
    path('courselist1/' , views.courselist1),
    path('addbatch/' , views.addbatch),
    path('studenthome/' , views.studenthome),
    path('batchlist1/' , views.batchlist1),
    path('batchlist2/' , views.batchlist2),
    path('courselist2/' , views.courselist2),
    path('admission/' , views.admission),
    path('logout1/' , views.logout1),
    
]+static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)
