from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.MainPage, name='Home'),
  path('login/', views.login_page, name='login'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_page, name='register'),
  path('biz_kimiz/', views.biz_kimiz, name='biz_kimiz'),
  path('derstalepleri/', views.derstalepleri,name='DersTalepleri'),
  path('OzelDers/',views.OzelDers,name='OzelDers' ),
  path('talepolustur/',views.TalepOlustur,name='TalepOlustur' ),
  path('talep_detay/<str:pk>/', views.talep_detay, name='TalepDetay'),
  path('talep_sil/<str:pk>/', views.talep_sil, name='TalepSil'),
  path('talep_duzenle/<str:pk>/', views.talep_duzenle, name='TalepDuzenle'),
  path('profil/<str:pk>/',views.Profil, name='profil'),
  path('mesaj/',views.mesaj, name='mesaj'),
  path('talebi_kabul_et/<str:pk>',views.talep_kabul, name='TalepKabul'),
  path('verdigim_dersler/<str:pk>/',views.verdigim_dersler,name='VerdigimDersler'),
  path('ders_ekle/<str:pk>/',views.ders_ekle,name='DersEkle'),  
  path('ders_sik/<str:pk>/',views.ders_sil,name='DersSil'),
  path('ders_duzenle/<str:pk>/',views.ders_duzenle,name='DersDuzenle'),
  path('avatar_guncelle/<str:pk>/',views.avatar_guncelle,name='AvatarGuncelle'),
  path('sohbet_detay/<str:pk>',views.sohbet_detay,name='SohbetDetay'),
  path('iletisime_gec1/<str:pk>',views.iletisime_gec1,name='IletisimeGec1'),
  path('hoca_detay/<str:pk>',views.hoca_detay,name='HocaDetay'),
  path('iletisime_gec2/<str:pk>',views.iletisime_gec2,name='IletisimeGec2'),
  path('ders_taleplerim/<str:pk>',views.ders_taleplerim,name='DersTaleplerim'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

