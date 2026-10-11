# Status 3 · Notfallmedizin-Trainer

Gamifizierter Fragentrainer für die Notfallmedizin (Zusatzbezeichnung, NA-Dienst) als Progressive Web App.
Statisch, ohne Server – läuft über GitHub Pages und offline nach dem ersten Aufruf.

## Inhalt
- **200 Fragen** in 7 Typen: Wahr/Falsch ×5 (64), Lückentext (25), Rechnen (25), EKG & Bild (24), Zuordnen (22), Reihenfolge (20), verzweigte Boss-Einsätze (20)
- **11 Themen**: Reanimation, Atemweg, Kardio/EKG, Neuro, Trauma, Pädiatrie/Geburtshilfe, Intox/Umwelt, Pharmakologie, Einsatztaktik & Recht, MANV & Sichtung, Gefahrenlagen (CBRN/TEL)
- Jede Frage mit Erklärung und Quellenangabe (ERC 2025, S3 Polytrauma, NUN-Versorgungspfade, ESC, DGN, S2k Anaphylaxie, FwDV 500, Dr. Smith's ECG Blog u. a.)
- 21 Merkkarten

## Spielmodi
Lernen (Filter, „schlaue“ Reihenfolge) · Übungsrunde · Prüfungssimulation mit Zeit · Blitzrunde (60 s Wahr/Falsch mit Combo) ·
Sichtungssprint (mSTaRT oder PRIOR, 90 s) · Boss-Einsätze (3 Herzen, Monitor, Joker) · **Duell am selben Gerät** (Buzzer, geteilter Bildschirm)

## Gamification
XP und 9 Dienstgrade (Praktikant → Legende der Leitstelle) · 37 Abzeichen · 3 Tagesmissionen · Tagesziel (10 Antworten) mit Serie und Wochenansicht · Rekorde · Konfetti & Töne (abschaltbar)

## Veröffentlichen (GitHub Pages)
1. Alle Dateien dieses Ordners ins Repository-Root (Branch `main`).
2. Settings → Pages → „Deploy from a branch“ → `main` / `/ (root)`.
3. Nach 1–2 Minuten erreichbar unter `https://<benutzer>.github.io/<repo>/`.

## Installieren
- iPhone (Safari): Teilen → „Zum Home-Bildschirm“.
- Android (Chrome): Menü ⋮ → „App installieren“.

## Daten
Alles bleibt lokal im Browser. Profil → „Fortschritt sichern“ / „Wiederherstellen“ für Gerätewechsel.
Profil → „Jährliche Inhaltsprüfung“ erzeugt einen Prompt für die Aktualisierung mit Claude.

## Inhalte ändern
Die Fragen liegen als Python-Quellen in `quellcode/` (`q_*.py`, `memos.py`); EKG/Kapnografie werden in `figs.py` gezeichnet.
`python3 figs.py figs.json && python3 finalize.py ..` (im Ordner `quellcode/`) erzeugt `data.js`, `sw.js` und eine neue Version.

*Lernhilfe – ersetzt keine Leitlinie und keine regionale SOP des ÄLRD.*
