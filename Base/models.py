from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT
from django.core.exceptions import ValidationError

class Dil(models.Model):
  dil = models.CharField(max_length=50)
  def __str__(self):
    return self.dil
  

class Sehir(models.Model):
  sehir = models.CharField(max_length=50)
  def __str__(self):
    return self.sehir
  

class Ders(models.Model):
  ders = models.CharField(max_length=50)

  def __str__(self) :
    return self.ders


class DersTalepleri(models.Model):
  seviye = [
    ('İlkokul', 'İlkokul'),
    ('Ortaokul', 'Ortaokul'),
    ('Lise', 'Lise'),
    ('Üniversite', 'Üniversite'),
    ('Yüksek Lisans','Yüksek Lisans'),
  ]

  ders_tipleri = [
        ('online', 'Online'),
        ('yuz_yuze', 'Yüz Yüze'),
        ('iksisde', 'Online ve Yüz Yüze'),
    ]
  kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
  baslik = models.CharField(max_length=50)
  ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
  talep_notu= models.TextField(max_length=200,null=True,blank=True)
  talep_durumu = models.BooleanField(default=False)
  min_butce = models.IntegerField(validators=[MinValueValidator(0)])
  max_butce = models.IntegerField(validators=[MaxValueValidator(10000)])
  ogrenci_seviyesi = models.CharField(max_length=50,choices=seviye)
  olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
  konum = models.ForeignKey(Sehir, on_delete=models.CASCADE)
  dil = models.ForeignKey(Dil,on_delete=models.CASCADE)
  gunceleme=models.DateTimeField(auto_now=True)
  ders_tipi = models.CharField(
        max_length=50,
        choices=(('online', 'Online'), ('yuz_yuze', 'Yüz Yüze'), ('iksisde', 'Online ve Yüz Yüze')),
        
    )  


  
  def __str__(self):
    return self.baslik


class VerilenDersler(models.Model):
  seviye = [
    ('İlkokul', 'İlkokul'),
    ('Ortaokul', 'Ortaokul'),
    ('Lise', 'Lise'),
    ('Universite', 'Üniversite'),
    ('Yukseklisans','Yüksek Lisans'),
  ]

  ders_tipleri = [
        ('online', 'Online'),
        ('yuz_yuze', 'Yüz Yüze'),
        ('iksisde', 'Online ve Yüz Yüze'),
    ]
  
  ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
  saatlik_ucret = models.IntegerField(validators=[MinValueValidator(0)])
  egitmen = models.ForeignKey(User, on_delete=models.CASCADE)
  ders_dili = models.ForeignKey(Dil, on_delete=models.CASCADE)
  sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE)
  ders_seviyesi = models.CharField(max_length=50, choices=seviye)
  ders_tipi = models.CharField(
        max_length=50,
        choices=(('online', 'Online'), ('yuz_yuze', 'Yüz Yüze'), ('iksisde', 'Online ve Yüz Yüze')),
        
    )  

  def __str__(self):
    return f'{self.egitmen} Dersin Dili:{self.ders_dili} Ders:{self.ders} Ücret{self.saatlik_ucret}'




class Profile(models.Model):
  secenek1 = [
    ('erkek','Erkek'),
    ('kadin','Kadın'),
  ]
  secenek2 = [
    ('egitmen','Eğitmen'),
    ('ogrenci','Öğrenci'),
  ]
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  kullanici_tipi = models.CharField(max_length=50,null=False, choices=secenek2)
  bio = models.TextField(max_length=200, null=True,blank=True, default=None)
  profil_foto = models.ImageField(upload_to='avatarlar',null=True,blank=True,)
  cinsiyet = models.CharField(max_length=50,choices=secenek1)
  
  def __str__(self):
    return str(self.user)
  

class OgrenciProfile(models.Model):
  choices = [
    ('ilkokul', 'İlkokul'),
    ('ortaokul', 'Ortaokul'),
    ('lise', 'Lise'),
    ('universite', 'Üniversite'),
    ('yukseklisans','Yüksek Lisans'),
  ]
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
  seviye = models.CharField(max_length=50, choices=choices)
  
  def __str__(self):
    return f'{self.profile.user.username} - Öğrenci'


class EgitmenProfile(models.Model):
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.profile.user.username} - Eğitmen'
  

class Sohbet(models.Model):
  user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_sohbet')
  user2 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user2_sohbet')
  def __str__(self):
        return f'{self.user1.username} - {self.user2.username}'
  
class Mesaj(models.Model):
  gönderen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gönderilen_mesajlar')
  alici = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True,default=None,related_name='alınan_mesajlar')
  tarih = models.DateTimeField(auto_now_add=True)
  icerik = models.CharField(max_length=200)
  sohbet = models.ForeignKey(Sohbet, on_delete=models.CASCADE,related_name='messages')

  def __str__(self):
    return f'{self.gönderen} --> {self.alici}: {self.icerik[0:50]}'