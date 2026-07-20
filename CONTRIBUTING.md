# Contribution Guidelines

Thank you for your interest in contributing to **Dzikir with EthiqsHub**!

## How to Contribute

### Reporting Issues
- Use GitHub issue templates for bugs, feature requests, or amalan requests
- Include clear steps to reproduce and screenshots when possible

### Content Contributions
1. **Amalan request issue** — use the `[AMALAN]` template
2. **Direct contribution** — edit JSON under `data/` (see below)

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit, push, and open a Pull Request

---

## Content Architecture

Content is **JSON-only**. Hugo Content Adapters generate pages at build time — no per-group `.md` files.

```
data/
├── amalan.json                 # Index of all groups (source of truth for listing)
└── groups/
    ├── maksiat-berdosa.json # Cards for one group
    ├── setelah-shalat.json
    └── ...

content/
├── menghafal/
│   ├── _index.md
│   └── _content.gotmpl      # Adapter → virtual /menghafal/<group-id>/ pages
└── pahami/
    ├── _index.md
    └── _content.gotmpl      # Adapter → virtual /pahami/<group-id>/ pages
```

| File | Role |
|------|------|
| `data/amalan.json` | Index only: `id`, `title`, `description`, `category`, `icon`, `color`, `file`, `count` |
| `data/groups/<id>.json` | Full group + `cards[]` (arabic, latin, translation, background, source, optional `menghafal`) |
| `_content.gotmpl` | Registers virtual pages from JSON (Hugo ≥ 0.123) |

Both modes share the same group JSON. **Pahami** shows all cards; **Menghafal** skips cards with `"menghafal": false`.

---

## Adding a New Group

### 1. Create the group file

`data/groups/nama-grup.json`:

```json
{
  "id": "nama-grup",
  "title": "Judul Grup",
  "description": "Deskripsi singkat grup.",
  "category": "Kondisi Hati & Spiritual",
  "icon": "🤲",
  "color": "#059669",
  "cards": []
}
```

### 2. Register it in the index

Add an entry to `data/amalan.json` → `groups`:

```json
{
  "id": "nama-grup",
  "title": "Judul Grup",
  "description": "Deskripsi singkat grup.",
  "category": "Kondisi Hati & Spiritual",
  "icon": "🤲",
  "color": "#059669",
  "file": "groups/nama-grup.json",
  "count": 0
}
```

Keep `count` in sync with `cards.length` in the group file.

### 3. Build & check

```bash
hugo server -D
# open http://localhost:1313
# pages appear at /pahami/nama-grup/ and /menghafal/nama-grup/
```

No new markdown files needed.

---

## Adding a New Amalan (to an existing group)

Edit `data/groups/<group-id>.json` and append to `cards`:

### Card types

| `type` | Purpose | Menghafal | Key fields |
|--------|---------|-----------|------------|
| `bacaan` | Doa / dzikir to memorize | Yes (default) | `arabic`, `latin`, `translation`, optional `background`/`body` |
| `guidance` | Explanation / steps only (markdown) | No | `body` (markdown), `source` |
| `personal` | User note (textarea → localStorage) | No | `body` (optional intro), `personal: true` |

```json
{
  "id": "unique-id",
  "title": "Nama Amalan",
  "type": "bacaan",
  "arabic": "النص العربي",
  "latin": "Transliterasi latin",
  "translation": "Arti dalam Bahasa Indonesia",
  "background": "Asal usul dan konteks (atau gunakan body markdown)",
  "source": "Qur'an / Hadits reference",
  "category": "category-name",
  "menghafal": true
}
```

Guidance example:

```json
{
  "id": "syarat-taubat",
  "title": "Syarat Taubat Nasuha",
  "type": "guidance",
  "body": "Teks **markdown** multi-baris.\n\n1. Langkah satu\n2. Langkah dua",
  "source": "QS. An-Nur: 31",
  "category": "taubat",
  "menghafal": false
}
```

| Field | Required | Notes |
|-------|----------|--------|
| `id`, `title`, `type` | yes | `type`: `bacaan` \| `guidance` \| `personal` |
| `arabic` / `latin` / `translation` | for `bacaan` | Core memorization content |
| `body` | for `guidance` / `personal` | Markdown (lists, bold, italics). Prefer over plain `background` |
| `background` | optional | Plain/markdown fallback if `body` absent |
| `menghafal` | no | Default true for `bacaan`. Always false for `guidance` / `personal` |
| `personal` | for type personal | Enables textarea saved to `localStorage` |

Then update `count` for that group in `data/amalan.json` (total cards, including pahami-only).

### Content guidelines
- Accurate Arabic with proper diacritics
- Reliable sources (Qur'an, authentic hadits)
- Clear Indonesian translation and background
- Unique `id` within the whole project (kebab-case)
- Use `type: "guidance"` or `"menghafal": false` for pahami-only content

---

## Development Setup

### Prerequisites
- **Hugo Extended v0.123+** (Content Adapters; CI uses 0.128+)
- Optional: Node.js for extra tooling

### Local development

```bash
git clone https://github.com/tegarimansyah/dzikir.git
cd dzikir

hugo server -D
# http://localhost:1313
```

### Production build

```bash
hugo --minify
# output in public/
```

---

## Code Style

- Follow existing template structure under `themes/dzikir-theme/layouts/`
- Prefer **server-side rendering** from page params / `site.Data` — avoid `fetch()` of content JSON
- Keep interactive JS (search, favorites, story navigation) client-side only
- Responsive / mobile-first

### Commit messages
- `feat:`, `fix:`, `docs:`, `refactor:`, `content:` prefixes preferred

---

## Project Structure

```
dzikir/
├── content/
│   ├── menghafal/          # Content adapter (no stub .md pages)
│   └── pahami/             # Content adapter (no stub .md pages)
├── data/
│   ├── amalan.json         # Group index
│   └── groups/             # Per-group JSON (cards)
├── themes/
│   └── dzikir-theme/           # Hugo theme
│       ├── layouts/        # Hugo templates (SSR)
│       └── static/         # CSS, images, assets
├── static/                 # Site-wide static files (CNAME, etc.)
├── .github/
│   └── ISSUE_TEMPLATE/
└── hugo.toml
```

---

## License

By contributing, you agree that your contributions are licensed under the same license as the project.

## Questions?

- Open an issue with the appropriate template
- Check README and existing discussions

Contributors are credited in the project. Thank you — 🤲
