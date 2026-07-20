# Muslim Flashcard

Kumpulan doa-doa dalam Islam untuk berbagai situasi dalam kehidupan sehari-hari.

## Fitur

- 📚 Kumpulan doa Islami terorganisir per kategori
- 📖 Mode **Pahami** — asal usul dan penjelasan lengkap
- 🧠 Mode **Menghafal** — tampilan story interaktif
- 🎨 Desain responsif
- 🔍 Pencarian & filter kategori
- ⭐ Favorit (localStorage)

## Struktur Konten

Satu sumber data JSON; halaman digenerate Hugo Content Adapters (tanpa file markdown per grup):

```
data/
├── doa.json              # Index grup
└── groups/
    └── <group-id>.json   # Detail + daftar doa
```

| Mode | URL |
|------|-----|
| Pahami | `/pahami/<group-id>/` |
| Menghafal | `/menghafal/<group-id>/?type=arabic\|latin\|indonesia` |

## Cara Menambah Doa

1. Edit `data/groups/<group-id>.json` — tambah item di `cards`
2. Update `count` di `data/doa.json` untuk grup tersebut
3. Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk grup baru dan format lengkap

## Pengembangan Lokal

Butuh **Hugo Extended ≥ 0.123**.

```bash
git clone https://github.com/tegarimansyah/muslim-flashcard.git
cd muslim-flashcard

hugo server -D
# http://localhost:1313
```

## Build Produksi

```bash
hugo --minify
# output: public/
```

## Deploy

GitHub Actions men-deploy ke GitHub Pages saat push ke `main`. Domain: [dzikir.ethiqshub.com](https://dzikir.ethiqshub.com).

## Lisensi

Dibuat dengan ❤️ untuk umat
