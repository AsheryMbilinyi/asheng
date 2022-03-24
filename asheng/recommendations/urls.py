from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

admin.site.site_header = "asheng admin"

urlpatterns = [
    #path('', index),
    path('', index, name="index")
    #path('success', success, name = 'success')

]