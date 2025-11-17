# warga/models.py
from django.db import models

class Warga(models.Model):
    nik          = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=120)
    alamat       = models.TextField()
    no_telepon   = models.CharField(max_length=15, blank=True)  # ← baru
    tanggal        = models.DateField(auto_now_add=True)   # ← kolom baru
    
    def __str__(self):
        return f"{self.nama_lengkap} ({self.nik})"

class Pengaduan(models.Model):
    # pakai string 'Warga' → tidak butuh import Warga
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    warga       = models.ForeignKey(
                    'Warga',            # atau 'warga.Warga' kalau beda app
                    on_delete=models.CASCADE,
                    related_name='pengaduan'
                  )
    judul       = models.CharField(max_length=100)
    deskripsi   = models.TextField()
    tanggal     = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=20,choices=STATUS_CHOICES, default='BARU')

    def __str__(self):
        return f"{self.judul} - {self.warga}"