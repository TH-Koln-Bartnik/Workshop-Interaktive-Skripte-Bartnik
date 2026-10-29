# Workshop-Vorlage: Interaktives Skript mit Quarto

Eine vollständige Quarto-Buch-Vorlage mit Platzhaltern für alle wichtigen
Elemente. Entstanden für den Workshop „Interaktive Skripte mit KI erstellen"
(TH Köln, hdw nrw).

## Was ist drin?

```
vorlage-skript/
├── _quarto.yml             # Buch-Konfiguration (TH-Köln, Hover, APA)
├── _brand.yml              # TH-Köln-Farben und -Schriften
├── styles.scss             # SCSS-Ergänzungen (kantig, Magenta-Akzente)
├── references.bib          # Zotero-Bibliographie (Beispiele)
├── index.qmd               # Landing Page mit Platzhaltern
├── parts/
│   ├── 01-beispielkapitel.qmd   # ZEIGT ALLE ELEMENTE (Bilder,
│   │                            # Tabellen, Cross-Refs, iFrames,
│   │                            # interaktive Charts, Zitate)
│   └── 02-mein-kapitel.qmd      # Leeres Kapitel zum Befüllen
├── appendix/
│   └── literatur.qmd       # Konsolidierte Quellenliste
├── images/                 # Logos, Screenshots, Grafiken (PNG/JPG/SVG)
│   └── platzhalter.png     # Beispielbild
├── interactions/           # HTML-Widgets (Lernspiele, Quizze)
│   └── beispiel-quiz.html  # Einfaches Multiple-Choice-Quiz
├── include/                # Wiederverwendbare qmd-Schnipsel
├── data/                   # CSV/JSON für interaktive Charts
│   └── beispiel-daten.csv  # Beispiel-Datensatz
└── .gitignore              # Build-Caches und LaTeX-Reste
```

## In drei Schritten zum eigenen Skript

1. **Entpacken** und in RStudio öffnen: **File → New Project → Existing Directory** → den entpackten Ordner wählen.
2. **Inhalte ersetzen** in `parts/02-mein-kapitel.qmd` (leerer Rahmen) oder in `index.qmd`. Die Beispielelemente in `parts/01-beispielkapitel.qmd` zeigen, wie was geht — kopieren und anpassen.
3. **Render und Push**: im Terminal `quarto render` (oder Knopf „Render Book"), dann GitHub Desktop Commit + Push.

## Was die Platzhalter enthalten

`parts/01-beispielkapitel.qmd` ist die wichtigste Datei zum Lernen — sie zeigt jeweils ein konkretes Beispiel für:

- **Lernziel-Box** mit Aufzählung
- **Citation** im APA-Format mit Hover-Tooltip (`[@key]`)
- **Bild** mit Caption und Label (`#fig-key`)
- **Markdown-Tabelle** mit Caption und Label (`#tbl-key`)
- **Cross-Reference** auf Bild und Tabelle (`@fig-key`, `@tbl-key`)
- **Interaktives Diagramm** aus R-Chunk mit plotly (Live-Render)
- **iFrame** für externes oder eigenes HTML-Widget
- **Callout-Tip** (Mach-mit-Block)
- **Callout-Warning** (Trouble-Shooting)
- **Tutor-Link** zum vorbereiteten ChatGPT
- **Bibliographie-Section** am Kapitelende (`# Literatur`)

## Voraussetzungen

- [Quarto](https://quarto.org) Version 1.5+
- R + RStudio Desktop
- R-Pakete: `install.packages(c("plotly", "tibble", "knitr"))`
- GitHub Desktop für Push auf GitHub Pages

## KI-Tutor zur Unterstützung

Während der Bearbeitung hilft der vorbereitete GPT:

[Tutor „Interaktive Skripte"](https://chatgpt.com/g/g-69fec93348108191af1ffb8ce0cf6712-tutor-interaktive-skripte)

## Lizenz

Inhalte: CC BY-SA 4.0. Code: MIT. Frei für eigene Lehr- und Lernzwecke.
