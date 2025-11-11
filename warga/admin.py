from django.contrib import admin
from .models import Warga, Pengaduan

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'nik', 'no_telepon', 'tanggal_registrasi')

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor')  # Kolom: Judul, Pelapor (relasi), Status, Tanggal
    list_filter = ('status', 'tanggal_lapor', 'pelapor')  # Filter kolom
    search_fields = ('judul', 'deskripsi', 'pelapor__nama_lengkap')  # Search termasuk nama pelapor
    # Raw ID untuk relasi (jika banyak warga)
    raw_id_fields = ('pelapor',)