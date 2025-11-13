from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# Daftar Warga
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nama_lengkap__icontains=q) | queryset.filter(nik__icontains=q)
        return queryset

# Detail Warga
class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

# Tambah Warga
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

# Daftar Pengaduan
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor']

# Tambah Pengaduan
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
