# Contribution Guidelines

Thank you for your interest in contributing to Muslim Flashcard!

## How to Contribute

### Reporting Issues
- Use GitHub issue templates for bugs, feature requests, or dzikir requests
- Include clear steps to reproduce and screenshots when possible

### Content Contributions
1. **Dzikir request issue** — use the `[DZIKIR]` template
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
├── doa.json                 # Index of all groups (source of truth for listing)
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
| `data/doa.json` | Index only: `id`, `title`, `description`, `category`, `icon`, `color`, `file`, `count` |
| `data/groups/<id>.json` | Full group + `cards[]` (arabic, latin, translation, background, source) |
| `_content.gotmpl` | Registers virtual pages from JSON (Hugo ≥ 0.123) |

Both **Pahami** and **Menghafal** share the same group JSON; only layouts differ.

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

Add an entry to `data/doa.json` → `groups`:

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

## Adding a New Doa (to an existing group)

Edit `data/groups/<group-id>.json` and append to `cards`:

```json
{
  "id": "unique-id",
  "title": "Nama Doa",
  "arabic": "النص العربي",
  "latin": "Transliterasi latin",
  "translation": "Arti dalam Bahasa Indonesia",
  "background": "Asal usul dan konteks",
  "source": "Qur'an / Hadits reference",
  "category": "category-name"
}
```

Then update `count` for that group in `data/doa.json`.

### Content guidelines
- Accurate Arabic with proper diacritics
- Reliable sources (Qur'an, authentic hadits)
- Clear Indonesian translation and background
- Unique `id` within the whole project (kebab-case)

---

## Development Setup

### Prerequisites
- **Hugo Extended v0.123+** (Content Adapters; CI uses 0.128+)
- Optional: Node.js for extra tooling

### Local development

```bash
git clone https://github.com/tegarimansyah/muslim-flashcard.git
cd muslim-flashcard

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

- Follow existing template structure under `themes/muslim-flashcard-theme/layouts/`
- Prefer **server-side rendering** from page params / `site.Data` — avoid `fetch()` of content JSON
- Keep interactive JS (search, favorites, story navigation) client-side only
- Responsive / mobile-first

### Commit messages
- `feat:`, `fix:`, `docs:`, `refactor:`, `content:` prefixes preferred

---

## Project Structure

```
muslim-flashcard/
├── content/
│   ├── menghafal/          # Content adapter (no stub .md pages)
│   └── pahami/             # Content adapter (no stub .md pages)
├── data/
│   ├── doa.json            # Group index
│   └── groups/             # Per-group JSON (cards)
├── themes/
│   └── muslim-flashcard-theme/
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
