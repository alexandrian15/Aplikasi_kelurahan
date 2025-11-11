# warga/urls.py
from django.urls import path
from .views import WargaListView, WargaDetailView

urlpatterns = [
    # Penting: CBV harus dipanggil dengan .as_view()
    path('', WargaListView.as_view(), name='warga-list'),



    # URL Detail: /warga/1/
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'), 
]
