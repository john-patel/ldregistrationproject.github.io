from django.contrib import admin
from django.urls import path
from EmailData import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vw.login_page,name='loginpage'),
    path('signup/',vw.signup,name="registerpage"),
    path('landingPage/',vw.LandingPage),
    path('anotherLoginPage/',vw.AnotherLoginPage,name='anotherloginpage'),
    path('landingPage/errorPage/',vw.ErrorPage),
    path('confirm-registration/<int:user_id>/<str:token>/', vw.confirm_registration, name='confirm_registration'),
]
