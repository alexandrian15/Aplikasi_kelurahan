# warga/models.py
from django.db import models

# Model Warga (update dengan field tambahan untuk match admin)
class Warga(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    nik = models.CharField(max_length=16, unique=True)  # NIK unik
    alamat = models.TextField()
    
    # Field tambahan untuk fix admin error
    no_telepon = models.CharField(max_length=15, blank=True, null=True)  # Nomor telepon (opsional)
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)  # Otomatis set saat create

    def __str__(self):
        return self.nama_lengkap

# Model Pengaduan (dari pertemuan 2, pastikan ada)
class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    
    # Relasi ForeignKey ke Warga
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')

    def __str__(self):
        return self.judul