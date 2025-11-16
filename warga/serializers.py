"""
serializers.py: Mendefinisikan bagaimana model Warga 
diubah menjadi JSON dan sebaliknya
"""

from rest_framework import serializers
from .models import Warga


class WargaSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Warga.
    
    ModelSerializer secara otomatis:
    - Membaca field dari model Warga
    - Membuat validator berdasarkan field type
    - Mengatur read-only untuk field tertentu (seperti 'id')
    """
    
    class Meta:
        model = Warga
        # Tentukan field mana yang ingin di-expose di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']
        # Alternatif: fields = '__all__'  (semua field)
        
        # Opsional: Tentukan field yang read-only
        # read_only_fields = ['id']


# ADVANCED: Serializer dengan custom field
class WargaDetailSerializer(serializers.ModelSerializer):
    """Serializer dengan field tambahan"""
    
    # Custom field yang tidak ada di model
    umur = serializers.SerializerMethodField()
    
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'umur']
    
    def get_umur(self, obj):
        """Method untuk menghitung umur dari tanggal lahir"""
        from datetime import date
        if obj.tanggal_lahir:
            return date.today().year - obj.tanggal_lahir.year
        return None