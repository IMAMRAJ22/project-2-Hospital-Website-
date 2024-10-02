from django.contrib import admin # type: ignore
from .models import userdata,Doctorinfo,Patientdetails,Doctorlogin

admin.site.register(userdata)
admin.site.register(Doctorinfo)
admin.site.register(Patientdetails)
admin.site.register(Doctorlogin)
# Register your models here.
