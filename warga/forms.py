from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nama_lengkap', 'nik', 'alamat']
        widgets = {
            'alamat': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nama_lengkap': 'Nama Lengkap',
            'nik': 'NIK',
            'alamat': 'Alamat',
        }

    def clean_nik(self):
        nik = self.cleaned_data['nik']
        if len(nik) != 16 or not nik.isdigit():
            raise forms.ValidationError("NIK harus 16 digit angka.")
        if Warga.objects.filter(nik=nik).exists():
            raise forms.ValidationError("NIK sudah terdaftar.")
        return nik