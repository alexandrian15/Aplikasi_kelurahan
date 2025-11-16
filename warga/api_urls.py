"""
api_urls.py: Routing khusus untuk API endpoints
"""

from django.urls import path
from .views import WargaListAPIView, WargaDetailAPIView

urlpatterns = [
    # List semua warga
    path('warga/', 
         WargaListAPIView.as_view(), 
         name='api-warga-list'),
    
    # Detail satu warga berdasarkan ID
    path('warga/<int:pk>/', 
         WargaDetailAPIView.as_view(), 
         name='api-warga-detail'),
]