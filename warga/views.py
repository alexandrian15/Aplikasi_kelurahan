from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView  # Untuk preview
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm  # Sekarang OK

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):  # Tugas praktik
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    ordering = ['-tanggal_lapor']

     # Opsional: Filter dinamis berdasarkan status (contoh .filter() dari materi)
    def get_queryset(self):
        queryset = super().get_queryset()  # Ambil base QuerySet (semua + ordering)
        status = self.request.GET.get('status')  # Ambil parameter ?status=BARU dari URL
        if status:
            queryset = queryset.filter(status=status)  # Filter seperti Pengaduan.objects.filter(status='BARU')
        return queryset

# Preview pertemuan depan (opsional)
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')