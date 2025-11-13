from django.contrib import admin
from .models import Warga, Pengaduan

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'alamat', 'no_telepon')
    search_fields = ('nik', 'nama_lengkap')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('warga', 'isi_pengaduan', 'tanggal')  # ubah dari pelapor -> warga
    search_fields = ('warga__nama_lengkap', 'isi_pengaduan')
    raw_id_fields = ('warga',)  # ubah dari pelapor -> warga
