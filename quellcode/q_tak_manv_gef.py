from qlib import *

Q = []
T = 'TAK'
Q += [
mtf('TAK-01', T, 'Sonder- und Wegerechte', 'Sonder- und Wegerechte im Rettungsdienst:', [
    ('§ 35 StVO befreit den Rettungsdienst von StVO-Vorschriften, wenn höchste Eile geboten ist, um Menschenleben zu retten oder schwere gesundheitliche Schäden abzuwenden.', 1, 'Sonderrecht.'),
    ('Das Wegerecht nach § 38 StVO erfordert blaues Blinklicht und Einsatzhorn gemeinsam.', 1, 'Nur beides zusammen fordert „sofort freie Bahn“.'),
    ('Sonderrechte entbinden von der Pflicht, die öffentliche Sicherheit und Ordnung gebührend zu berücksichtigen.', 0, 'Diese Pflicht bleibt ausdrücklich bestehen.'),
    ('Der Fahrer haftet für Unfälle unter Sonderrechten grundsätzlich nicht.', 0, 'Haftung und strafrechtliche Verantwortung bleiben möglich.'),
    ('Blaues Blinklicht allein (ohne Horn) dient z. B. der Warnung an der Einsatzstelle.', 1, '§ 38 Abs. 2 StVO.'),
], STVO, 1),

mtf('TAK-02', T, 'NotSan & Delegation', 'Kompetenzen von Notfallsanitätern:', [
    ('§ 2a NotSanG erlaubt heilkundliche Maßnahmen invasiver Art bis zum Eintreffen des Notarztes, wenn Lebensgefahr oder wesentliche Folgeschäden drohen.', 1, 'Seit 2021 in Kraft.'),
    ('Vorab delegierte Maßnahmen (§ 4 Abs. 2 Nr. 2c NotSanG) gibt der ÄLRD standardisiert vor.', 1, 'Über SOP/Versorgungspfade.'),
    ('Bei telenotärztlicher Delegation trägt der NotSan keinerlei Verantwortung für die Durchführung.', 0, 'Die Durchführungsverantwortung bleibt beim Anwender.'),
    ('In Niedersachsen bilden die NUN-Versorgungspfade die landesweite Grundlage; regionale ÄLRD-Vorgaben haben Vorrang.', 1, 'So im NUN-Dokument formuliert.'),
    ('Ein NotSan darf jede ärztliche Maßnahme durchführen, wenn kein Notarzt verfügbar ist.', 0, 'Nur, was er beherrscht und was verhältnismäßig ist.'),
], NOTSANG + '; ' + NUN, 2),

mtf('TAK-03', T, 'Patientenwille', 'Patientenwille und Einwilligung:', [
    ('Eine wirksame Patientenverfügung, die auf die konkrete Situation zutrifft, bindet auch den Notarzt.', 1, '§ 1827 BGB.'),
    ('Bei Zweifeln an Echtheit oder Anwendbarkeit und fehlender Zeit wird im Zweifel lebenserhaltend behandelt.', 1, '„In dubio pro vita“ – Therapie kann später beendet werden.'),
    ('Ein einwilligungsfähiger Patient darf Behandlung und Transport auch gegen ärztlichen Rat ablehnen.', 1, 'Nach Aufklärung über Risiken.'),
    ('Für eine Transportverweigerung genügt die Unterschrift; Aufklärung und Prüfung der Einwilligungsfähigkeit sind entbehrlich.', 0, 'Einwilligungsfähigkeit prüfen, aufklären, dokumentieren, Zeugen.'),
    ('Erwachsene Kinder ohne Vorsorgevollmacht oder Betreuerbestellung können rechtsverbindlich für ihre Eltern in Behandlungen einwilligen.', 0, 'Nur Bevollmächtigte/Betreuer; seit 2023 gilt zusätzlich das Ehegatten-Notvertretungsrecht (§ 1358 BGB).'),
], BGB, 2),

mtf('TAK-04', T, 'Todesfeststellung', 'Todesfeststellung und Leichenschau:', [
    ('Sichere Todeszeichen: Totenflecken, Totenstarre, Fäulnis, mit dem Leben nicht vereinbare Verletzungen.', 1, 'Ggf. dokumentierter Hirntod.'),
    ('Totenflecken entstehen erst nach 6–8 h.', 0, 'Nach ca. 20–30 min, zunächst wegdrückbar.'),
    ('Die Totenstarre beginnt typischerweise im Kiefergelenk nach ca. 2–4 h.', 1, 'Nysten-Regel: von kranial nach kaudal.'),
    ('Bei Anhaltspunkten für einen nicht-natürlichen Tod wird die Polizei informiert und die Auffindesituation möglichst unverändert gelassen.', 1, 'Eigene Veränderungen dokumentieren.'),
    ('Weite, lichtstarre Pupillen sind ein sicheres Todeszeichen.', 0, 'Unsicheres Zeichen (z. B. Hypoxie, Intoxikation, Hypothermie).'),
], ROSSAINT, 1),

mtf('TAK-05', T, 'Eigenschutz', 'Eigenschutz an Einsatzstellen:', [
    ('Eigenschutz hat Vorrang vor der Patientenversorgung.', 1, 'Ein verletzter Helfer hilft niemandem.'),
    ('Warnkleidung nach DIN EN ISO 20471 ist an Verkehrsunfallstellen Pflicht.', 1, 'Auch für den Notarzt.'),
    ('Bei Gewalt gegen Einsatzkräfte gilt: Rückzug und Polizei nachfordern statt Deeskalation um jeden Preis.', 1, 'Fluchtweg freihalten.'),
    ('An Bahnanlagen dürfen Gleise betreten werden, sobald der Zug steht.', 0, 'Erst nach Sperrung/Bahnerdung durch den Notfallmanager.'),
    ('Bei Verdacht auf Gasaustritt in einer Wohnung Licht einschalten, um besser zu sehen.', 0, 'Zündquelle! Keine Schalter, kein Funk/Handy im Gefahrenbereich.'),
], ROSSAINT + '; ' + FWDV500, 1),

mtf('TAK-06', T, 'Crew Resource Management', 'Human Factors und Teamkommunikation:', [
    ('Closed-Loop-Kommunikation reduziert Übertragungsfehler.', 1, 'Anordnung – Wiederholung – Bestätigung.'),
    ('„10-für-10“: In kritischen Situationen 10 s Team-Time-out, um die nächsten 10 min zu planen.', 1, 'Verhindert Aktionismus.'),
    ('Bei der Übergabe in der Notaufnahme berichten alle Teammitglieder gleichzeitig.', 0, 'Einer spricht, alle hören zu („Hands-off-Übergabe“).'),
    ('Fixierungsfehler werden durch aktives Ansprechen von Bedenken („Speak up“) reduziert.', 1, 'Flache Hierarchie fördern.'),
    ('Die Führungskraft sollte selbst die Thoraxkompressionen übernehmen, um das Team zu motivieren.', 0, 'Hands-off-Leadership: Überblick behalten.'),
], CRM, 1),

order('TAK-07', T, 'Lagemeldung', 'Inhalt einer ersten Lagemeldung in sinnvoller Reihenfolge:', [
    'Funkrufname und bestätigter Einsatzort',
    'Was ist passiert? (Schadensart/Lage)',
    'Anzahl Betroffener/Verletzter (Schätzung)',
    'Gefahren an der Einsatzstelle',
    'Bereits eingeleitete Maßnahmen',
    'Nachforderungen (Kräfte/Mittel), Zufahrt/Bereitstellungsraum',
], 'Kurz, strukturiert, früh – lieber zu viel als zu wenig nachfordern.', MANVLIT, 1),

order('TAK-08', T, 'Übergabe nach MIST', 'Bringe die Elemente der Übergabe nach MIST in die richtige Reihenfolge.', [
    'M – Mechanismus/Medizinisches Leitproblem',
    'I – Injuries/Befunde',
    'S – Signs: Vitalparameter',
    'T – Treatment und Trend',
], 'Kurze, standardisierte Übergaben reduzieren Informationsverlust.', CRM, 1),

order('TAK-09', T, 'FMS-Status im Einsatz', 'Bringe die FMS-Statusmeldungen eines typischen Notfalltransports in die zeitliche Reihenfolge.', [
    'Status 2 – einsatzbereit auf Wache',
    'Status 3 – Einsatz übernommen',
    'Status 4 – Ankunft am Einsatzort',
    'Status 7 – Patient aufgenommen',
    'Status 8 – am Transportziel',
    'Status 1 – einsatzbereit über Funk',
], 'Status 3 gab der App ihren Namen: Einsatz übernommen – los geht’s!', FMS, 1),

match('TAK-10', T, 'FMS-Status', 'Ordne der Statusziffer ihre Bedeutung zu.', [
    ['Status 0', 'priorisierter Sprechwunsch (Notruf)'],
    ['Status 5', 'Sprechwunsch'],
    ['Status 6', 'nicht einsatzbereit'],
    ['Status 3', 'Einsatz übernommen'],
    ['Status 4', 'Ankunft am Einsatzort'],
], 'Status 0 nur in echten Notlagen (z. B. Bedrohung der Besatzung).', FMS, 1),

match('TAK-11', T, 'Rechtsnormen', 'Ordne der Rechtsnorm ihren Inhalt zu.', [
    ['§ 323c StGB', 'Unterlassene Hilfeleistung'],
    ['§ 34 StGB', 'Rechtfertigender Notstand'],
    ['§ 203 StGB', 'Verletzung von Privatgeheimnissen (Schweigepflicht)'],
    ['§ 630d BGB', 'Einwilligung in medizinische Maßnahmen'],
    ['§ 1358 BGB', 'Notvertretungsrecht für Ehegatten'],
], 'Notvertretung durch Ehegatten gilt seit 2023 und ist auf 6 Monate befristet.', STGB + '; ' + BGB, 2),

cloze('TAK-12', T, 'Wegerecht', 'Nach § 38 StVO ordnet {0} zusammen mit {1} an: „Alle übrigen Verkehrsteilnehmer haben sofort freie Bahn zu schaffen.“', [
    ['blaues Blinklicht', ['gelbes Blinklicht', 'Fernlicht', 'die Warnblinkanlage']],
    ['dem Einsatzhorn', ['der Lichthupe', 'dem Funk', 'der normalen Hupe']],
], 'Nur gemeinsam – und nur, wenn höchste Eile geboten ist.', STVO, 1),

cloze('TAK-13', T, 'Patientenverfügung', 'Die Patientenverfügung ist in § {0} BGB geregelt; sie muss {1} verfasst sein und gilt {2} von Art und Stadium der Erkrankung.', [
    ['1827', ['1901', '630', '323']],
    ['schriftlich', ['notariell beglaubigt', 'mündlich', 'digital signiert']],
    ['unabhängig', ['nur abhängig', 'nur bei Krebs', 'nur im Endstadium']],
], 'Bis 2022 § 1901a BGB. Mündliche Äußerungen sind Behandlungswünsche/mutmaßlicher Wille.', BGB, 2),

cloze('TAK-14', T, 'NotSanG', '§ {0} NotSanG erlaubt heilkundliche Maßnahmen invasiver Art bis zum Eintreffen des {1}, wenn {2} besteht.', [
    ['2a', ['4', '1', '13']],
    ['Notarztes', ['RTW', 'Polizei', 'Hausarztes']],
    ['Lebensgefahr oder Gefahr wesentlicher Folgeschäden', ['Transportverweigerung', 'Schmerz NRS > 3', 'fehlender Zugang']],
], 'Voraussetzung: Beherrschung der Maßnahme und Verhältnismäßigkeit.', NOTSANG, 2),

num('TAK-15', T, 'Eintreffzeit', 'Planungsgröße Niedersachsen: Ein geeignetes Rettungsmittel soll in wie viel Prozent der Notfalleinsätze innerhalb von 15 Minuten eintreffen?', '%', 95, 0,
    '15 Minuten in 95 % der Notfälle – Grundlage der Bedarfsplanung.', NRETTDG, 2),
]

T = 'MANV'
Q += [
mtf('MANV-01', T, 'Sichtungskategorien', 'Sichtungskategorien beim MANV:', [
    ('SK I (rot): akute vitale Bedrohung – Sofortbehandlung.', 1, 'Lebensrettende Maßnahmen sofort.'),
    ('SK II (gelb): schwer verletzt/erkrankt – aufgeschobene Behandlungsdringlichkeit.', 1, 'Überwachung.'),
    ('SK III (grün): leicht verletzt – spätere, ggf. ambulante Behandlung.', 1, 'Betreuung, Registrierung.'),
    ('SK IV (blau) darf von jedem Rettungsdienstmitarbeiter vergeben werden.', 0, 'Ärztliche Entscheidung (LNA), nur bei Ressourcenmangel.'),
    ('Die Vorsichtung ersetzt die ärztliche Sichtung.', 0, 'Vorsichtung ist ein vorläufiges Ranking.'),
], SK, 1),

mtf('MANV-02', T, 'Ersteintreffendes Team', 'Aufgaben des ersteintreffenden Rettungsmittels beim MANV:', [
    ('Es übernimmt die Führung bis zum Eintreffen von LNA/OrgL.', 1, 'Rolle klar kommunizieren (Weste).'),
    ('Erste Aufgabe ist eine qualifizierte Lagemeldung mit Nachforderung.', 1, 'Erkunden vor Handeln.'),
    ('Das Team beginnt sofort mit der Individualversorgung des ersten Patienten.', 0, 'Bindet Ressourcen – Überblick geht verloren.'),
    ('Das Fahrzeug wird so abgestellt, dass es später abfahren kann.', 1, 'Nicht zuparken lassen.'),
    ('Lebensrettende Sofortmaßnahmen (Blutstillung, Atemwege freimachen, Seitenlage) sind während der Vorsichtung erlaubt.', 1, 'Kurz, dann weiter.'),
], MANVLIT + '; ' + PRIOR, 1),

mtf('MANV-03', T, 'mSTaRT & PRIOR', 'Vorsichtungsalgorithmen:', [
    ('mSTaRT: Gehfähige werden zunächst SK III (grün) zugeordnet.', 1, 'Erster Schritt.'),
    ('mSTaRT: Atemfrequenz > 30/min führt zu SK I.', 1, 'Ebenso fehlender Radialispuls/Rekap > 2 s.'),
    ('PRIOR folgt dem ABCDE-Schema; jeder positive Indikator führt zu SK I.', 1, 'z. B. Bewusstlosigkeit, Atemstörung, fehlender Radialispuls, starke Rumpfschmerzen.'),
    ('PRIOR ist ein ärztlicher Algorithmus, der die Sichtung durch den LNA ersetzt.', 0, 'Vorsichtung durch NotSan/RettSan – ärztliche Sichtung folgt.'),
    ('Bei mSTaRT wird ein Patient ohne Atmung nach Freimachen der Atemwege SK II zugeordnet.', 0, 'Keine Atmung nach Atemwegsöffnung → tot (ex).'),
], MSTART + '; ' + PRIOR, 2),

mtf('MANV-04', T, 'Führungsstruktur', 'Führung und Raumordnung beim MANV:', [
    ('Die Sanitätseinsatzleitung besteht aus Leitendem Notarzt und Organisatorischem Leiter Rettungsdienst.', 1, 'Gemeinsame Führung.'),
    ('Der LNA führt medizinisch, der OrgL organisatorisch-taktisch.', 1, 'Klare Aufgabenteilung.'),
    ('Patientenablage: Sammlung nahe der Schadensstelle; Behandlungsplatz: strukturierte Versorgung.', 1, 'Raumordnung früh festlegen.'),
    ('Am Rettungsmittelhalteplatz werden die Patienten registriert.', 0, 'Dort stehen die Fahrzeuge für den Abtransport bereit.'),
    ('Im MANV gilt: bestmögliche Versorgung möglichst vieler statt maximaler Individualversorgung.', 1, 'Paradigmenwechsel.'),
], MANVLIT, 1),

order('MANV-05', T, 'mSTaRT', 'Bringe die Prüfschritte von mSTaRT in die richtige Reihenfolge.', [
    'Gehfähig? → SK III',
    'Spritzende/lebensbedrohliche Blutung? → Blutstillung, SK I',
    'Atmung vorhanden? (ggf. Atemwege freimachen)',
    'Atemfrequenz > 30/min? → SK I',
    'Radialispuls fehlt oder Rekap > 2 s? → SK I',
    'Befolgt Aufforderungen nicht? → SK I, sonst SK II',
], 'In Sekunden pro Patient – nur lebensrettende Sofortmaßnahmen.', MSTART, 2),

order('MANV-06', T, 'Raumordnung', 'Raumordnung beim MANV von der Schadensstelle nach außen:', [
    'Schadensstelle (Gefahrenbereich)',
    'Patientenablage',
    'Behandlungsplatz',
    'Rettungsmittelhalteplatz',
    'Bereitstellungsraum',
], 'Klare Wege: Einbahnstraßenprinzip für Fahrzeuge.', MANVLIT, 2),

order('MANV-07', T, 'Ablauf', 'Typischer Ablauf der medizinischen Bewältigung eines MANV:', [
    'Lageerkundung und Lagemeldung',
    'Vorsichtung und Kennzeichnung',
    'Ärztliche Sichtung',
    'Behandlung nach Sichtungskategorie',
    'Transportorganisation und Klinikzuweisung',
], 'Sichtung ist ein dynamischer Prozess – Patienten regelmäßig resichten.', MANVLIT, 1),

match('MANV-08', T, 'Funktionen', 'Ordne der Funktion ihre Kernaufgabe zu.', [
    ['Leitender Notarzt', 'medizinische Leitung, Sichtung, Behandlungs- und Transportprioritäten'],
    ['Organisatorischer Leiter RD', 'Organisation, Logistik, Kommunikation'],
    ['Leitstelle', 'Alarmierung, Klinikabfrage, Nachforderungen'],
    ['Abschnittsleiter Transport', 'Rettungsmittelhalteplatz, Abtransport'],
    ['Einsatzleiter Feuerwehr', 'Gefahrenabwehr, Menschenrettung aus dem Gefahrenbereich'],
], 'Schnittstellen klar definieren, Funktionswesten tragen.', MANVLIT, 2),

cloze('MANV-09', T, 'Sichtungskategorien', 'Sichtungskategorie {0} = rot, {1} = gelb, {2} = grün, {3} = blau.', [
    ['I', ['II', 'III', 'IV']],
    ['II', ['I', 'III', 'IV']],
    ['III', ['I', 'II', 'IV']],
    ['IV', ['I', 'II', 'III']],
], 'Verstorbene: „ex“ (schwarz).', SK, 1),

cloze('MANV-10', T, 'mSTaRT-Kriterien', 'Nach mSTaRT ist ein Patient SK I, wenn die Atemfrequenz über {0}/min liegt, die Rekapillarisierungszeit über {1} s beträgt oder kein {2} tastbar ist.', [
    ['30', ['20', '40', '12']],
    ['2', ['1', '4', '6']],
    ['Radialispuls', ['Karotispuls', 'Femoralispuls', 'Fußpuls']],
], 'Zusätzlich: befolgt keine Aufforderungen → SK I.', MSTART, 1),

num('MANV-11', T, 'Vorsichtung – Zeitbedarf', 'Busunfall, 30 Betroffene. Ein Helfer benötigt 10 s pro Patient für die Vorsichtung. Wie viele Minuten braucht er mindestens?', 'min', 5, 0,
    '30 × 10 s = 300 s = 5 min – reine Sichtungszeit ohne Wege.', PRIOR, 1),
]

T = 'GEF'
Q += [
mtf('GEF-01', T, 'Gefahrgutkennzeichnung', 'Orange Warntafel (ADR):', [
    ('Oben steht die Nummer zur Kennzeichnung der Gefahr (Kemler-Zahl), unten die UN-Nummer.', 1, 'Stoffidentifikation über UN-Nummer.'),
    ('Ein vorangestelltes X bedeutet: reagiert gefährlich mit Wasser.', 1, 'Kein Wasser einsetzen.'),
    ('Die Verdopplung einer Ziffer (z. B. 33) bedeutet Verstärkung der Gefahr.', 1, '33 = leicht entzündbare Flüssigkeit.'),
    ('Die Ziffer 8 steht für Giftigkeit, die 6 für Ätzwirkung.', 0, 'Umgekehrt: 6 = giftig, 8 = ätzend.'),
    ('Eine leere orange Tafel bedeutet: keine Gefahr.', 0, 'Gefahrgut – z. B. Stückgut oder mehrere Stoffe.'),
], ADR, 1),

mtf('GEF-02', T, 'Annäherung & Absperrung', 'Annäherung an eine Gefahrstoff-Einsatzstelle:', [
    ('Annäherung mit dem Wind im Rücken, möglichst von erhöhter Position.', 1, 'Gase/Dämpfe werden vom Team weggetragen.'),
    ('Bei unklarer Lage gilt als Faustregel: Gefahrenbereich mindestens 50 m, Absperrbereich 100 m.', 1, 'FwDV 500.'),
    ('Der Rettungsdienst arbeitet ohne Schutzausrüstung im Gefahrenbereich, wenn Patienten sichtbar sind.', 0, 'Nur mit geeigneter PSA – Menschenrettung durch Feuerwehr.'),
    ('Die Menschenrettung aus dem Gefahrenbereich übernimmt die Feuerwehr mit geeigneter PSA.', 1, 'Übergabe an der Grenze.'),
    ('Kontaminierte Patienten werden vor der Behandlung im RTW (not-)dekontaminiert.', 1, 'Sonst Kontaminationsverschleppung.'),
], FWDV500, 1),

mtf('GEF-03', T, 'Nervenkampfstoffe', 'Nervenkampfstoffe und Organophosphate:', [
    ('Leitsymptome: Miosis, Hypersalivation, Bronchorrhö, Bradykardie, Faszikulationen, Krämpfe.', 1, 'Cholinerge Krise.'),
    ('Atropin wird hoch dosiert gegeben, bis die Bronchialsekretion sistiert.', 1, 'Zielkriterium „trockene Lunge“.'),
    ('Obidoxim reaktiviert die Acetylcholinesterase, sofern die Bindung noch nicht „gealtert“ ist.', 1, 'Frühe Gabe.'),
    ('Krampfanfälle werden primär mit Obidoxim behandelt.', 0, 'Benzodiazepine.'),
    ('Eine Dekontamination ist unnötig, da Nervenkampfstoffe nur inhalativ wirken.', 0, 'Auch perkutan – Dekontamination essenziell.'),
], FWDV500 + '; ' + GIZ, 2),

mtf('GEF-04', T, 'Terror-/Amoklage', 'Rettungsdienst bei lebensbedrohlicher Einsatzlage (Terror/Amok):', [
    ('Die Polizei hat die Führung; Gefahrenbereiche werden nur nach Freigabe betreten.', 1, 'Eigenschutz absolut.'),
    ('Zonenmodell: rot = unmittelbare Gefahr, gelb = potenziell gefährdet, grün = sicher.', 1, 'Rettungsdienst arbeitet in der grünen Zone.'),
    ('In gefährdeten Bereichen gilt: Blutungskontrolle und schnelle Evakuierung vor umfassender Diagnostik.', 1, '„Stop the bleeding“, „Scoop and run“.'),
    ('Bereitstellungsräume liegen möglichst nahe am Täterstandort, um Zeit zu sparen.', 0, 'Außerhalb der Gefahrenzone, gedeckt, mit Abstand.'),
    ('Mit Zweitanschlägen („second hit“) muss gerechnet werden.', 1, 'Sammelpunkte variieren, nicht vorhersagbar machen.'),
], TEL, 2),

mtf('GEF-05', T, 'Radiologische Lagen', 'Strahlenunfall:', [
    ('4-A-Regel: Abstand, Aufenthaltsdauer, Abschirmung, Aufnahme vermeiden.', 1, 'Abstand ist am wirksamsten (Abstandsquadratgesetz).'),
    ('Eine Kontamination ist meist keine unmittelbare Lebensgefahr für Retter; die vitale Bedrohung des Patienten hat Vorrang.', 1, 'Erst ABC, dann Dekontamination.'),
    ('Entkleiden entfernt einen Großteil (ca. 80–90 %) einer äußeren Kontamination.', 1, 'Einfach und effektiv.'),
    ('Früh einsetzendes Erbrechen nach Exposition weist auf eine hohe Ganzkörperdosis hin.', 1, 'Prodromalphase.'),
    ('Ein bestrahlter, aber nicht kontaminierter Patient gefährdet das Team radioaktiv.', 0, 'Bestrahlung macht nicht radioaktiv.'),
], FWDV500, 2),

order('GEF-06', T, 'GAMS-Regel', 'Bringe die GAMS-Regel in die richtige Reihenfolge.', [
    'Gefahr erkennen',
    'Absperren',
    'Menschenrettung durchführen',
    'Spezialkräfte alarmieren',
], 'Erstmaßnahmen für alle Ersteintreffenden bei Gefahrstofflagen.', FWDV500, 1),

order('GEF-07', T, 'Zonen bei Terrorlagen', 'Bereiche bei lebensbedrohlichen Einsatzlagen von innen nach außen:', [
    'Rote Zone (unmittelbare Gefahr)',
    'Gelbe Zone (potenziell gefährdet)',
    'Grüne Zone mit Patientenablage/Übergabepunkt',
    'Bereitstellungsraum Rettungsdienst',
], 'Zonen sind dynamisch und werden von der Polizei festgelegt.', TEL, 1),

match('GEF-08', T, 'Kemler-Ziffern', 'Ordne der Kemler-Ziffer die Gefahr zu.', [
    ['2', 'Gas'],
    ['3', 'Entzündbarkeit von Flüssigkeiten'],
    ['6', 'Giftigkeit'],
    ['7', 'Radioaktivität'],
    ['8', 'Ätzwirkung'],
], 'Weitere: 4 = entzündbarer Feststoff, 5 = oxidierend, 9 = spontane heftige Reaktion.', ADR, 1),

match('GEF-09', T, 'Kampfstoffe', 'Ordne dem Kampfstoff das Leitsymptom zu.', [
    ['Nervenkampfstoff (Sarin)', 'Miosis, Bronchorrhö'],
    ['Hautkampfstoff (Schwefellost)', 'verzögerte Blasenbildung'],
    ['Lungenkampfstoff (Phosgen)', 'verzögertes Lungenödem'],
    ['Blutkampfstoff (Cyanid)', 'Bewusstlosigkeit, Laktatazidose'],
    ['Reizstoff (CS/Pfefferspray)', 'Augenbrennen, Tränenfluss'],
], 'Latenzzeiten (Lost, Phosgen) erfordern Überwachung auch bei initial Beschwerdefreien.', FWDV500, 2),

cloze('GEF-10', T, '4A-1C-4E', 'Gefahrenmatrix 4A-1C-4E: A = {0}, Angstreaktion, Ausbreitung, Atomare Strahlung; C = {1}; E = Erkrankung/Verletzung, {2}, Einsturz, Elektrizität.', [
    ['Atemgifte', ['Absturz', 'Aerosole', 'Alkohol']],
    ['Chemische Stoffe', ['Chaos', 'Kohlenmonoxid', 'Crowd']],
    ['Explosion', ['Ertrinken', 'Eis', 'Evakuierung']],
], 'Systematische Gefahrenerkennung an jeder Einsatzstelle.', FWDV500, 1),

cloze('GEF-11', T, 'Hilfesysteme', 'Bei Gefahrgutunfällen unterstützt das Hilfeleistungssystem {0} der chemischen Industrie; Einsatzinformationen bieten u. a. die {1}-Karten.', [
    ['TUIS', ['THW', 'TEL', 'DLRG']],
    ['ERI', ['UN', 'GHS', 'MSDS']],
], 'ERI = Emergency Response Intervention Cards.', ADR, 2),

num('GEF-12', T, 'Absperrbereich', 'Faustregel nach FwDV 500: Wie groß ist der Absperrbereich (m) bei unklarer Gefahrstofflage?', 'm', 100, 0,
    'Gefahrenbereich ≥ 50 m, Absperrbereich ≥ 100 m; bei Bedarf erweitern.', FWDV500, 1),
]
