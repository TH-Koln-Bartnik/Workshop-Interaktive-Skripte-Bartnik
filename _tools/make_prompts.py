#!/usr/bin/env python3
"""Erzeugt alle Workshop-Prompts aus einer Quelle.

Ausgabe:
  parts/_prompts/<id>.md                 Codeblock zum Einbinden mit {{< include >}}
  _vorlage-lehreinheit/PROMPTS.md        Sammlung für die Starter-Vorlage
  downloads/prompts-workshop.txt         alle Prompts als Textdatei

Aufruf aus dem Projektordner:  python3 _tools/make_prompts.py
Wer einen Prompt ändert, ändert ihn NUR hier und ruft das Skript erneut auf.
"""
from pathlib import Path

BASIS = "https://th-koln-bartnik.github.io/Workshop-Interaktive-Skripte-Bartnik"
FORSCHUNG = f"{BASIS}/downloads/interaktionstypen-forschung.md"

TECHNIK = """Technische Abnahmekriterien:
- Eine einzige HTML-Datei, kein externer Code, keine Bilder oder Schriften aus dem Netz. Sie muss offline und eingebettet in einem iframe laufen.
- Alle Inhalte stehen oben in einem Block `const DATEN = { … };` zwischen den Kommentaren /* ===== DATEN: Nur diesen Block ändern ===== */ und /* ===== ENDE DATEN ===== */. Der Programmcode darunter liest nur aus DATEN.
- Alles Klickbare ist ein <button> und mit der Tastatur bedienbar; Rückmeldungen stehen in einem Bereich mit aria-live="polite".
- Auf einem Handy (360 px Breite) gut bedienbar, ohne seitliches Scrollen.
- Die Datei meldet ihre Höhe an die einbettende Seite: window.parent.postMessage({typ: "iframe-hoehe", hoehe: document.documentElement.scrollHeight}, "*") nach dem Laden, bei Größenänderung und nach jeder Antwort.
- Oberfläche auf Deutsch in der Sie-Form, sachlich, ohne Konfetti, Sounds oder dekorative Animationen.
- Jede Rückmeldung erklärt in einem Satz, warum eine Antwort stimmt oder nicht."""

PROMPTS = {}

PROMPTS["p1-grundbegriffe-chat"] = ("Grundbegriffe sammeln (Chat)", """Sie helfen mir, die Grundbegriffe für eine Lehreinheit zusammenzustellen. Stellen Sie mir zuerst nacheinander vier Fragen, jede als Multiple Choice mit den Optionen a) bis d) und „e) eigene Angabe“. Warten Sie nach jeder Frage auf meine Antwort.

1. Fach und Thema der Einheit. Wenn ich nur das Fach nenne, schlagen Sie vier typische Themen vor.
2. Woher kommen die Begriffe? a) aus einer Quelle, die ich gleich einfüge oder hochlade; b) aus Ihrem Wissen; c) Ihre Vorschläge, abgeglichen mit meiner Quelle; d) aus meinem Vorlesungsskript als Datei.
3. Niveau: a) erstes Semester; b) fortgeschrittenes Bachelorstudium; c) Master; d) Weiterbildung.
4. Anzahl der Begriffe: a) 6; b) 8; c) 10; d) 12.

Danach erstellen Sie eine Tabelle mit den Spalten: Begriff | Definition | typische Verwechslung | Fundstelle.

Regeln:
- Definitionen in eigenen Worten, höchstens 15 Wörter, ohne den Begriff selbst zu wiederholen.
- Kein Begriff steckt in der Definition eines anderen, sonst verrät das Spiel die Lösung.
- Mit Quelle: nur Begriffe, die in der Quelle vorkommen; Fundstelle mit Seite oder Abschnitt.
- Ohne Quelle: In der Spalte Fundstelle steht „bitte prüfen“. Nennen Sie kein Lehrbuch, das Sie nicht sicher kennen.

Fragen Sie zum Schluss, ob ich Begriffe tauschen, kürzen oder ergänzen will.""")

PROMPTS["p1-grundbegriffe-agent"] = ("Grundbegriffe sammeln (Agent)", """Im verbundenen Ordner liegt meine Starter-Vorlage für ein Quarto-Skript. Ich möchte die Grundbegriffe für meine Lehreinheit zusammenstellen.

Stellen Sie mir zuerst nacheinander vier Fragen als Multiple Choice (a bis d, dazu „eigene Angabe“) und warten Sie jeweils auf meine Antwort:
1. Fach und Thema der Einheit (bei bloßer Fachangabe: vier typische Themen vorschlagen);
2. Quelle der Begriffe: a) eine Datei, die ich in den Ordner material/ lege; b) Ihr Wissen; c) beides abgeglichen; d) eine Webseite, deren Adresse ich nenne;
3. Niveau: a) erstes Semester; b) fortgeschrittenes Bachelorstudium; c) Master; d) Weiterbildung;
4. Anzahl: a) 6; b) 8; c) 10; d) 12.

Legen Sie danach die Datei begriffe.md im Projektordner an, mit einer Tabelle: Begriff | Definition | typische Verwechslung | Fundstelle.
Regeln: Definitionen in eigenen Worten, höchstens 15 Wörter, ohne den Begriff selbst; kein Begriff steckt in einer anderen Definition; mit Quelle nur Begriffe aus der Quelle samt Seite oder Abschnitt; ohne Quelle steht bei Fundstelle „bitte prüfen“.
Ändern Sie keine anderen Dateien. Zeigen Sie mir die Tabelle und fragen Sie, ob ich etwas tauschen will.""")

PROMPTS["p2-memory-chat"] = ("Memory-Spiel bauen (Chat)", f"""Bauen Sie aus der Tabelle oben ein Memory-Spiel.
Ziel: Lernende decken je zwei Karten auf und finden zu jedem Begriff die passende Definition. Bei jedem gefundenen Paar erscheint die Definition noch einmal ganz; am Ende stehen die Zahl der Versuche und ein Knopf „Neu mischen“.

{TECHNIK}

Geben Sie nur den vollständigen Code in einem einzigen Codeblock aus.""")

PROMPTS["p2-memory-agent"] = ("Memory-Spiel bauen und einbauen (Agent)", f"""Bauen Sie aus der Tabelle in begriffe.md ein Memory-Spiel.
Ziel: Lernende decken je zwei Karten auf und finden zu jedem Begriff die passende Definition. Bei jedem gefundenen Paar erscheint die Definition noch einmal ganz; am Ende stehen die Zahl der Versuche und ein Knopf „Neu mischen“.

{TECHNIK}

Arbeitsschritte:
1. Speichern Sie das Spiel als interactions/spiel-01.html (die vorhandene Beispieldatei wird ersetzt).
2. Passen Sie in lehreinheit.qmd im ersten Abschnitt nur den Titel des Kastens „Lernspiel: …“ und den Satz darunter an. Die iframe-Zeile bleibt, wie sie ist.
3. Rendern Sie mit `quarto render` und melden Sie mir Fehler oder Warnungen in einfachen Worten.
Ändern Sie keine anderen Dateien.""")

PROMPTS["p3-auswahl"] = ("Interaktionen auswählen (Chat und Agent)", f"""Lesen Sie zuerst diese Zusammenfassung der Forschung zu Interaktionstypen und stützen Sie Ihre Vorschläge darauf: {FORSCHUNG}
Falls Sie die Seite nicht öffnen können, sagen Sie es; dann füge ich den Text ein.

Meine Lehreinheit:
- Fach und Thema: [ … ]
- Lernziel dieser Einheit: [ … ]
- Eine typische Fehlvorstellung der Studierenden: [ … ]
- Niveau: [ erstes Semester / Bachelor / Master / Weiterbildung ]

Schlagen Sie mir fünf Interaktionen vor, die sich gut in ein Quarto-Skript einbauen lassen. Für jede:
1. Typ aus der Palette der Zusammenfassung;
2. konkrete Umsetzung zu meinem Thema in zwei Sätzen;
3. welches Lernprinzip sie nutzt, mit der Quelle aus der Zusammenfassung;
4. Einbauweg: Quarto-Kasten ohne Code, eigene HTML-Datei per iframe, H5P-Inhalt oder fremde Simulation;
5. Aufwand: klein, mittel oder groß.

Bevorzugen Sie Interaktionen, bei denen Lernende etwas erzeugen (vorhersagen, begründen, zuordnen mit Begründung), vor bloßem Klicken. Mindestens eine Option kommt ohne Programmierung aus. Sagen Sie offen, wenn eine Idee vor allem Dekoration wäre.
Fragen Sie mich am Ende per Multiple Choice, welche zwei Interaktionen ich umsetzen will.""")

PROMPTS["p4-spiel-chat"] = ("Eigene Interaktion bauen (Chat)", f"""Bauen Sie die Interaktion, die wir ausgewählt haben, nach dieser Konzeptkarte:
- Lernziel: [ … ]
- Fehlvorstellung, die sichtbar werden soll: [ … ]
- Interaktionstyp: [ z. B. Vorhersage mit Auflösung, Zuordnen mit Begründung, Sortieren, Fehler finden, Lückentext ]
- Was die Lernenden tun: [ … ]
- Rückmeldung: [ was nach jeder Antwort erklärt wird ]
- Inhalte: [ Fragen, Begriffe oder Werte, oder: „Entwerfen Sie die Inhalte selbst und zeigen Sie sie mir zuerst als Tabelle.“ ]

{TECHNIK}

Geben Sie nur den vollständigen Code in einem einzigen Codeblock aus.""")

PROMPTS["p4-spiel-agent"] = ("Eigene Interaktion bauen und einbauen (Agent)", f"""Bauen Sie die Interaktion nach dieser Konzeptkarte:
- Lernziel: [ … ]
- Fehlvorstellung, die sichtbar werden soll: [ … ]
- Interaktionstyp: [ … ]
- Was die Lernenden tun: [ … ]
- Rückmeldung: [ … ]
- Inhalte: [ … oder: „Entwerfen Sie die Inhalte und zeigen Sie sie mir zuerst als Tabelle, bevor Sie programmieren.“ ]

{TECHNIK}

Arbeitsschritte:
1. Speichern Sie das Spiel als interactions/spiel-02.html (bzw. spiel-03.html, wenn ich das sage).
2. Passen Sie in lehreinheit.qmd nur Titel und Einleitungssatz des zugehörigen Lernspiel-Kastens an.
3. Rendern Sie mit `quarto render` und melden Sie Fehler in einfachen Worten.
Ändern Sie keine anderen Dateien.""")

MUSTER = """```
## Titel des Abschnitts {#sec-abschnitt-1}

::: {.einschaetzung #ez-1}
Aussage, der man zustimmen oder widersprechen kann.

[Auflösung im ersten Abschnitt](#sec-abschnitt-1){.ez-verweis}
:::

::: {.callout-tip .ez-pruefen title="Ihre Einschätzung prüfen"}
*„Aussage wörtlich wiederholt“* []{.ez-ihre data-ez="ez-1"}

**Auflösung: ja/nein/teils.** Begründung in zwei Sätzen.
:::
```"""

PROMPTS["p5-rahmen-chat"] = ("Die Einheit rahmen (Chat)", f"""Ich baue eine Lehreinheit in Quarto. Thema: [ … ]. Niveau: [ … ]. Die drei Abschnitte heißen: [ 1 … / 2 … / 3 … ].
Hier ist mein Rohmaterial (Text, Stichpunkte oder Folien): [ einfügen ]

Schreiben Sie mir in genau dieser Quarto-Syntax (Muster siehe unten):
1. eine Szene aus dem Fach in vier bis fünf Sätzen: eine Person, eine konkrete Situation, ein offenes Problem;
2. drei Aussagen für den Vorab-Check (Kennungen ez-1 bis ez-3), je eine zu einer typischen Fehlvorstellung pro Abschnitt, so formuliert, dass man zustimmen oder widersprechen kann;
3. drei Lernziele mit beobachtbaren Verben;
4. zu jeder Aussage den Prüfkasten „Ihre Einschätzung prüfen“ mit Auflösung in zwei Sätzen;
5. drei Kernaussagen, je eine pro Lernziel;
6. Lernfragen in drei Stufen: Wiederholen, Anwenden, Beurteilen (je ein bis zwei Fragen).

Erfinden Sie keine Studien oder Zahlen. Wo eine Quelle nötig wäre, schreiben Sie [QUELLE?].

Muster:
{MUSTER}""")

PROMPTS["p5-rahmen-agent"] = ("Die Einheit rahmen (Agent)", """Öffnen Sie lehreinheit.qmd. Mein Thema: [ … ]. Niveau: [ … ]. Mein Rohmaterial liegt in material/ [ Dateiname ].

Ersetzen Sie die Beispielinhalte überall dort, wo ein gelber Kasten „ERSETZEN“ steht: Titel, Szene, die drei Aussagen des Vorab-Checks, Lernziele, die drei Prüfkästen „Ihre Einschätzung prüfen“, Kernaussagen und Lernfragen. Die Abschnittstexte selbst lassen Sie stehen; die schreibe ich.

Regeln:
- Kennungen (#ez-1 bis #ez-3, #sec-abschnitt-1 bis 3, #fig-abb-01 bis 03) und alle iframe-Zeilen bleiben unverändert.
- Löschen Sie jeden gelben ERSETZEN-Kasten, dessen Block Sie erledigt haben.
- Erfinden Sie keine Studien oder Zahlen; wo eine Quelle nötig wäre, schreiben Sie [QUELLE?].
- Rendern Sie danach mit `quarto render` und nennen Sie mir die Stellen, an denen ich nachbessern sollte.""")


def codeblock(text: str) -> str:
    return "````text\n" + text.strip() + "\n````\n"


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    ziel = root / "parts" / "_prompts"
    ziel.mkdir(parents=True, exist_ok=True)
    for pid, (_, text) in PROMPTS.items():
        (ziel / f"{pid}.md").write_text(codeblock(text), encoding="utf-8")

    teile = ["# Prompts für Ihre Lehreinheit\n",
             "Jeder Prompt steht in zwei Fassungen: **Chat** (ChatGPT, Claude, Gemini, Academiccloud: Antwort kopieren und als Datei speichern) "
             "und **Agent** (Claude Desktop oder Codex mit verbundenem Projektordner: Der Agent schreibt die Dateien selbst).\n",
             "Text in eckigen Klammern `[ … ]` ersetzen Sie durch Ihre Angaben.\n",
             f"Erklärungen und Reihenfolge: {BASIS}/\n"]
    for pid, (titel, text) in PROMPTS.items():
        teile.append(f"\n## {titel}\n\n" + codeblock(text))
    (root / "_vorlage-lehreinheit" / "PROMPTS.md").write_text("\n".join(teile), encoding="utf-8")

    txt = []
    for pid, (titel, text) in PROMPTS.items():
        txt.append("=" * 70 + f"\n{titel}\n" + "=" * 70 + "\n" + text.strip() + "\n")
    (root / "downloads" / "prompts-workshop.txt").write_text("\n".join(txt), encoding="utf-8")
    print(f"{len(PROMPTS)} Prompts geschrieben.")


if __name__ == "__main__":
    main()
