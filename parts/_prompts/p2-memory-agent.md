````text
Bauen Sie aus der Tabelle in begriffe.md ein Memory-Spiel.
Ziel: Lernende decken je zwei Karten auf und finden zu jedem Begriff die passende Definition. Bei jedem gefundenen Paar erscheint die Definition noch einmal ganz; am Ende stehen die Zahl der Versuche und ein Knopf „Neu mischen“.

Technische Abnahmekriterien:
- Eine einzige HTML-Datei, kein externer Code, keine Bilder oder Schriften aus dem Netz. Sie muss offline und eingebettet in einem iframe laufen.
- Alle Inhalte stehen oben in einem Block `const DATEN = { … };` zwischen den Kommentaren /* ===== DATEN: Nur diesen Block ändern ===== */ und /* ===== ENDE DATEN ===== */. Der Programmcode darunter liest nur aus DATEN.
- Alles Klickbare ist ein <button> und mit der Tastatur bedienbar; Rückmeldungen stehen in einem Bereich mit aria-live="polite".
- Auf einem Handy (360 px Breite) gut bedienbar, ohne seitliches Scrollen.
- Die Datei meldet ihre Höhe an die einbettende Seite: window.parent.postMessage({typ: "iframe-hoehe", hoehe: document.documentElement.scrollHeight}, "*") nach dem Laden, bei Größenänderung und nach jeder Antwort.
- Oberfläche auf Deutsch in der Sie-Form, sachlich, ohne Konfetti, Sounds oder dekorative Animationen.
- Jede Rückmeldung erklärt in einem Satz, warum eine Antwort stimmt oder nicht.

Arbeitsschritte:
1. Speichern Sie das Spiel als interactions/spiel-01.html (die vorhandene Beispieldatei wird ersetzt).
2. Passen Sie in lehreinheit.qmd im ersten Abschnitt nur den Titel des Kastens „Lernspiel: …“ und den Satz darunter an. Die iframe-Zeile bleibt, wie sie ist.
3. Rendern Sie mit `quarto render` und melden Sie mir Fehler oder Warnungen in einfachen Worten.
Ändern Sie keine anderen Dateien.
````
