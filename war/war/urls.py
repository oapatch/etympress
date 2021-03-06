"""war URL Configuration

VII -- Virtual Internet Interface!

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
from django.urls import include, path
#from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from war.war.views import Jade, WarInn, WarEntrance

urlpatterns = [
    path('', RedirectView.as_view(url='https://thewarsheadinn.tumblr.com/')),
    path('connect', RedirectView.as_view(url='https://docs.google.com/forms/d/1cI0xz9zYplaaxosRclDTR4B8g0EwcLrJ_qDDOwPihe4/')),
    path('post', RedirectView.as_view(url='https://thewarsheadinn.tumblr.com/')),
    path('code', RedirectView.as_view(url='https://github.com/oapatch/etympress')),
    #path('/stage', Jade.as_view(url='stage')),
    path('admin/', admin.site.urls),
    # path('xine', RedirectView.as_view(url=''),
    #path('', Jade.as_view()),
    #path('inn/', WarInn.as_view()),
]

