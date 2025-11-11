from django.contrib import admin
from .models import Warga


class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'no_telepon', 'tanggal_registrasi')
    search_fields = ('nik', 'nama_lengkap')
    list_filter = ('tanggal_registrasi',)

admin.site.register(Warga, WargaAdmin)