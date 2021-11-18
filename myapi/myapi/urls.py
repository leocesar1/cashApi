"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [url(r'^', include('cashApi.urls')),]

urlpatterns += [
    path('api_auth/', include('rest_auth.urls')),
    path('api_auth/registration/',      include('rest_auth.registration.urls'))
]
# for registration, login and logout
# Registration ###################################################
# [post] /api_auth/registration/
# json_data = {
#    'username': 'username',
#    'email': 'email@email.com',
#    'password1': 'password',
#    'password2': 'passwordConfirmation',
# }
# Response = {
#    "key": Token
# }
# Login ###################################################
# [post] /api_auth/login/
# json_data = {
#    'username': 'username',
#    'password': 'password'
# }
# Response = {
#    "key": Token
# }
# Logout ###################################################
# [post] /api_auth/logout/
# header = {
#    'Authorization': 'Token <Token>'
# }

