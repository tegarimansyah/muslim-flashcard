---
name: amalan-content
description: >
  Create or revise amalan group content for Dzikir with EthiqsHub (doa, dzikir,
  guidance journeys). Use when writing data/groups/*.json, filling empty
  groups, expanding a situation into a taubat/dzikir journey, or when the
  user asks for content that matches the maksiat-berdosa standard.
---

# Amalan Content Skill

Gold standard: `data/groups/maksiat-berdosa.json`.

## When to use

- User wants content for a group under `data/groups/`
- Expanding outline bullets into full cards
- Migrating old cards (arabic-only) to typed cards
- Reviewing whether a card should be pahami-only vs menghafal

## Files to touch

| File | Role |
|------|------|
| `data/groups/<id>.json` | Cards (source of truth) |
| `data/amalan.json` | Group index: sync `count` + description if changed |
| `CONTRIBUTING.md` | Only if schema/docs change |

Never invent Arabic. Research authentic wording; cite sources.

## Card types

| `type` | Menghafal | Required fields | Optional |
|--------|-----------|-----------------|----------|
| `bacaan` | yes (default) | `arabic`, `latin`, `translation` | `background` or `body`, `source` |
| `guidance` | **no** | `body` (markdown) | `source` |
| `personal` | **no** | `personal: true` | `body` intro, `source` |

Rules:

- Always set `"type"` explicitly.
- `guidance` / `personal` → `"menghafal": false`.
- `bacaan` → `"menghafal": true` unless intentionally pahami-only.
- Prefer `body` (markdown) for guidance; use `background` for short bacaan context.
- Omit empty `arabic`/`latin`/`translation` on non-bacaan cards (do not leave `""`).
- Unique `id` kebab-case project-wide.
- `category` on cards can match group theme (e.g. `taubat`, `sakit`).

### JSON shapes

**Bacaan**

```json
{
  "id": "istighfar",
  "title": "Istighfar Dasar",
  "type": "bacaan",
  "menghafal": true,
  "category": "taubat",
  "arabic": "…",
  "latin": "…",
  "translation": "…",
  "background": "Konteks singkat + faidah. Kutip hadits jika relevan.",
  "source": "Hadits Riwayat Muslim (2702)"
}
```

**Guidance (markdown body)**

```json
{
  "id": "syarat-taubat",
  "title": "Syarat Taubat Nasuha",
  "type": "guidance",
  "menghafal": false,
  "category": "taubat",
  "body": "Pembuka hangat.\n\n**Tiga syarat:**\n\n1. **Menyesali** …\n2. **Menghentikan** …\n3. **Bertekad** …\n\n*\"Kutipan ayat/hadits.\"*",
  "source": "QS. An-Nur: 31"
}
```

**Personal (textarea → localStorage)**

```json
{
  "id": "doa-pribadi",
  "title": "Doa Pribadi: Curhat kepada Allah",
  "type": "personal",
  "personal": true,
  "menghafal": false,
  "category": "taubat",
  "body": "Ajakan singkat menulis doa sendiri.",
  "source": "QS. Al-Baqarah: 186"
}
```

## Journey design (situation groups)

Not every group is a flat list of doas. Prefer a **journey** when the situation needs steps:

1. **Orientasi batin** (`guidance`) — hope, conditions, mindset  
2. **Persiapan ritual** (`bacaan` + `guidance`) — e.g. wudhu doa, then how to pray  
3. **Memanggil Allah** (`bacaan`) — Asmaul Husna / short dzikir if relevant  
4. **Inti bacaan** (`bacaan`) — ma'thur doas/dzikirs for the situation  
5. **Personal** (`personal`) — user writes own doa (one card max per group unless needed)  
6. **Sosial / hak orang lain** (`guidance` + optional `bacaan`)  
7. **Amalan lanjutan** (`bacaan` + `guidance`) — daily wirid, sedekah, sabar, etc.

Split “action + recitation” into two cards when one is memorized text and the other is how-to (example: *Doa Setelah Wudhu* vs *Shalat Taubat*).

Merge many tiny non-recitation tips into one guidance card if they share a theme (e.g. daily sin-erasing deeds).

## Research & sources

- Prefer Qur'an, Bukhari, Muslim, Abu Dawud, Tirmidzi, Nasa'i, Ibn Majah with numbers when known.
- For fiqh notes (khusyuk, times of prayer), say “mayoritas ulama” / cite clearly; do not invent rulings.
- Latin: consistent Indonesian transliteration (`'`, `gh`, `sh`, `th`, `dz` as used in maksiat-berdosa).
- Arabic: proper diacritics when possible; verify against a reliable mushaf/hadith text.
- Do **not** pad background with meta-explanations the user did not ask for (e.g. grammar of a phrase) — put that in chat if needed.
- Counts like **100×** belong in title and/or latin/translation when the hadits specifies a count.

## Writing tone (Indonesian)

- Warm, peer-to-peer: “kita”, “Alhamdulillah…”, not lecture-heavy.
- Short paragraphs; markdown lists for steps and named attributes.
- Bold key terms (**Khauf**, **Ya Ghaffar**).
- Italicize short quotes of ayat/hadits.
- Guidance body: actionable; bacaan background: origin + when/why to read (2–4 sentences).

## Workflow

1. Read existing `data/groups/<id>.json` and index entry in `data/amalan.json`.
2. Outline the journey with the user if they only gave rough bullets; confirm order.
3. Research each bacaan (Arabic + source) before writing.
4. Write/update cards with correct `type` / `menghafal`.
5. Set `count` in `data/amalan.json` to `len(cards)`.
6. Align group `description` if the journey scope changed.
7. Sanity-check: only `bacaan` with `menghafal !== false` appear in menghafal (adapter filters `guidance`, `personal`, `menghafal: false`).
8. Optional: `hugo --quiet` to ensure build.

## Checklist before done

- [ ] Every card has `id`, `title`, `type`, `category`
- [ ] Non-bacaan have `menghafal: false` and no empty string fields for arabic/latin
- [ ] Bacaan have arabic + latin + translation + source
- [ ] Guidance uses markdown `body` with clear structure
- [ ] At most one primary `personal` card unless user asks for more
- [ ] `data/amalan.json` `count` matches
- [ ] No unsolicited theological digressions in card text
- [ ] Sources are real and appropriately specific

## Anti-patterns

- Dumping everything as `bacaan` with empty arabic
- Long wall of text without lists
- Mixing how-to shalat and a long Arabic doa in one card
- Setting `menghafal: true` on guidance/personal
- Updating only group JSON without `count`
- Copying user outline wording literally without research
