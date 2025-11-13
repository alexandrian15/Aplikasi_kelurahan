
from django.db import models

STATUS_CHOICES = [
    ('baru', 'Baru'),
    ('diproses', 'Diproses'),
    ('selesai', 'Selesai'),
]

# warga/models.py
class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)  # NIK unik, cukup satu kali
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=16, unique=True)  # NIK unik
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15)
    tanggal_registrasi = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE)
    isi_pengaduan = models.TextField()
    tanggal = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='baru')  # opsional

    def __str__(self):
        return f"{self.pelapor.nama_lengkap} - {self.tanggal}"
