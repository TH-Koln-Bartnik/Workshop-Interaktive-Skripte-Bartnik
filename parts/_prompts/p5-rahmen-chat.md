````text
Ich baue eine Lehreinheit in Quarto. Thema: [ … ]. Niveau: [ … ]. Die drei Abschnitte heißen: [ 1 … / 2 … / 3 … ].
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
```
## Titel des Abschnitts {#sec-abschnitt-1}

::: {.einschaetzung #ez-1}
Aussage, der man zustimmen oder widersprechen kann.

[Auflösung im ersten Abschnitt](#sec-abschnitt-1){.ez-verweis}
:::

::: {.callout-tip .ez-pruefen title="Ihre Einschätzung prüfen"}
*„Aussage wörtlich wiederholt“* []{.ez-ihre data-ez="ez-1"}

**Auflösung: ja/nein/teils.** Begründung in zwei Sätzen.
:::
```
````
