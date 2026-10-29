# Interaktive Skripte mit KI erstellen

Werkstatt-Skript zum Workshop an der TH Köln (hdw nrw, 26-157-P-Z).
Referent: Prof. Dr. Roman Bartnik.

Dieses Repository ist gleichzeitig **Lehrmaterial** und **Vorlage** —
die Teilnehmenden bauen im Workshop ein Skript dieser Art selbst auf.

## Schnellstart (für Lesende)

Online-Version: <https://th-koln-bartnik.github.io/Workshop-Interaktive-Skripte-Bartnik/>

## Schnellstart (für die Workshop-Vorbereitung)

```bash
# Build
quarto render

# Preview
quarto preview

# Publish nach GitHub Pages
quarto publish gh-pages
```

## Struktur (Lakens-Konvention)

```
.
├── _quarto.yml             # Buch-Konfiguration
├── _brand.yml              # TH Köln Farben & Typografie
├── styles.scss             # SCSS-Ergänzungen (TH-Köln-Brand)
├── references.bib          # Zotero-Export
├── index.qmd               # Landing Page mit Lernzielen
├── parts/                  # Teil 0 (Quick-Start, Galerie), Kapitel 1–12
├── appendix/               # Troubleshooting, Tutor-Prompt, Reviewer-Prompt
├── images/                 # Logos, Screenshots, statische Grafiken
├── interactions/           # HTML-Widgets (Lernspiele, Workflow-Animation, Beispiel-Widget)
├── include/                # Wiederverwendbare qmd-Partials
└── data/                   # CSV/JSON-Daten für interaktive Charts
```

## Lizenz

Inhalte: CC BY-SA 4.0. Code: MIT.
