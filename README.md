# Muslim Flashcard

Kumpulan doa-doa dalam Islam untuk berbagai situasi dalam kehidupan sehari-hari.

## Fitur

- 📚 Kumpulan doa-doa Islami terorganisir dalam kategori
- 📖 Mode "Lihat untuk Pahami" dengan asal usul dan penjelasan lengkap
- 🧠 Mode "Membaca dan Menghafal" dengan tampilan interaktif
- 🎨 Desain responsif dan cantik
- 🔍 Fitur pencarian doa
- 📱 Mobile-friendly

## Struktur Kategori

- Ketika Merasa Terlalu Banyak Maksiat dan Berdosa
- Doa Pagi dan Petang
- Doa Sebelum Tidur
- Doa Setelah Shalat
- Doa Saat Sakit
- Doa Musafir

## Cara Menambah Doa Baru

Edit file `themes/muslim-flashcard-theme/data/doa.json` dan tambahkan doa baru sesuai format yang sudah ada.

## Lokal Pengembangan

```bash
# Clone repository ini
git clone https://github.com/username/muslim-flashcard.git
cd muslim-flashcard

# Jalankan Hugo server
hugo server -D

# Buka http://localhost:1313
```

## Build untuk Produksi

```bash
hugo --minify
```

File yang sudah di-build akan berada di folder `public/`.

## Deploy ke GitHub Pages

Repository ini sudah dikonfigurasi untuk auto-deploy ke GitHub Pages menggunakan GitHub Actions. Setiap kali Anda push ke branch `main`, website akan otomatis di-deploy.

## Lisensi

Dibuat dengan ❤️ untuk umat