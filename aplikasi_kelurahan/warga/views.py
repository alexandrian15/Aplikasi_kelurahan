# warga/views.py
from django.views.generic import ListView
from .models import Warga

# Cukup 2 baris ini untuk menggantikan logika query dan rendering
class WargaListView(ListView):
    model = Warga
    # template_name = 'warga/warga_list.html' (Opsional, karena sudah sesuai convention)
    # context_object_name = 'daftar_warga' (Opsional, jika ingin mengganti nama object_list)
    # warga/views.py (lanjutan)
from django.views.generic import ListView, DetailView # Tambahkan DetailView
from .models import Warga

class WargaDetailView(DetailView):
    model = Warga
    # DetailView secara otomatis mencari template: warga/warga_detail.html