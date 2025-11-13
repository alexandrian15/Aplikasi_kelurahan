from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    WargaCreateView,
    PengaduanListView,
    PengaduanCreateView,
)

urlpatterns = [
    # Daftar Warga
    path('', WargaListView.as_view(), name='warga-list'),

    # Tambah Warga
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),

    # Detail Warga
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),

    # Daftar Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),

    # Tambah Pengaduan
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]
