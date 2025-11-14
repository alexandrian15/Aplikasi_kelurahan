from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    WargaCreateView,
    PengaduanListView,
    PengaduanCreateView,
    PengaduanUpdateView,
    PengaduanDeleteView,
)

urlpatterns = [
    # URL untuk Warga
    path('', WargaListView.as_view(), name='warga-list'), # ⚠️ name='warga-list'
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    
    # URL untuk Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'), # ⚠️ name='pengaduan-list'
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),

]