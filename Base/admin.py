from django.contrib import admin
from .models import DersTalepleri, Ders, Dil, VerilenDersler, Mesaj, Profile, OgrenciProfile, EgitmenProfile, Sehir, Sohbet
# Register your models here.

admin.site.register(Profile)
admin.site.register(DersTalepleri)
admin.site.register(Ders)
admin.site.register(Dil)
admin.site.register(VerilenDersler)
admin.site.register(Mesaj)
admin.site.register(OgrenciProfile)
admin.site.register(EgitmenProfile)
admin.site.register(Sehir)
admin.site.register(Sohbet)