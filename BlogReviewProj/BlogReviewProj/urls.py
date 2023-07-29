"""
URL configuration for BlogReviewProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Standard imports for Django URL configuration
from django.contrib import admin
from django.urls import path

# Importing your views from the reviewerapp app
from reviewerapp.views import homepage, coverpage, Register, Signin, signout

# urlpatterns is a list where you define your URL paths and map them to their respective views.
# Django uses this list to route incoming HTTP requests to the appropriate view functions based on the path in the URL.
urlpatterns = [
    # This line sets up the URL for the Django admin site, which is a built-in feature of Django.
    # It's typically accessible at the /admin/ path of your site.
    path('admin/', admin.site.urls),

    # The empty string '' represents the root of your site. Here, it's mapped to the 'coverpage' view.
    # 'name' is an optional argument that lets you name your URL, so you can refer to it elsewhere in your code.
    path('', view=coverpage, name='cover'),

    # Here, the path 'home/' is mapped to the 'homepage' view.
    path("home/", view=homepage, name="home"),

    # Here, the path 'register/' is mapped to the 'Register' view.
    path("register/", view=Register, name="register"),

    # Here, the path 'signin/' is mapped to the 'Signin' view.
    path("signin/", view=Signin, name="signin"),

    # Here, the path 'signout/' is mapped to the 'signout' view.
    path("signout/", view=signout, name="signout"),
]

