# Starter-Vorlage: eine interaktive Lehreinheit

Diese Vorlage ist ein fertig eingerichtetes Quarto-Skript mit einer Beispiel-Lehreinheit. Sie ersetzen nur noch Inhalte: Texte, Bilder und Lernspiele. Ordner, Einstellungen, Zitierstil und Vorab-Check sind schon fertig.

## In drei Schritten zum ersten Ergebnis

1. **Öffnen:** ZIP entpacken. In RStudio *File → Open Project…* und die Datei `starter-lehreinheit.Rproj` wählen.
2. **Rendern:** Im Reiter *Terminal* `quarto preview` eingeben. Der Browser zeigt das Skript mit Memory, Zuordnungsspiel und Lern-Check. Die Vorschau aktualisiert sich bei jedem Speichern; **Strg+C** im Terminal beendet sie.
3. **Ersetzen:** Gelbe Kästen „ERSETZEN“ im Skript zeigen, was Sie austauschen. Die passenden KI-Prompts stehen in `PROMPTS.md`.

## Was wo liegt

```
starter-lehreinheit/
├── lehreinheit.qmd      Ihre Lehreinheit: Szene, Vorab-Check, 3 Abschnitte, Lern-Check
├── index.qmd            Startseite
├── literatur.qmd        Literaturliste (wird automatisch gefüllt)
├── images/              abb-01.png bis abb-03.png: unter gleichem Namen ersetzen
├── interactions/        spiel-01.html bis spiel-03.html: unter gleichem Namen ersetzen
├── material/            Ihr Rohmaterial für die KI (wird nicht veröffentlicht)
├── references.bib       Quellen: durch Ihren Zotero-Export ersetzen
├── PROMPTS.md           alle Prompts, je für Chat und für Agent
├── _quarto.yml          Einstellungen: nur Zeilen mit ← ändern
├── include/             Technik für Vorab-Check und Spielhöhe: nicht ändern
└── apa.csl, styles.scss Zitierstil und Farben
```

## Die drei Tauschregeln

- **Bild tauschen:** Neue Datei als `images/abb-01.png` speichern (alte überschreiben). Der Verweis `@fig-abb-01` im Text bleibt gültig.
- **Spiel tauschen:** Neue Datei als `interactions/spiel-01.html` speichern. Die iframe-Zeile im Text bleibt, wie sie ist.
- **Nur Inhalte eines Spiels ändern:** In der HTML-Datei ausschließlich den Block zwischen `DATEN` und `ENDE DATEN` bearbeiten.

## Hilfe

Workshop-Skript: <https://th-koln-bartnik.github.io/Workshop-Interaktive-Skripte-Bartnik/>

Lizenz der Vorlage: Inhalte CC BY-SA 4.0, Code MIT. Der Vorab-Check stammt aus Bartnik, *Generative KI als Hilfe zum Lehren und Lernen* (<https://th-koln-bartnik.github.io/genai4teaching/>). Zitierstil `apa.csl`: Citation Style Language, CC BY-SA 3.0.
