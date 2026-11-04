# Übergabe-Kontext — Kapitel 7 Slides & Bild-Einfügung

Stand: 2026-05-12. Diese Notiz brieft eine neue Claude-Instanz auf den Stand der Arbeiten.

## Projektkontext

Workshop „Interaktive Skripte mit KI erstellen", TH Köln Gummersbach, gehalten am 11.05.2026 von Prof. Dr. Roman Bartnik. Workspace-Ordner:

```
C:\Users\roman\My Tresors\0_Roman Arbeit\0_GenAI\2-Teach\31-Workshop-Interaktive-Skripte-2026-05-11
```

Es ist ein Quarto-Buchprojekt mit dieser Ordnerlogik:

- `parts/` — Skript-Kapitel als `.qmd`-Dateien
- `slides/` — Reveal.js-Decks zu einzelnen Blöcken
- `interactions/` — eigenständige HTML-Spiele für iFrame-Einbettung
- `images/` — alle PNGs/JPGs (aus qmd referenziert als `../images/dateiname.png`)
- `docs/` — gerenderte Site (nicht direkt editieren)
- `_quarto.yml` — Build-Konfiguration

## Wichtige Datei-Identitäten

- **Skript-Kapitel „Block 7 — iFrames, Spiele und KI-Tutor"**: `parts/05-iframes-tutor.qmd`. Achtung: Datei heißt `05-…`, ist im Buch aber als Block 7 nummeriert. Wenn der User von „Skript 5" oder „Kapitel 7" spricht, meint er dieselbe Datei.
- **Slide-Deck zu Kapitel 7**: `slides/kap07-iframes-tutor.qmd` — in dieser Session neu erstellt.
- **Format-Vorlage für alle Slides**: `slides/intro-vorstellung.qmd`. Format: 1280×720, Zwei-Spalten-Layout (55/45), Bullets links als `::: incremental`, Bild rechts als `::: {.fragment}`, Speaker-Notes als `::: notes`, Schlussfolie auf TH-Rot `#c81e0f`, Hidden Slide mit DALL·E-Bild-Prompts am Ende.

## Was in dieser Session getan wurde

### 1. Plan zur Bild-Einfügung in `parts/05-iframes-tutor.qmd` (NICHT umgesetzt)

Vorschlag liegt vor, drei Freigabe-Fragen sind beim User offen. Geplante Einfügungen:

| # | Position im qmd | Bild | Begründung |
|---|---|---|---|
| 1 | Nach „Worum es im Kern geht" (~Z. 16) | `tool-metaphor-genai.png` | Werkzeug-Metapher als Anker für ganzes Kapitel |
| 2 | Vor „Drei Wege, ein Spiel einzubauen" (~Z. 61) | `digitalization-to-genai-timeline-not-so-new.png` | Historische Einordnung der Optionen |
| 3 | Anfang „KI-Tutor als Link" (~Z. 110) | `centaur-genai.png` | Mollick-Centaur-Metapher |
| 4 | Vor „Galerie: zehn didaktische Ansätze" (~Z. 163) | `teaching-new-genai-processes.png` | Vielfalt didaktischer Wege |
| 5 | Bei „Wann **kein** KI-Tutor?" (~Z. 155) | `jagged-frontier-genai.png` | Dell'Acqua zerklüftete Grenze |

Bild-Syntax (Quarto): `![Caption als ganzer Satz mit didaktischer Aussage.](../images/datei.png){#fig-id width=70% fig-align="center"}`

**Drei offene Entscheidungen vom User:**

1. Bild-Auswahl so übernehmen oder einzelne tauschen? (Alternativen im Bestand: `cyborg-genai.png`, `augmentation-hope-genai.png`, `rag-hope-genai-bookshelf.png`, `effectiveness-rise-by-genai-hope.png`.)
2. Position 5 bei „Wann kein KI-Tutor?" oder alternativ vor der Reaktivierung („Aktiv auslaufen lassen")?
3. Captions mit Quellenhinweis (DOI/URL) oder schlicht ohne Quelle?

### 2. Slide-Deck `slides/kap07-iframes-tutor.qmd` erstellt (UMGESETZT)

12 Inhalts-Folien plus 1 Hidden Slide am Ende. Reihenfolge:

1. Aktivität schlägt Konsum — auch im Skript
2. Ein iFrame ist ein Mini-Browser in Ihrer Seite
3. Live: drei Prinzipien per Drag-and-Drop
4. Drei Wege ein Spiel einzubauen — eine Empfehlung für heute (Tabelle)
5. Der KI-Tutor läuft im zweiten Tab — nicht im iFrame
6. Drei Hosting-Varianten — heute reicht Option 1
7. Live: Tutor öffnen, Frage stellen, Antwort lesen
8. Drei Situationen, in denen Sie es lassen sollten
9. Zehn Spiele, eine Progression: Verstehen → Prüfen
10. Mach mit — eines der zehn als Bauplan übernehmen
11. Reaktivierung: fünf Behauptungen, Wahr oder Falsch? (iFrame `../interactions/wahr-falsch-kap07.html`)
12. Aktivität schlägt Konsum (Schlussfolie TH-Rot, Tutor-Link)
13. Hidden: Bild-Generierungs-Prompts

**Bilder-Mix**: drei aus dem Bestand (`centaur-genai.png`, `jagged-frontier-genai.png`, `teaching-new-genai-processes.png`), sechs noch zu generieren (`kap07-aktivitaet.png`, `kap07-iframe-konzept.png`, `kap07-live-spiel.png`, `kap07-tutor-optionen.png`, `kap07-tutor-demo.png`, `kap07-progression.png`). Vollständige DALL·E-Prompts für die sechs neuen Bilder liegen in der Hidden Slide am Ende des Decks im NYT-editorial-Stil mit der TH-Farbpalette (`#c81e0f` rot, `#b43092` magenta, `#ea5a00` orange).

## Offene To-dos für die nächste Session

1. **Bild-Einfügung Skript 5**: drei User-Entscheidungen abwarten, dann Edits in `parts/05-iframes-tutor.qmd` vornehmen.
2. **Sechs neue Slide-Bilder generieren**: Prompts aus der Hidden Slide von `slides/kap07-iframes-tutor.qmd` an DALL·E/Imagen geben, PNGs unter `images/kap07-*.png` ablegen.
3. **Render-Test der Slides**: `quarto render slides/kap07-iframes-tutor.qmd` ausführen, prüfen, ob die Datei `interactions/wahr-falsch-kap07.html` für Folie 11 existiert (in dieser Session nicht verifiziert).
4. **Tutor-Link prüfen**: Der ChatGPT-Custom-GPT-Link auf Folie 12 (`https://chatgpt.com/g/g-69fec93348108191af1ffb8ce0cf6712-tutor-interaktive-skripte`) wurde aus dem Skript übernommen — falls inzwischen ein anderer Tutor genutzt wird, austauschen.

## User-Präferenzen (Auszug für diese Arbeit)

- Sprache: Deutsch für alle Workshop-Inhalte
- Slides immer im TH-Köln-Stil mit Action-Titeln (Aussage-Sätze, keine Themen-Labels), Speaker-Notes als vollständige Sätze, Quellenangaben auf den Folien
- Vor Dokumenten über ~500 Wörter immer erst Outline vorschlagen, Freigabe abwarten
- Continuous prose statt Bullet-Wüsten, außer wo Struktur tatsächlich trägt (Vergleichstabellen, Handlungsschritte)
- IT-Begriffe immer mit Lay-Sprach-Glosse erläutern (Beispiel: „iFrame = *inline frame*, ein eingebettetes Browser-Fenster im Browser-Fenster")
- Keine Emojis ohne Aufforderung
- Quellen in APA in-text, BibTeX-Block am Ende bei Literatur-Anfragen
- Etymologische Notizen für lateinisch-/griechischstämmige Begriffe sind willkommen

## Im Skript & Slide-Deck bereits zitierte Quellen

- Karpicke & Blunt (2011) — Retrieval Practice
- Fiorella & Mayer (2016) — Generative Learning
- Mollick & Mollick (2023) — Pädagogische Designentscheidungen für KI-Tutoren
- Kasneci et al. (2023) — Large Language Models in Education
- Dell'Acqua et al. (2023) — Jagged Technological Frontier
