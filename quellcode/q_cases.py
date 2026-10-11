from qlib import *

Q = [
case('REA-C1', 'REA', 'Kammerflimmern im Supermarkt',
     'Alarm: „Person bewusstlos, Reanimation durch Ersthelfer“. Beim Eintreffen (6 min nach Notruf) drückt ein Passant, ein öffentlicher AED klebt bereits und hat einmal geschockt.',
     dict(rhy='CPR läuft', HF='–', RR='–', SpO2='–', AF='–', GCS=3),
     [N('a', 'Der AED fordert gerade zur Fortsetzung der CPR auf. Ihr Team steht mit Monitor/Defibrillator bereit.',
        'Was tun Sie zuerst?', [
         ('Kompressionen übernehmen, AED-Zyklus fortführen und im nächsten 2-min-Zyklus geordnet auf den manuellen Defibrillator wechseln', 1,
          'Richtig – ERC 2025: laufenden AED-Anweisungen folgen und während eines Zyklus wechseln, ohne zusätzliche Pausen.'),
         ('Sofort AED-Pads abziehen und eigene Pads kleben, um den Rhythmus selbst zu beurteilen', 0,
          'Unnötige Pause – der AED arbeitet bereits.'),
         ('Zuerst intubieren, damit danach kontinuierlich komprimiert werden kann', 0,
          'Atemweg ist nachrangig; Kompressionen und Defibrillation zuerst.')]),
      N('b', 'Nach dem 3. Schock (2 vom AED, 1 manuell) weiterhin Kammerflimmern. i.v.-Zugang liegt, i-gel sitzt, Kapnografie 16 mmHg.',
        'Welche Medikation ist jetzt indiziert?', [
         ('Adrenalin 1 mg und Amiodaron 300 mg i.v.', 1, 'Genau – beides nach dem 3. Schock.'),
         ('Nur Amiodaron 150 mg', 0, '150 mg ist die zweite Dosis nach dem 5. Schock.'),
         ('Natriumbicarbonat 100 ml 8,4 %', 0, 'Nicht routinemäßig.')],
        vit=dict(rhy='VF', etCO2=16)),
      N('c', 'Nach dem 5. Schock persistiert das Kammerflimmern.', 'Wie gehen Sie mit dem refraktären VF um?', [
         ('Pad-Lage prüfen, Vektorwechsel auf anterior-posterior, Amiodaron 150 mg, reversible Ursachen suchen', 1,
          'Richtig – refraktäres VF nach ERC 2025; DSD nur in Studien.'),
         ('Doppelt-sequenzielle Defibrillation mit zwei Geräten als Standard', 0, 'Nicht routinemäßig empfohlen.'),
         ('Reanimation beenden, da nach 5 Schocks keine Chance mehr besteht', 0, 'Refraktäres VF ist behandelbar – an ECPR/Lyse denken.', None, None)],
        vit=dict(rhy='VF (refraktär)', etCO2=18)),
      N('d', 'Nach dem Vektorwechsel: organisierter Rhythmus, die etCO₂ springt auf 42 mmHg, Puls tastbar. RR 92/58, SpO₂ 91 %. Das 12-Kanal-EKG zeigt ST-Hebungen in V1–V4.',
        'Was hat jetzt Priorität?', [
         ('SpO₂ 94–98 %, Normoventilation, MAP > 65 mmHg, direkter Transport ins PCI-Zentrum mit Voranmeldung', 1,
          'Postreanimation nach ERC/ESICM 2025.'),
         ('Hyperventilieren, um die Azidose rasch auszugleichen', 0, 'Hyperventilation reduziert die zerebrale Durchblutung.'),
         ('Mit 2 l kalter Infusion präklinisch kühlen', 0, 'Nicht empfohlen.')],
        vit=dict(rhy='Sinusrhythmus', HF=108, RR='92/58', SpO2=91, AF='beatmet', etCO2=42, GCS=3)),
      END('Übergabe im Katheterlabor: proximaler LAD-Verschluss, erfolgreich eröffnet. Der Patient wird nach 4 Tagen extubiert.',
          dict(rhy='Sinusrhythmus', HF=92, RR='118/70', SpO2=96, etCO2=38))],
     ERC_ALS + '; ' + ERC_POST),

case('REA-C2', 'REA', 'PEA nach Hüft-OP',
     'Hausbesuch: 71-jährige Frau, 10 Tage nach Hüft-TEP, plötzlich Luftnot, dann kollabiert. Der Ehemann reanimiert.',
     dict(rhy='PEA', HF='–', RR='–', SpO2='–', AF='–', GCS=3),
     [N('a', 'Monitor: schmalkomplexiger Rhythmus 120/min, kein Puls.', 'Erste Medikation?', [
         ('Adrenalin 1 mg so früh wie möglich, CPR fortführen', 1, 'Nicht schockbar → Adrenalin sofort.'),
         ('Atropin 3 mg', 0, 'Bei PEA nicht empfohlen.'),
         ('Defibrillation 200 J', 0, 'PEA ist nicht schockbar.')]),
      N('b', 'Die Anamnese (Immobilisation, akute Dyspnoe) legt eine Ursache nahe. Point-of-Care-Sono in der Pulscheck-Pause: rechter Ventrikel deutlich dilatiert, kein Perikarderguss.',
        'Wie bewerten Sie die Situation?', [
         ('Hochwahrscheinlich fulminante LE – Thrombolyse unter CPR erwägen', 1,
          'Klinischer Kontext + Befund; RV-Dilatation allein ist nicht beweisend, hier aber stimmig.'),
         ('RV-Dilatation beweist eine LE auch ohne Anamnese', 0, 'ERC 2025: isolierte RV-Dilatation ist nicht diagnostisch.'),
         ('Sono ohne Kontraktilität → Reanimation beenden', 0, 'Kontraktilität allein ist kein Abbruchkriterium.')]),
      N('c', 'Sie geben Alteplase als Bolus.', 'Wie lange reanimieren Sie mindestens weiter?', [
         ('60–90 min, ggf. mechanische Reanimationshilfe für den Transport', 1, 'Das Fibrinolytikum braucht Zeit.'),
         ('10 min – danach Abbruch, wenn kein ROSC', 0, 'Zu kurz nach Lyse.'),
         ('Sofort beenden, weil Lyse unter CPR kontraindiziert ist', 0, 'Reanimation ist keine Kontraindikation.')]),
      END('Nach 28 min ROSC. Transport unter Noradrenalin in ein Zentrum mit ECLS-Option.',
          dict(rhy='Sinustachykardie', HF=124, RR='88/50', SpO2=89, etCO2=30))],
     ERC_ALS + '; ' + ESC_LE),

case('AW-C1', 'AW', 'Status asthmaticus',
     '24-jährige Asthmatikerin, seit Stunden zunehmende Luftnot, Spray hilft nicht mehr. Sie sitzt vornübergebeugt, spricht nur einzelne Worte.',
     dict(HF=132, RR='140/85', SpO2=86, AF=34, GCS=15),
     [N('a', 'Auskultatorisch kaum Atemgeräusch beidseits.', 'Erste Therapie?', [
         ('O₂ titriert, Salbutamol + Ipratropium vernebelt, Prednisolon i.v.', 1, 'Basistherapie des schweren Anfalls.'),
         ('Midazolam 2 mg gegen die Panik', 0, 'Gefahr der Atemdepression.'),
         ('Furosemid 40 mg wegen „feuchter Lunge“', 0, 'Kein Lungenödem – silent chest = Obstruktion.')]),
      N('b', 'Nach 15 min kaum Besserung, SpO₂ 88 %, AF 30/min.', 'Nächste Eskalation?', [
         ('Magnesiumsulfat 2 g i.v. über 20 min, Vernebelung wiederholen, ggf. Adrenalin i.m./vernebelt', 1, 'Leitliniengerechte Eskalation.'),
         ('Sofort Propofol-Narkose ohne Vorbereitung', 0, 'Hochrisiko-Intubation – vorher maximal konservativ, dann geplant.'),
         ('Theophyllin-Bolus als erste Eskalationsstufe', 0, 'Nachrangig, viele Nebenwirkungen.')],
        vit=dict(HF=138, SpO2=88, AF=30)),
      N('c', 'Die Patientin wird somnolent, SpO₂ 82 %, etCO₂ steigt. Sie entscheiden sich zur Narkose.', 'Welches Einleitungs-Hypnotikum ist am günstigsten?', [
         ('Ketamin/Esketamin (bronchodilatierend, kreislaufstabil)', 1, 'Erste Wahl beim Asthma.'),
         ('Thiopental', 0, 'Histaminfreisetzung möglich.'),
         ('Keins – Wachintubation ohne Medikamente', 0, 'Nicht praktikabel.')],
        vit=dict(HF=142, SpO2=82, AF=12, GCS=11, etCO2=68)),
      N('d', 'Nach Intubation: Spitzendruck 45 cmH₂O, RR fällt auf 75/40, die Kapnografie zeigt eine Haifischflosse ohne Nulllinienrückkehr.',
        'Was ist die wahrscheinlichste Ursache – und Ihre Maßnahme?', [
         ('Dynamische Überblähung (Auto-PEEP) – kurz diskonnektieren, Frequenz senken, lange Exspiration', 1, 'Klassische Komplikation; Spannungspneu ausschließen.'),
         ('Hypovolämie – 2 l Volumen', 0, 'Volumen hilft kurzfristig, die Ursache bleibt.'),
         ('Tubusfehllage – sofort extubieren', 0, 'Die Kapnografie zeigt CO₂ – Tubus liegt.')],
        vit=dict(HF=148, RR='75/40', SpO2=84, AF='beatmet', etCO2=60)),
      END('Mit AF 8/min, I:E 1:4 und Salbutamol über den Respirator stabilisiert. Übergabe auf die Intensivstation.',
          dict(HF=120, RR='105/65', SpO2=93, etCO2=55))],
     NVL_ASTHMA + '; ' + NARK),

case('AW-C2', 'AW', 'Bolusgeschehen im Restaurant',
     'Ein 68-jähriger Mann greift sich beim Steakessen an den Hals, kann nicht sprechen, hustet nicht wirksam.',
     dict(HF=118, RR='160/90', SpO2=84, AF='frustrane Atembewegungen', GCS=15),
     [N('a', 'Der Patient ist noch wach.', 'Erste Maßnahme?', [
         ('Bis zu 5 Rückenschläge, dann bis zu 5 Oberbauchkompressionen im Wechsel', 1, 'ERC-Sequenz bei ineffektivem Husten.'),
         ('Blind mit dem Finger auswischen', 0, 'Gefahr, den Bolus tiefer zu schieben.'),
         ('Abwarten, bis der Notarzt laryngoskopiert', 0, 'Keine Zeit – Hypoxie.')]),
      N('b', 'Der Mann wird bewusstlos und sinkt zu Boden.', 'Wie weiter?', [
         ('Hinlegen, CPR beginnen; vor Beatmungen in den Mund schauen; Laryngoskopie und Magill-Zange vorbereiten', 1, 'Kompressionen erzeugen hohe Atemwegsdrücke.'),
         ('Weiter Oberbauchkompressionen am Liegenden', 0, 'Bei Bewusstlosigkeit: CPR.'),
         ('Sofort Koniotomie', 0, 'Erst Laryngoskopie/Magill versuchen.')],
        vit=dict(HF=42, SpO2=70, AF=0, GCS=3)),
      N('c', 'Unter Laryngoskopie sehen Sie ein Fleischstück vor der Glottis und entfernen es mit der Magill-Zange. Spontanatmung setzt ein, HF 98/min.',
        'Was ist nach erfolgreicher Entfernung wichtig?', [
         ('O₂, Monitoring, Transport zur Abklärung (Aspiration, Verletzungen durch Kompressionen)', 1, 'Immer ärztliche Abklärung.'),
         ('Kein Transport nötig – Ursache ist beseitigt', 0, 'Aspirationspneumonie, Rippen-/Organverletzungen möglich.'),
         ('Sofortige Intubation, da jeder Bolus-Patient intubiert werden muss', 0, 'Nur bei Indikation.')],
        vit=dict(HF=98, RR='130/80', SpO2=93, AF=18, GCS=11)),
      END('Der Patient ist bei Übergabe wach; Röntgen-Thorax ohne Aspiration.', dict(HF=88, RR='135/80', SpO2=97, AF=16, GCS=15))],
     ERC_BLS + '; ' + AWM, lvl=2),

case('KAR-C1', 'KAR', 'Hinterwand mit Bradykardie',
     '63-jähriger Landwirt, seit 1 h Oberbauch- und Brustschmerz, kaltschweißig.',
     dict(rhy='Sinusbradykardie', HF=44, RR='86/52', SpO2=95, AF=18, GCS=15),
     [N('a', 'Das 12-Kanal-EKG zeigt ST-Hebungen in II, III, aVF (III > II) mit ST-Senkung in aVL; geringe ST-Hebung in V1.',
        'Welche zusätzliche Diagnostik ist sinnvoll?', [
         ('Rechtsventrikuläre Ableitungen (V4R)', 1, 'ST-Hebung in V1 und III > II → RV-Beteiligung prüfen.'),
         ('Keine – das EKG ist eindeutig, Transport sofort ohne weitere Ableitungen', 0, 'V4R kostet Sekunden und ändert die Therapie (Nitrate, Volumen).'),
         ('Troponin-Schnelltest abwarten', 0, 'Verzögert die Reperfusion.')]),
      N('b', 'V4R: ST-Hebung 1,5 mm. Der Patient klagt weiter über starke Schmerzen.', 'Welche Therapie ist jetzt kontraindiziert?', [
         ('Nitroglycerin s.l.', 1, 'Vorlastabhängiger RV-Infarkt + Hypotonie → Nitrate kontraindiziert.'),
         ('ASS 250 mg i.v.', 0, 'ASS ist indiziert.'),
         ('Heparin 5000 IE i.v.', 0, 'Heparin ist indiziert.')]),
      N('c', 'HF fällt auf 38/min, RR 78/45, Patient wird unruhig.', 'Nächster Schritt?', [
         ('Atropin 0,5 mg i.v., vorsichtiger Volumenbolus, Pacing/Adrenalin vorbereiten', 1, 'Instabile Bradykardie bei inferiorem Infarkt – Atropin oft wirksam (vagal).'),
         ('Furosemid 40 mg', 0, 'Verschlechtert die Vorlast.'),
         ('Betablocker zur Infarktgrößenreduktion', 0, 'Kontraindiziert bei Bradykardie/Schock.')],
        vit=dict(HF=38, RR='78/45')),
      N('d', 'Nach Atropin HF 62/min, RR 95/60.', 'Zielklinik?', [
         ('Direkt ins nächste PCI-Zentrum mit Katheterlabor-Voranmeldung', 1, 'Primäre PCI ≤ 120 min.'),
         ('Nächstes Krankenhaus ohne Katheterlabor zur Stabilisierung', 0, 'Zeitverlust.'),
         ('Hausarzt informieren und abwarten', 0, '—')],
        vit=dict(HF=62, RR='95/60')),
      END('RCA proximal verschlossen und eröffnet; RV-Funktion erholt sich.', dict(rhy='Sinusrhythmus', HF=72, RR='110/70', SpO2=97))],
     ESC_ACS + '; ' + SMITH + '; ' + ERC_TACHY),

case('KAR-C2', 'KAR', 'Instabile Breitkomplex-Tachykardie',
     '71-Jähriger mit ischämischer Kardiomyopathie, Herzrasen und Brustenge seit 30 min, blass, kaltschweißig.',
     dict(rhy='Breitkomplextachykardie', HF=186, RR='78/50', SpO2=92, AF=24, GCS=14),
     [N('a', 'Der Monitor zeigt eine regelmäßige Breitkomplextachykardie.', 'Wie stufen Sie die Situation ein?', [
         ('Instabile VT (Schock, Ischämiezeichen) – synchronisierte Kardioversion', 1, 'Instabilitätszeichen → elektrische Therapie.'),
         ('Stabile SVT mit Schenkelblock – Adenosin', 0, 'Bei KHK und Instabilität: VT annehmen.'),
         ('Sinustachykardie – Volumen', 0, 'Frequenz 186 regelmäßig, breit – keine Sinustachykardie.')]),
      N('b', 'Sie bereiten die Kardioversion vor.', 'Analgosedierung?', [
         ('Kleine titrierte Dosen (z. B. Esketamin/Midazolam oder Propofol), Atemwegsbereitschaft', 1, 'Kreislaufschonend titrieren.'),
         ('Keine – der Patient ist instabil', 0, 'Wacher Patient: Analgosedierung, solange vertretbar.'),
         ('Volle Narkosedosis Propofol 2 mg/kg', 0, 'Kollapsgefahr.')]),
      N('c', 'Synchronisiert, Energie gewählt.', 'Welche Anfangsenergie ist nach ERC 2025 angemessen?', [
         ('120–150 J', 1, 'VT mit Puls.'),
         ('50 J', 0, 'Zu niedrig.'),
         ('4 J/kg', 0, 'Pädiatrische Angabe.')]),
      N('d', 'Nach dem ersten Schock unverändert VT.', 'Nächster Schritt?', [
         ('Synchronisation prüfen, Energie steigern, erneut kardiovertieren; dann Amiodaron 300 mg über 10–20 min', 1, 'Bis zu 3 Versuche, dann Amiodaron.'),
         ('Verapamil 5 mg i.v.', 0, 'Bei VT gefährlich.'),
         ('Abwarten und monitoren', 0, 'Patient instabil.')]),
      END('Nach dem zweiten Schock Sinusrhythmus. Amiodaron-Kurzinfusion, Transport in die Kardiologie.',
          dict(rhy='Sinusrhythmus', HF=84, RR='112/70', SpO2=96, AF=16, GCS=15))],
     ERC_TACHY),

case('NEU-C1', 'NEU', 'Aphasie beim Frühstück',
     '74-jährige Frau, beim Frühstück plötzlich sprachgestört, rechter Arm schlaff. Ehemann: „Um 7:40 Uhr war noch alles normal.“ Jetzt 8:05 Uhr.',
     dict(HF=88, RR='190/100', SpO2=96, AF=16, GCS=13, BZ='?'),
     [N('a', 'BE-FAST positiv (Gesicht, Arm, Sprache).', 'Was messen Sie zwingend vor allen weiteren Entscheidungen?', [
         ('Blutzucker', 1, 'Hypoglykämie ausschließen.'),
         ('Temperatur', 0, 'Wichtig, aber nicht vorrangig.'),
         ('Troponin', 0, 'Präklinisch nicht relevant.')], vit=dict(BZ=134)),
      N('b', 'BZ 134 mg/dl, RR 190/100.', 'Blutdruckmanagement?', [
         ('Nicht senken – präklinisch erst > 220/120 vorsichtig', 1, 'Penumbra-Perfusion erhalten.'),
         ('Urapidil auf < 140 mmHg', 0, 'Zu aggressiv.'),
         ('Nifedipin s.l.', 0, 'Obsolet.')]),
      N('c', 'Die Patientin hat einen hochgradigen Defekt mit Blickwendung nach links – Verdacht auf großen Gefäßverschluss.', 'Transport und Kommunikation?', [
         ('Voranmeldung und direkter Transport in ein Zentrum mit Thrombektomie (gemäß regionalem Konzept); Ehemann mitnehmen oder Telefonnummer notieren', 1, 'Zeitfenster und Fremdanamnese sichern.'),
         ('Transport in das nächste Krankenhaus ohne Stroke Unit', 0, 'Zeitverlust bis zur Rekanalisation.'),
         ('ASS 500 mg i.v. vor Transport', 0, 'Blutung nicht ausgeschlossen.')]),
      END('CT-Angiografie: M1-Verschluss links. Lyse um 8:52 Uhr, Thrombektomie mit kompletter Rekanalisation.',
          dict(HF=80, RR='165/90', SpO2=97, GCS=14))],
     DGN_STROKE, lvl=2),

case('NEU-C2', 'NEU', 'Krampfanfall ohne Ende',
     '38-jähriger Epileptiker, generalisiert tonisch-klonisch krampfend, laut Kollegen seit 8 min.',
     dict(HF=128, RR='165/95', SpO2=88, AF='unregelmäßig', GCS=3, BZ='?'),
     [N('a', 'Kein i.v.-Zugang, Patient 85 kg.', 'Erste Medikation?', [
         ('Midazolam 10 mg i.m.', 1, 'Gleichwertig zu Lorazepam i.v., ohne Zugangsverzögerung.'),
         ('Zuerst i.v.-Zugang erzwingen, dann Lorazepam', 0, 'Zeitverlust.'),
         ('Levetiracetam 4,5 g i.m.', 0, 'Nicht i.m.; Stufe 2.')]),
      N('b', 'Nach 5 min krampft er weiter. Zugang liegt jetzt. BZ 92 mg/dl.', 'Wie weiter?', [
         ('Benzodiazepin einmal wiederholen (z. B. Lorazepam 4 mg i.v.), Levetiracetam vorbereiten', 1, 'Zweite Benzodiazepin-Gabe, dann Stufe 2.'),
         ('Sofort Propofol-Narkose', 0, 'Erst Stufe 1 und 2 ausschöpfen, wenn möglich.'),
         ('Glukose 40 % 50 ml', 0, 'BZ normal.')], vit=dict(BZ=92)),
      N('c', 'Weiter krampfend.', 'Stufe 2?', [
         ('Levetiracetam 60 mg/kg (max. 4500 mg) i.v. über ca. 10 min', 1, 'Oder Valproat 40 mg/kg.'),
         ('Diazepam rektal', 0, 'Weiterhin Stufe 1.'),
         ('Flumazenil', 0, 'Kontraindiziert.')]),
      N('d', 'Der Anfall sistiert. GCS 6, SpO₂ 90 % unter O₂, schnarchende Atmung.', 'Atemwegsmanagement?', [
         ('Esmarch/Wendl, Seitenlage, O₂; Intubation bei fehlender Besserung bzw. Aspirationsgefahr', 1, 'Postiktal oft rasche Besserung.'),
         ('Sofortige Intubation ohne Evaluation', 0, 'Nicht automatisch.'),
         ('Keine Maßnahme – postiktal normal', 0, 'Atemweg sichern!')],
        vit=dict(HF=104, SpO2=90, AF=12, GCS=6)),
      END('Atemweg mit Wendl frei, GCS bei Ankunft 10. Ursache: Medikamentenpause.',
          dict(HF=96, RR='140/85', SpO2=97, AF=14, GCS=10))],
     DGN_SE, lvl=2),

case('TRA-C1', 'TRA', 'Motorrad gegen Leitplanke',
     '29-jähriger Motorradfahrer, Oberschenkel links subtotal amputiert, spritzende Blutung, blass, unruhig.',
     dict(HF=142, RR='82/50', SpO2=93, AF=28, GCS=13),
     [N('a', 'Ankunft am Patienten.', 'Was tun Sie zuerst?', [
         ('Tourniquet proximal anlegen („<c>“)', 1, 'Kritische Blutung zuerst.'),
         ('Helm abnehmen und intubieren', 0, 'A kommt nach <c>.'),
         ('Zwei großlumige Zugänge legen', 0, 'Blutung zuerst stoppen.')]),
      N('b', 'Blutung steht. Becken: Prellmarken, Schmerz bei Kompression angegeben.', 'Nächste Maßnahmen?', [
         ('Beckenschlinge (Trochanterhöhe), Tranexamsäure 1 g, Wärmeerhalt', 1, 'Blutungstherapie komplett.'),
         ('Becken mehrfach auf Stabilität prüfen', 0, 'Löst Gerinnsel.'),
         ('2 l kristalloide Lösung zügig', 0, 'Permissive Hypotension: RRsys ≈ 80 mmHg.')],
        vit=dict(HF=136, RR='84/52')),
      N('c', 'GCS 14, keine Kopfverletzung erkennbar, RR 84/52.', 'Blutdruckziel?', [
         ('RRsys ≈ 80 mmHg / MAP ≈ 65 mmHg bis zur chirurgischen Blutstillung', 1, 'Permissive Hypotension ohne SHT.'),
         ('RRsys > 120 mmHg', 0, 'Fördert Blutung.'),
         ('RRsys 60 mmHg', 0, 'Zu niedrig.')]),
      N('d', 'Analgesie nötig, NRS 9.', 'Welche Option ist hier besonders günstig?', [
         ('Esketamin titriert (kreislaufstabil)', 1, 'Im Schock gut geeignet.'),
         ('Metamizol 2,5 g schnell i.v.', 0, 'Hypotonie.'),
         ('Keine Analgesie – maskiert Befunde', 0, 'Analgesie ist Pflicht.')]),
      END('Transport per RTH ins überregionale Traumazentrum, Tourniquet-Zeit dokumentiert.',
          dict(HF=118, RR='88/56', SpO2=96, AF=22, GCS=14))],
     S3PT),

case('TRA-C2', 'TRA', 'Plötzlicher Druckanstieg nach Intubation',
     'Pkw-Seitenaufprall. 54-jähriger Fahrer mit Thoraxtrauma rechts, GCS 7 – Sie haben ihn intubiert.',
     dict(HF=104, RR='118/70', SpO2=95, AF='beatmet', GCS=3, etCO2=36),
     [N('a', 'Zehn Minuten später: Beatmungsdruck von 22 auf 42 cmH₂O, SpO₂ 82 %, RR 70/40, rechts kein Atemgeräusch.',
        'Wahrscheinlichste Ursache?', [
         ('Spannungspneumothorax rechts', 1, 'Klassische Trias unter Überdruckbeatmung.'),
         ('Einseitige Intubation links', 0, 'Dann fehlte das Atemgeräusch links.'),
         ('Hypovolämie', 0, 'Erklärt den Beatmungsdruck nicht.')],
        vit=dict(HF=132, RR='70/40', SpO2=82, etCO2=24)),
      N('b', '—', 'Sofortmaßnahme?', [
         ('Entlastung: Nadeldekompression oder direkt Minithorakotomie rechts', 1, 'Ohne Bildgebung.'),
         ('Erst Thorax-Ultraschall in Ruhe, dann entscheiden', 0, 'Der Patient stirbt dabei.'),
         ('PEEP erhöhen', 0, 'Verschlechtert die Lage.')]),
      N('c', 'Nach Nadeldekompression Besserung, 5 min später erneut steigende Drücke.', 'Wie weiter?', [
         ('Minithorakotomie (4./5. ICR vordere/mittlere Axillarlinie), digitale Exploration', 1, 'Nadel abgeknickt/verlegt – chirurgische Pleuraeröffnung.'),
         ('Zweite Nadel daneben, mehr nicht', 0, 'Unsicher.'),
         ('Extubieren', 0, '—')]),
      END('Nach Minithorakotomie stabil, Übergabe im Schockraum mit Thoraxdrainage.',
          dict(HF=108, RR='112/68', SpO2=95, etCO2=35))],
     S3PT, lvl=2),

case('PAE-C1', 'PAE', 'Gartenteich',
     'Ein 2-jähriges Kind (ca. 12 kg) wurde leblos aus dem Gartenteich gezogen. Die Mutter hält es im Arm.',
     dict(HF='–', RR='–', SpO2='–', AF=0, GCS=3, T='?'),
     [N('a', 'Keine Atmung, keine Lebenszeichen.', 'Erste Maßnahme?', [
         ('5 initiale Beatmungen, dann 15:2', 1, 'Hypoxischer Stillstand.'),
         ('Sofort 30 Kompressionen ohne Beatmung', 0, 'Beim Ertrinken zuerst beatmen.'),
         ('Kind kopfüber halten, um Wasser abfließen zu lassen', 0, 'Zeitverlust, Aspirationsgefahr.')]),
      N('b', 'Monitor: Asystolie. i.o.-Zugang liegt.', 'Adrenalin-Dosis?', [
         ('120 µg (10 µg/kg)', 1, 'Alle 3–5 min.'),
         ('1 mg', 0, 'Erwachsenendosis.'),
         ('12 µg', 0, 'Zehnfach zu niedrig.')]),
      N('c', 'Rektale Temperatur 29 °C.', 'Konsequenz?', [
         ('Adrenalin bis > 30 °C zurückhalten, Wärmeerhalt, Transport in Zentrum mit ECLS', 1, 'Hypotherme Reanimation.'),
         ('Reanimation abbrechen – bei 29 °C aussichtslos', 0, '„Nobody is dead until warm and dead“.'),
         ('Mit kalten Infusionen weiter kühlen', 0, 'Unsinnig.')], vit=dict(T='29 °C')),
      END('Unter laufender CPR in die Kinderklinik mit ECLS; ROSC nach Wiedererwärmung.',
          dict(HF=110, SpO2=94, T='33 °C'))],
     ERC_PLS + '; ' + ERC_SPEC),

case('PAE-C2', 'PAE', 'Geburt im RTW',
     'Sie werden zu einer Schwangeren (39. SSW) gerufen; die Geburt ist nicht mehr aufzuhalten. Das Kind wird im RTW geboren, ist schlaff und blass.',
     dict(HF='< 100', RR='–', SpO2='–', AF='Schnappatmung', GCS='–'),
     [N('a', 'Uhr gestartet.', 'Was ist der erste Schritt?', [
         ('Abtrocknen, in warme Tücher wickeln, Atmung/HF/Tonus beurteilen', 1, 'Wärmeerhalt und Stimulation.'),
         ('Sofort Thoraxkompressionen', 0, 'Erst Beatmung.'),
         ('Routinemäßig absaugen', 0, 'Nur bei Verlegung.')]),
      N('b', 'Schnappatmung, HF ca. 60/min.', 'Weiter?', [
         ('Atemwege öffnen, 5 Blähbeatmungen (2–3 s)', 1, 'Lunge belüften.'),
         ('Adrenalin i.v.', 0, 'Noch nicht indiziert.'),
         ('Kind sofort abnabeln und zur Klinik fahren, ohne Maßnahmen', 0, 'Versorgung vor Ort.')]),
      N('c', 'Nach 30 s effektiver Beatmung (Thorax hebt sich) HF 50/min.', 'Nächster Schritt?', [
         ('Thoraxkompressionen 3:1 mit 100 % O₂', 1, 'HF < 60/min trotz Beatmung.'),
         ('Weiter nur beatmen', 0, 'HF < 60/min → Kompressionen.'),
         ('Abwarten', 0, '—')], vit=dict(HF=50)),
      N('d', 'Das Kind erholt sich (HF 140/min, schreit). Die Mutter blutet nach Plazentageburt stark.', 'Maßnahmen bei der Mutter?', [
         ('Uterusmassage, Oxytocin, Tranexamsäure 1 g, Volumen, Blase entleeren', 1, 'Atonie häufigste Ursache.'),
         ('Abwarten, Blutverlust ist postpartal normal', 0, 'PPH ist lebensbedrohlich.'),
         ('Fundusdruck mit maximaler Kraft und Tamponade der Scheide als einzige Maßnahme', 0, 'Uterustonus medikamentös fördern.')],
        vit=dict(HF=140)),
      END('Mutter und Kind stabil in der Geburtsklinik übergeben.', dict(HF=136, SpO2=95))],
     ERC_NLS + '; ' + ROSSAINT),

case('TOX-C1', 'TOX', 'Bewusstlos im Bahnhofs-WC',
     'Ein 31-jähriger Mann liegt bewusstlos in einer Toilettenkabine, daneben eine Spritze.',
     dict(HF=58, RR='100/60', SpO2=74, AF=4, GCS=3),
     [N('a', 'Pupillen stecknadelkopfgroß, Atmung kaum vorhanden.', 'Erste Maßnahme?', [
         ('Atemwege freimachen und mit Beutel-Maske beatmen (O₂)', 1, 'Oxygenierung zuerst.'),
         ('Sofort 2 mg Naloxon i.v. Bolus', 0, 'Entzug, Agitation, Erbrechen – erst beatmen, dann titrieren.'),
         ('Spritze sicher entsorgen und Polizei abwarten', 0, 'Eigenschutz ja – aber sofort behandeln.')],
        vit=dict(SpO2=88)),
      N('b', 'SpO₂ 88 % unter Beatmung. i.v.-Zugang liegt.', 'Naloxon-Strategie?', [
         ('Titriert in kleinen Schritten (z. B. 0,04–0,1 mg) bis ausreichende Spontanatmung', 1, 'Ziel ist Atmung, nicht Wachheit.'),
         ('Keine Gabe – nur beatmen bis zur Klinik', 0, 'Möglich, aber Naloxon ist indiziert.'),
         ('Flumazenil 0,5 mg', 0, 'Kein Benzodiazepin-Hinweis; Krampfrisiko.')]),
      N('c', 'Nach 0,2 mg atmet er mit AF 12/min, ist wach und will gehen.', 'Wie verfahren Sie?', [
         ('Über Rebound-Gefahr aufklären, Einwilligungsfähigkeit prüfen, Transport dringend empfehlen; Ablehnung sorgfältig dokumentieren', 1, 'Wirkdauer Naloxon < Opioid.'),
         ('Gehen lassen – Problem gelöst', 0, 'Rebound-Gefahr.'),
         ('Gegen seinen Willen fixieren und transportieren', 0, 'Nur bei Einwilligungsunfähigkeit/Gefahr nach Landesrecht.')],
        vit=dict(HF=92, RR='130/80', SpO2=95, AF=12, GCS=15)),
      END('Er willigt nach Aufklärung in den Transport ein; nach 45 min erneute Somnolenz in der Notaufnahme.',
          dict(HF=70, SpO2=92, AF=9, GCS=12))],
     GIZ + '; ' + BGB, lvl=2),

case('TOX-C2', 'TOX', 'Wohnungsbrand – Rauchgas',
     'Die Feuerwehr rettet einen 52-jährigen Mann aus einer verrauchten Wohnung. Er ist somnolent, Ruß im Gesicht.',
     dict(HF=118, RR='105/60', SpO2=98, AF=24, GCS=10),
     [N('a', 'SpO₂ zeigt 98 % unter Raumluft.', 'Bewertung der SpO₂?', [
         ('Unzuverlässig – CO-Hb wird als O₂-Hb gemessen; SpCO messen, 100 % O₂', 1, 'Standardpulsoxymetrie täuscht.'),
         ('Normal, keine O₂-Gabe nötig', 0, 'Gefährlicher Trugschluss.'),
         ('Messfehler durch Ruß – Sensor tauschen genügt', 0, '—')]),
      N('b', 'SpCO 28 %, Laktat (BGA im RTW) 11 mmol/l, RR fällt auf 80/45, GCS 8.', 'Woran denken Sie zusätzlich?', [
         ('Cyanidintoxikation – Hydroxocobalamin 5 g i.v.', 1, 'Brandrauch + Laktat > 8–10 + Schock.'),
         ('Hypoglykämie – Glukose', 0, 'BZ messen, aber erklärt Laktat nicht.'),
         ('Anaphylaxie – Adrenalin i.m.', 0, '—')],
        vit=dict(HF=126, RR='80/45', GCS=8, SpO2=98)),
      N('c', 'Heiserkeit, Ruß im Rachen, beginnender Stridor.', 'Atemweg?', [
         ('Frühzeitige Intubation durch Erfahrene (Schwellung nimmt zu)', 1, 'Inhalationstrauma.'),
         ('Abwarten bis zur Klinik', 0, 'Später unmöglich.'),
         ('Larynxtubus als Primärstrategie', 0, 'Supraglottische Schwellung.')]),
      END('Intubiert, Hydroxocobalamin gegeben; Verlegung in ein Zentrum mit HBO-Option nach Rücksprache.',
          dict(HF=104, RR='110/65', SpO2=99, AF='beatmet', GCS=3))],
     GIZ + '; ' + BURN + '; ' + ERC_SPEC),

case('TAK-C1', 'TAK', 'Nach Hypoglykämie: „Ich bleib zu Hause“',
     '79-jähriger Typ-2-Diabetiker unter Glibenclamid, von der Tochter verwirrt aufgefunden. BZ 32 mg/dl.',
     dict(HF=96, RR='150/80', SpO2=96, AF=16, GCS=12, BZ=32),
     [N('a', '—', 'Therapie?', [
         ('Glukose i.v. titriert (z. B. 8–16 g), BZ-Kontrolle', 1, 'Standard.'),
         ('Glukagon 1 mg i.m. als erste Wahl trotz liegendem Zugang', 0, 'i.v.-Glukose bevorzugt.'),
         ('Insulin', 0, '—')], vit=dict(BZ=142, GCS=15)),
      N('b', 'BZ 142 mg/dl, Patient wach und orientiert, lehnt den Transport ab.', 'Was spricht medizinisch für den Transport?', [
         ('Sulfonylharnstoff mit langer Wirkdauer – hohe Rezidivgefahr über Stunden', 1, 'Stationäre Überwachung empfohlen.'),
         ('Nichts – BZ ist normal', 0, 'Rezidivgefahr.'),
         ('Die Tochter möchte es so', 0, 'Ist kein medizinisches Argument.')]),
      N('c', 'Er bleibt dabei, wirkt einwilligungsfähig.', 'Korrektes Vorgehen?', [
         ('Aufklärung über Risiken, Einwilligungsfähigkeit dokumentieren, Unterschrift, Angehörige einbinden, Hausarzt/Wiederkontakt sichern', 1, 'Rechtssicher und patientenorientiert.'),
         ('Gegen seinen Willen transportieren', 0, 'Freiheitsberaubung bei Einwilligungsfähigkeit.'),
         ('Ohne Dokumentation abrücken', 0, 'Haftungsrisiko.')]),
      END('Die Tochter bleibt über Nacht; BZ-Kontrollen stündlich vereinbart; Hausarzt informiert.', dict(BZ=118, GCS=15))],
     NUN + '; ' + BGB, lvl=2),

case('TAK-C2', 'TAK', 'Patientenverfügung im Pflegeheim',
     '91-jährige Bewohnerin, pulslos aufgefunden. Pflegekraft reanimiert und reicht Ihnen eine Patientenverfügung.',
     dict(rhy='Asystolie', HF='–', RR='–', SpO2='–', AF=0, GCS=3),
     [N('a', 'Die Verfügung (unterschrieben, aktuell) lehnt Wiederbelebung bei Herz-Kreislauf-Stillstand ausdrücklich ab.', 'Wie handeln Sie?', [
         ('Wirksam und zutreffend → Reanimation beenden, Angehörige/Bevollmächtigte informieren', 1, 'Bindend nach § 1827 BGB.'),
         ('Weiter reanimieren, da der Notarzt immer reanimieren muss', 0, 'Falsch – der Wille bindet.'),
         ('Erst Hausarzt anrufen und so lange weiter reanimieren', 0, 'Bei eindeutiger Lage nicht nötig.')]),
      N('b', 'Keine Hinweise auf nicht-natürlichen Tod, keine sicheren Todeszeichen nach 5 min.', 'Was ist bei der Todesfeststellung zu beachten?', [
         ('Tod sicher feststellen (ggf. Wiederholung/ EKG-Nulllinie dokumentieren), Leichenschau nach Landesrecht veranlassen', 1, 'Auf sichere Todeszeichen warten bzw. nach Landesregelung.'),
         ('Weite Pupillen genügen als Todeszeichen', 0, 'Unsicher.'),
         ('Natürlicher Tod kann ohne Untersuchung bescheinigt werden', 0, 'Leichenschau am entkleideten Leichnam.')]),
      END('Angehörige werden begleitet, die Leichenschau übernimmt der Hausarzt.', dict(rhy='Asystolie'))],
     BGB + '; ' + ROSSAINT, lvl=2),

case('MANV-C1', 'MANV', 'Busunfall auf der A29',
     'Ihr RTW ist als erstes Fahrzeug an einem umgestürzten Reisebus. Viele Verletzte, Rufe, Benzingeruch.',
     dict(HF='–', RR='–', SpO2='–', AF='–', GCS='–'),
     [N('a', '—', 'Was tun Sie als ersteintreffendes Team zuerst?', [
         ('Erkunden, Gefahren erkennen, Lagemeldung mit Nachforderung (MANV-Alarm)', 1, 'Führung übernehmen.'),
         ('Sofort den ersten schreienden Patienten versorgen', 0, 'Wer schreit, atmet.'),
         ('In den Bus steigen und Verletzte herausholen', 0, 'Eigenschutz – Brandgefahr.')]),
      N('b', 'Vorsichtung nach mSTaRT: Patient A läuft herum, Platzwunde an der Stirn.', 'Kategorie?', [
         ('SK III (grün)', 1, 'Gehfähig.'), ('SK II (gelb)', 0, '—'), ('SK I (rot)', 0, '—')]),
      N('c', 'Patient B: nicht gehfähig, AF 36/min, Radialispuls tastbar.', 'Kategorie?', [
         ('SK I (rot)', 1, 'AF > 30/min.'), ('SK II (gelb)', 0, 'AF > 30 → rot.'), ('SK III (grün)', 0, '—')]),
      N('d', 'Patient C: nicht gehfähig, AF 20/min, Radialispuls tastbar, Rekap < 2 s, befolgt Aufforderungen; Unterschenkelfehlstellung.', 'Kategorie?', [
         ('SK II (gelb)', 1, 'Kein Sofortkriterium.'), ('SK I (rot)', 0, '—'), ('SK III (grün)', 0, 'Nicht gehfähig.')]),
      N('e', 'Patient D: keine Atmung, auch nicht nach Freimachen der Atemwege.', 'Einordnung?', [
         ('Tot (ex) – keine Reanimation im MANV, weiter zum Nächsten', 1, 'Ressourcen für Überlebende.'),
         ('SK I – sofort reanimieren', 0, 'Bindet das Team im MANV.'),
         ('SK II', 0, '—')]),
      END('LNA und OrgL übernehmen; Ihre Vorsichtungsergebnisse werden übergeben.')],
     MSTART + '; ' + MANVLIT, lvl=2),

case('MANV-C2', 'MANV', 'Als LNA: Transportprioritäten',
     'Sie sind LNA bei einer Explosion in einer Lagerhalle: 4 SK I, 9 SK II, 23 SK III. Verfügbar: 4 RTW, 1 RTH, 2 NEF; weitere Kräfte in 20 min.',
     dict(HF='–', RR='–', SpO2='–', AF='–', GCS='–'),
     [N('a', '—', 'Welche Patienten werden zuerst transportiert?', [
         ('Transportfähig stabilisierte SK I in geeignete Zentren, verteilt auf mehrere Kliniken', 1, 'Lastverteilung, Zentren nicht überlasten.'),
         ('Alle SK III zuerst, weil sie schnell abtransportierbar sind', 0, 'Falsche Priorität.'),
         ('Alle SK I in das nächstgelegene Krankenhaus', 0, 'Überlastung einer Klinik.')]),
      N('b', 'Ein SK-I-Patient mit 90 % VKOF-Verbrennung und Inhalationstrauma; Ressourcen sind knapp.', 'Wie entscheiden Sie?', [
         ('SK IV (blau) als ärztliche LNA-Entscheidung bei Ressourcenknappheit erwägen, palliativ betreuen, regelmäßig re-evaluieren', 1, 'Nur durch den Arzt, dynamisch.'),
         ('Sofort per RTH transportieren', 0, 'Bindet den RTH für einen Patienten mit infauster Prognose.'),
         ('Ohne Betreuung liegen lassen', 0, 'Betreuung/Analgesie gehört dazu.')]),
      N('c', 'Die SK-III-Patienten sammeln sich unruhig.', 'Wie werden sie versorgt?', [
         ('Betreuungsplatz mit Registrierung, Re-Sichtung, später Busse/KTW zu entfernteren Kliniken', 1, 'Entlastet die Zentren.'),
         ('Selbst nach Hause schicken ohne Registrierung', 0, 'Registrierung ist Pflicht.'),
         ('In die nächste Notaufnahme laufen lassen', 0, 'Überlastet die Kliniken.')]),
      END('Alle SK I binnen 70 min in vier Kliniken verteilt; Registrierung vollständig.')],
     SK + '; ' + MANVLIT),

case('GEF-C1', 'GEF', 'Tanklaster auf der Landstraße',
     'Ein Tanklaster liegt im Graben, eine Flüssigkeit läuft aus. Warntafel: oben 336, unten 1230. Der Fahrer sitzt benommen im Führerhaus.',
     dict(HF='?', RR='?', SpO2='?', AF='?', GCS='?'),
     [N('a', '—', 'Wie nähern Sie sich?', [
         ('Mit Wind im Rücken, Abstand ≥ 50 m, Absperrung, GAMS', 1, 'Eigenschutz.'),
         ('Direkt zum Führerhaus, der Fahrer braucht Hilfe', 0, 'Kontaminations- und Brandgefahr.'),
         ('Gegen den Wind, um Dämpfe zu riechen', 0, 'Gefährlich.')]),
      N('b', 'Kemler-Zahl 336.', 'Bedeutung?', [
         ('Leicht entzündbare Flüssigkeit, giftig', 1, '33 = leicht entzündbar, 6 = giftig (UN 1230 = Methanol).'),
         ('Ätzender Stoff', 0, '8 = ätzend.'),
         ('Radioaktiv', 0, '7 = radioaktiv.')]),
      N('c', 'Die Feuerwehr rettet den Fahrer unter PSA. Er ist mit Flüssigkeit getränkt.', 'Vor der Übernahme in den RTW?', [
         ('Notdekontamination: Kleidung entfernen, abspülen', 1, 'Verhindert Weiterexposition.'),
         ('Sofort in den RTW, Dekon in der Klinik', 0, 'Kontamination von Team und Fahrzeug.'),
         ('Nur Gesicht abwischen', 0, 'Unzureichend.')]),
      N('d', 'Methanol-Exposition, der Patient klagt später über verschwommenes Sehen.', 'Klinische Konsequenz?', [
         ('Giftnotruf, Zentrum mit Antidot (Fomepizol/Ethanol) und Dialyse', 1, 'Metabolische Azidose, Sehnervschaden.'),
         ('Sehstörung ist harmlos', 0, 'Warnzeichen.'),
         ('Natriumbicarbonat ersetzt die Antidottherapie', 0, 'Nur ergänzend.')]),
      END('Übergabe mit Stoffinformation (UN 1230, ERI-Card) an die Klinik.')],
     ADR + '; ' + FWDV500 + '; ' + GIZ),

case('GEF-C2', 'GEF', 'Amoklage an einer Schule',
     'Meldung: Schüsse in einer Gesamtschule. Polizei vor Ort, Lage unklar. Sie sind auf dem ersten NEF.',
     dict(HF='–', RR='–', SpO2='–', AF='–', GCS='–'),
     [N('a', '—', 'Wohin fahren Sie?', [
         ('In den von der Polizei/Leitstelle zugewiesenen Bereitstellungsraum außerhalb der Gefahrenzone', 1, 'Eigenschutz, Koordination.'),
         ('Direkt zum Schuleingang', 0, 'Rote Zone.'),
         ('Abwarten auf der Wache', 0, '—')]),
      N('b', 'Die Polizei bringt einen Schüler mit spritzender Oberschenkelblutung an die Übergabestelle (gelb/grün).', 'Erste Maßnahme?', [
         ('Tourniquet „hoch und fest“, dann <c>ABCDE', 1, 'Stop the bleeding.'),
         ('Vollständiger Bodycheck vor Blutstillung', 0, 'Kritische Blutung zuerst.'),
         ('Zugang und Volumen', 0, 'Erst Blutung stoppen.')]),
      N('c', 'Weitere Verletzte werden gemeldet; Gerüchte über einen zweiten Täter.', 'Taktisch richtig?', [
         ('Sammelpunkte variabel halten, rasch evakuieren, Rücksprache mit Polizei-Einsatzleitung', 1, 'Second-hit-Gefahr.'),
         ('Alle Patienten vor dem Haupteingang sammeln', 0, 'Vorhersehbares Ziel.'),
         ('Eigenmächtig in das Gebäude gehen', 0, 'Nur nach Freigabe.')]),
      END('Alle Verletzten über die Übergabepunkte evakuiert; Nachbesprechung (Debriefing) organisiert.')],
     TEL),
]
