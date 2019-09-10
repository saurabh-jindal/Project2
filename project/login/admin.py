from django.contrib import admin
from .models import Signup
# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    pass



admin.site.register(Signup, SignupAdmin)