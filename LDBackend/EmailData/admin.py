from django.contrib import admin
from EmailData.models import RegisterData
from .models import RegisterData


class RegisterDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'confirmpassword')

admin.site.register(RegisterData, RegisterDataAdmin)

# admin.site.register(RegisterData)
