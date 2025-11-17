# warga/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser


class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'
    paginate_by = 20

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    fields = ['judul', 'deskripsi', 'warga']  # sesuaikan dengan field kamu
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaListAPIView(ListAPIView):
    """
    API endpoint untuk menampilkan daftar semua warga dalam format JSON.
    
    Fitur:
    - Pagination otomatis
    - Filter dan search (jika dikonfigurasi)
    - Browsable API
    
    URL: GET /api/warga/
    Response: 
    {
        "count": 15,
        "next": "http://127.0.0.1:8000/api/warga/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "nik": "3201234567890123",
                "nama_lengkap": "Budi Santoso",
                "alamat": "Jl. Merdeka No. 1",
                "no_telepon": "081234567890"
            },
            ...
        ]
    }
    """
    
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    
    # Opsional: Konfigurasi pagination
    # pagination_class = None  # Untuk disable pagination


class WargaDetailAPIView(RetrieveAPIView):
    """
    Endpoint untuk menampilkan detail satu warga berdasarkan ID.
    
    Usage:
    GET /api/warga/1/     <- Ambil warga dengan ID 1
    GET /api/warga/5/     <- Ambil warga dengan ID 5
    GET /api/warga/999/   <- 404 Not Found (tidak ada)
    """
    
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

@api_view(['GET'])
def warga_list_fbv(request):
    """
    Function-based view alternatif untuk list warga.
    
    Ini adalah cara 'tradisional' sebelum class-based views.
    Umumnya tidak direkomendasikan untuk API besar,
    tapi berguna untuk endpoint simple.
    """
    if request.method == 'GET':
        warga = Warga.objects.all()
        serializer = WargaSerializer(warga, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def warga_detail_fbv(request, pk):
    """Function-based view untuk detail warga"""
    try:
        warga = Warga.objects.get(pk=pk)
    except Warga.DoesNotExist:
        return Response({'error': 'Warga not found'}, status=404)
    
    if request.method == 'GET':
        serializer = WargaSerializer(warga)
        return Response(serializer.data)
    
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]
    
    # Jika ingin menambahkan logika khusus, misal:
    def perform_create(self, serializer):
        # Misal: otomatis set warga berdasarkan user yang login
        serializer.save(warga=self.request.user.warga)

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal']

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = ['id', 'warga', 'judul', 'deskripsi', 'tanggal', 'status']