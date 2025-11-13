from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telepon = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nama_lengkap

class Pengaduan(models.Model):
    warga = models.ForeignKey(Warga, on_delete=models.CASCADE)
    isi_pengaduan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pengaduan oleh {self.warga.nama_lengkap} pada {self.tanggal}"
