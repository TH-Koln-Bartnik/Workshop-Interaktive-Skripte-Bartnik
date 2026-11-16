````text
Bauen Sie die Interaktion, die wir ausgewählt haben, nach dieser Konzeptkarte:
- Lernziel: [ … ]
- Fehlvorstellung, die sichtbar werden soll: [ … ]
- Interaktionstyp: [ z. B. Vorhersage mit Auflösung, Zuordnen mit Begründung, Sortieren, Fehler finden, Lückentext ]
- Was die Lernenden tun: [ … ]
- Rückmeldung: [ was nach jeder Antwort erklärt wird ]
- Inhalte: [ Fragen, Begriffe oder Werte, oder: „Entwerfen Sie die Inhalte selbst und zeigen Sie sie mir zuerst als Tabelle.“ ]

Technische Abnahmekriterien:
- Eine einzige HTML-Datei, kein externer Code, keine Bilder oder Schriften aus dem Netz. Sie muss offline und eingebettet in einem iframe laufen.
- Alle Inhalte stehen oben in einem Block `const DATEN = { … };` zwischen den Kommentaren /* ===== DATEN: Nur diesen Block ändern ===== */ und /* ===== ENDE DATEN ===== */. Der Programmcode darunter liest nur aus DATEN.
- Alles Klickbare ist ein <button> und mit der Tastatur bedienbar; Rückmeldungen stehen in einem Bereich mit aria-live="polite".
- Auf einem Handy (360 px Breite) gut bedienbar, ohne seitliches Scrollen.
- Die Datei meldet ihre Höhe an die einbettende Seite: window.parent.postMessage({typ: "iframe-hoehe", hoehe: document.documentElement.scrollHeight}, "*") nach dem Laden, bei Größenänderung und nach jeder Antwort.
- Oberfläche auf Deutsch in der Sie-Form, sachlich, ohne Konfetti, Sounds oder dekorative Animationen.
- Jede Rückmeldung erklärt in einem Satz, warum eine Antwort stimmt oder nicht.

Geben Sie nur den vollständigen Code in einem einzigen Codeblock aus.
````
