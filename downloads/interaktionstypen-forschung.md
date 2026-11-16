# Interaktionstypen für Online-Skripte: Was die Forschung sagt

Kurzfassung für Lehrende und für KI-Assistenten, die Interaktionen für ein Quarto-Skript vorschlagen.
Stand: November 2026. Quelle: Workshop „Interaktive Skripte mit KI erstellen“ (R. Bartnik),
https://th-koln-bartnik.github.io/Workshop-Interaktive-Skripte-Bartnik/parts/w2-interaktionstypen.html

## Fünf Prinzipien

1. **Abrufen statt Wiederlesen.** Wer Gelerntes aus dem Gedächtnis abruft, behält es länger als durch
   erneutes Lesen; nach einer Woche liegt die Abrufgruppe vorn, obwohl sich die Lesegruppe sicherer
   fühlt (Roediger & Karpicke, 2006). Übungstests schlagen Wiederlesen und alle anderen
   Vergleichsbedingungen (Adesope et al., 2017). Im Hörsaal und Klassenzimmer erhöhen Quizze die
   Leistung im mittleren Umfang, g = 0,50 über 222 Studien (Yang et al., 2021). Übungstests und
   verteiltes Lernen gehören zu den Techniken mit dem höchsten Nutzen (Dunlosky et al., 2013).

2. **Fragen vor dem Stoff.** Ein Vortest verbessert das spätere Lernen, auch für Fragen, die im Vortest
   falsch beantwortet wurden (Richland et al., 2009). Eine eigene Vorhersage vor dem Ergebnis
   verbessert das Lernen, weil die Überraschung über ein unerwartetes Ergebnis das Behalten stärkt
   (Brod et al., 2018). Erst Probleme versuchen, dann erklären, wirkt besser als die umgekehrte
   Reihenfolge, g = 0,36 (Sinha & Kapur, 2021).

3. **Erzeugen schlägt Klicken.** Das ICAP-Modell ordnet Lernaktivitäten in vier Stufen: passiv < aktiv
   < konstruktiv < interaktiv; je mehr Lernende über das Material hinaus selbst erzeugen, desto mehr
   lernen sie (Chi & Wylie, 2014). Aufforderungen zum Selbsterklären wirken mit g = 0,55 (Bisra et al.,
   2018). Concept Maps selbst zu erstellen wirkt stärker (g = 0,72) als fertige zu studieren
   (g = 0,43) (Schroeder et al., 2018).

4. **Rückmeldung, die erklärt.** Feedback wirkt insgesamt mittelstark, d = 0,48, aber je nach Inhalt
   sehr unterschiedlich (Wisniewski et al., 2020). In computergestützten Übungen wirkt erklärendes
   Feedback (0,49) stärker als die Angabe der richtigen Lösung (0,32) und viel stärker als bloßes
   „richtig/falsch“ (0,05) (Van der Kleij et al., 2015).

5. **Spiel ja, Dekoration nein.** Lernspiele wirken besser als konventioneller Unterricht, d = 0,29, vor
   allem in Kombination mit anderer Instruktion und über mehrere Sitzungen (Wouters et al., 2013).
   Gamification hat kleine positive Effekte auf kognitive Lernergebnisse, g = 0,49, die Effekte
   schwanken aber stark (Sailer & Homner, 2020). Interessante, aber irrelevante Zutaten
   („verführerische Details“) senken Behalten und Transfer (Rey, 2012). Animationen schlagen
   statische Bilder im Mittel mit d = 0,37, deutlich stärker bei Abläufen und Handgriffen
   (d = 1,06), schwächer bei rein dekorativen Animationen (Höffler & Leutner, 2007).

## Palette: Interaktionstypen und wie sie in Quarto kommen

Namen in Klammern: entsprechender H5P-Inhaltstyp (https://h5p.org/content-types-and-applications).
Einbauwege: (Q) Quarto-Kasten ohne Code, (H) eigene HTML-Datei per iframe, von KI gebaut,
(H5P) H5P-Inhalt per Einbettungscode, (S) fremde Simulation per iframe (z. B. PhET).

| Typ | Lernende tun | Prinzip | Einbau |
|---|---|---|---|
| Vorab-Check mit Skala | Aussagen vor dem Lesen einschätzen, Auflösung im Text | 2 | Q (Vorlage) |
| Vorhersage mit Auflösung (Guess the Answer) | Ergebnis vorhersagen, dann aufdecken | 2, 3 | Q (aufklappbarer Kasten) oder H |
| Multiple Choice mit Erklärung (Multiple Choice, Question Set) | Antwort wählen, Erklärung zu jeder Option lesen | 1, 4 | H oder H5P |
| Memory, Karteikarten (Memory Game, Flashcards, Dialog Cards) | Begriff und Definition abrufen und zuordnen | 1 | H oder H5P |
| Zuordnen mit Begründung (Drag and Drop) | Fälle Kategorien zuordnen, Begründung lesen | 1, 3, 4 | H oder H5P |
| Lückentext (Fill in the Blanks, Drag the Words) | Fachbegriff im Satz abrufen | 1 | H oder H5P |
| Reihenfolge (Sort the Paragraphs) | Prozessschritte ordnen | 1, 3 | H oder H5P |
| Fehler finden (Mark the Words) | Fehler im Text oder in einer Rechnung markieren und erklären | 3, 4 | H oder H5P |
| Bild erkunden (Image Hotspots, Find the Hotspot) | Teile einer Abbildung finden und benennen | 1 | H oder H5P |
| Video mit Haltepunkten (Interactive Video) | Video, unterbrochen von Fragen | 1, 5 | H5P |
| Simulation mit Vorhersage | Parameter ändern, vorher Ergebnis schätzen | 2, 5 | S oder H |
| Selbsterklären oder KI-Tutor | Zusammenhang in eigenen Worten erklären, Rückfrage erhalten | 3 | Q (Prompt-Kasten) |
| Concept Map erstellen | Begriffe verbinden und Beziehungen beschriften | 3 | Q (Aufgabe) oder H |
| Problem zuerst | Aufgabe versuchen, bevor die Lösung erklärt wird | 2 | Q (aufklappbarer Kasten) |

## Regeln für Vorschläge

- Bevorzuge Typen, bei denen Lernende etwas erzeugen oder begründen (konstruktiv), vor bloßem Klicken.
- Jede Interaktion braucht eine Rückmeldung, die erklärt, warum eine Antwort stimmt oder nicht.
- Keine Dekoration ohne Bezug zum Lernziel: keine Punkte, Abzeichen oder Animationen als Selbstzweck.
- Mindestens eine Option soll ohne Programmierung auskommen (Q).
- Für (H): eine einzige HTML-Datei, Inhalte oben in einem DATEN-Block, Tastatur- und Handy-tauglich.

## Quellen

- Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. Review of Educational Research, 87(3), 659–701. https://doi.org/10.3102/0034654316689306
- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. Educational Psychology Review, 30(3), 703–725. https://doi.org/10.1007/s10648-018-9434-x
- Brod, G., Hasselhorn, M., & Bunge, S. A. (2018). When generating a prediction boosts learning: The element of surprise. Learning and Instruction, 55, 22–31. https://doi.org/10.1016/j.learninstruc.2018.01.013
- Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. Educational Psychologist, 49(4), 219–243. https://doi.org/10.1080/00461520.2014.965823
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. Psychological Science in the Public Interest, 14(1), 4–58. https://doi.org/10.1177/1529100612453266
- Höffler, T. N., & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. Learning and Instruction, 17(6), 722–738. https://doi.org/10.1016/j.learninstruc.2007.09.013
- Rey, G. D. (2012). A review of research and a meta-analysis of the seductive detail effect. Educational Research Review, 7(3), 216–237. https://doi.org/10.1016/j.edurev.2012.05.003
- Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? Journal of Experimental Psychology: Applied, 15(3), 243–257. https://doi.org/10.1037/a0016496
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Sailer, M., & Homner, L. (2020). The gamification of learning: A meta-analysis. Educational Psychology Review, 32(1), 77–112. https://doi.org/10.1007/s10648-019-09498-w
- Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and constructing concept maps: A meta-analysis. Educational Psychology Review, 30(2), 431–455. https://doi.org/10.1007/s10648-017-9403-9
- Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works: Evidence for productive failure. Review of Educational Research, 91(5), 761–798. https://doi.org/10.3102/00346543211019105
- Van der Kleij, F. M., Feskens, R. C. W., & Eggen, T. J. H. M. (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: A meta-analysis. Review of Educational Research, 85(4), 475–511. https://doi.org/10.3102/0034654314564881
- Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. Frontiers in Psychology, 10, 3087. https://doi.org/10.3389/fpsyg.2019.03087
- Wouters, P., van Nimwegen, C., van Oostendorp, H., & van der Spek, E. D. (2013). A meta-analysis of the cognitive and motivational effects of serious games. Journal of Educational Psychology, 105(2), 249–265. https://doi.org/10.1037/a0031311
- Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. Psychological Bulletin, 147(4), 399–435. https://doi.org/10.1037/bul0000309
