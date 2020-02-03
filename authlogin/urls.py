from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    url('home/', views.home, name='home'),
    url('signup/', views.signup, name='signup'),
    url("logout/", auth_views.LogoutView.as_view(), name="logout"),

    url('login/', auth_views.LoginView.as_view(), name='login'),

    # url('', include('social_django.urls', namespace='social')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('admin/', admin.site.urls),

]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'