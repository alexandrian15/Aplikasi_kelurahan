// app.js
document.addEventListener('DOMContentLoaded', () => {
    const wargaListContainer = document.getElementById('warga-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';

    // Fungsi untuk membuat elemen warga
    function renderWarga(warga) {
        const wargaDiv = document.createElement('div');
        wargaDiv.style.border = '1px solid #ddd';
        wargaDiv.style.padding = '15px';
        wargaDiv.style.marginBottom = '10px';
        wargaDiv.style.borderRadius = '5px';
        wargaDiv.style.backgroundColor = '#f9f9f9';

        const nama = document.createElement('h3');
        nama.textContent = warga.nama_lengkap;
        nama.style.marginTop = '0';

        const nik = document.createElement('p');
        nik.textContent = `NIK: ${warga.nik}`;

        const alamat = document.createElement('p');
        alamat.textContent = `Alamat: ${warga.alamat}`;

        const telepon = document.createElement('p');
        telepon.textContent = `No. Telepon: ${warga.no_telepon || '-'}`;

        wargaDiv.appendChild(nama);
        wargaDiv.appendChild(nik);
        wargaDiv.appendChild(alamat);
        wargaDiv.appendChild(telepon);

        return wargaDiv;
    }

    // Ambil data dari API
    function fetchWargaList() {
        wargaListContainer.innerHTML = '<p>Memuat data...</p>';

        fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                wargaListContainer.innerHTML = ''; // Kosongkan kontainer
                if (data.results && data.results.length > 0) {
                    data.results.forEach(warga => {
                        const wargaElement = renderWarga(warga);
                        wargaListContainer.appendChild(wargaElement);
                    });
                } else {
                    wargaListContainer.innerHTML = '<p>Tidak ada data warga.</p>';
                }
            })
            .catch(error => {
                wargaListContainer.innerHTML = `
                    <p style="color: red;">
                        Gagal memuat data. Pastikan server backend berjalan dan CORS diizinkan.
                    </p>
                `;
                console.error('Fetch error:', error);
            });
    }

    // Panggil fungsi saat halaman dimuat
    fetchWargaList();
    // Dapatkan form dan elemen pesan
const form = document.getElementById('form-tambah-warga');
const statusMessage = document.getElementById('status-message');

form.addEventListener('submit', (event) => {
    event.preventDefault(); // Cegah reload halaman

    // Ambil nilai input
    const nik = document.getElementById('nik').value;
    const nama_lengkap = document.getElementById('nama_lengkap').value;
    const alamat = document.getElementById('alamat').value;
    const no_telepon = document.getElementById('no_telepon').value;

    const newWarga = {
        nik,
        nama_lengkap,
        alamat,
        no_telepon: no_telepon || null
    };

    // Kirim ke API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newWarga)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        statusMessage.textContent = `Warga ${data.nama_lengkap} berhasil ditambahkan!`;
        statusMessage.style.color = 'green';
        form.reset(); // Kosongkan form
        fetchWargaList(); // Refresh daftar
    })
    .catch(error => {
        console.error('Error:', error);
        statusMessage.textContent = `Gagal: ${JSON.stringify(error)}`;
        statusMessage.style.color = 'red';
    });
});
});