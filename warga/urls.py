# warga/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Daftar warga: /warga/ (ubah name ke 'warga-list')
    path('', views.WargaListView.as_view(), name='warga-list'),  # Hyphen: warga-list
    
    # Detail warga: /warga/<pk>/ (sudah hyphen dari fix sebelumnya)
    path('<int:pk>/', views.WargaDetailView.as_view(), name='warga-detail'),
    
    # Daftar pengaduan: /warga/pengaduan/ (tugas praktik)
    path('pengaduan/', views.PengaduanListView.as_view(), name='pengaduan-list'),  # Opsional: ubah ke hyphen juga
]