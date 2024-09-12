from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import DersTalepleri, Profile, EgitmenProfile, OgrenciProfile, VerilenDersler, Mesaj




class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı İsmi', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Ad', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(label='Soyad', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Şifreyi Onaylayın', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            raise ValidationError(_("Bu şifre çok kısa. En az 8 karakter içermelidir.")) from error
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Girilen şifreler eşleşmiyor."))
        return password2
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    secenek1 = [
      ('erkek','Erkek'),
      ('kadin','Kadın'),
    ]
    secenek2 = [
      ('egitmen','Eğitmen'),
      ('ogrenci','Öğrenci'),
    ]
    cinsiyet = forms.ChoiceField(
      choices=secenek1,
      widget=forms.Select(attrs={'class': 'form-select'})
    )
    kullanici_tipi = forms.ChoiceField(
      choices=secenek2,
      widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Profile
        fields = ['kullanici_tipi', 'cinsiyet']


class DersTalepleriForm(forms.ModelForm):
    class Meta:
        model = DersTalepleri
        fields = ['baslik', 'ders', 'talep_notu', 'min_butce', 'max_butce', 'ogrenci_seviyesi', 'konum', 'dil', 'ders_tipi']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input'})

class EgitmenForm(forms.ModelForm):
    class Meta:
        model = EgitmenProfile
        exclude = ['profile']

class OgrenciForm(forms.ModelForm):
    class Meta: 
        model = OgrenciProfile
        fields = ['seviye']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Kullanıcı İsmi',
            'first_name': 'Ad',
            'last_name': 'Soyad',
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'kullanici_tipi' ]
        labels = {
            
            'bio': 'Hakkımda',
            'kullanici_tipi': "Kullanıcı Tipi"
        }
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'kullanici_tipi': forms.Select(attrs={'class': 'form-control'}),
        }
        
        

class DersEkleForm(forms.ModelForm):
    class Meta:
        model = VerilenDersler
        fields = ['ders','saatlik_ucret','ders_dili','sehir','ders_seviyesi', 'ders_tipi']
        exclude = ['egitmen']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profil_foto']
    
class MessageForm(forms.ModelForm):
    icerik = forms.CharField(label='Mesaj', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Mesaj
        fields = ['icerik']
    
