from django.contrib import admin
from django.urls import path
from EmailData import views as vw
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vw.login_page,name='loginpage'),
    path('signup/',vw.signup,name="registerpage"),
    path('landingPage/',vw.LandingPage),
    path('anotherLoginPage/',vw.AnotherLoginPage,name='anotherloginpage'),
    path('landingPage/errorPage/',vw.ErrorPage),
    path('confirm-registration/<int:user_id>/<str:token>/', vw.confirm_registration, name='confirm_registration'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
