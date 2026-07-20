# Dzikir with EthiqsHub

Kumpulan amalan Islami (doa, dzikir, dan bacaan) untuk berbagai situasi dalam kehidupan sehari-hari.  
Live: [dzikir.ethiqshub.com](https://dzikir.ethiqshub.com)

## Fitur

- 📚 Kumpulan amalan Islami terorganisir per kategori
- 📖 Mode **Pahami** — asal usul dan penjelasan lengkap
- 🧠 Mode **Menghafal** — tampilan story interaktif
- 🎨 Desain responsif
- 🔍 Pencarian & filter kategori
- ⭐ Favorit (localStorage)

## Struktur Konten

Satu sumber data JSON; halaman digenerate Hugo Content Adapters (tanpa file markdown per grup):

```
data/
├── amalan.json              # Index grup
└── groups/
    └── <group-id>.json      # Detail + daftar amalan
```

| Mode | URL |
|------|-----|
| Pahami | `/pahami/<group-id>/` |
| Menghafal | `/menghafal/<group-id>/?type=arabic\|latin\|indonesia` |

## Cara Menambah Amalan

1. Edit `data/groups/<group-id>.json` — tambah item di `cards`
2. Update `count` di `data/amalan.json` untuk grup tersebut
3. Set `"type": "guidance"` / `"personal"` atau `"menghafal": false` jika hanya untuk mode Pahami
4. Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk grup baru, tipe kartu, dan format lengkap

## Pengembangan Lokal

Butuh **Hugo Extended ≥ 0.123**.

```bash
git clone https://github.com/tegarimansyah/dzikir.git
cd dzikir

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

Dibuat dengan ❤️ sebagai wasilah untuk mendekatkan diri kepada-Nya.
