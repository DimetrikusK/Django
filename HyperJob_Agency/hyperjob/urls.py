from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', views.UserSignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('login', views.UserLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('home', views.HomeView.as_view()),
    path('resumes/', include('resume.urls')),
    path('resume/', include('resume.urls')),
    path('vacancies/', include('vacancy.urls')),
    path('vacancy/', include('vacancy.urls')),
]