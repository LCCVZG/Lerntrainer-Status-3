from qlib import *

Q = []
T = 'TRA'
Q += [
mtf('TRA-01', T, 'Blutstillung', 'Blutungskontrolle beim Schwerverletzten (S3 Polytrauma):', [
    ('Stufenschema an der Extremität: manuelle Kompression → Druckverband (ggf. mit Hämostyptikum) → Tourniquet.', 1, 'Empfehlungsgrad A.'),
    ('Ein Tourniquet wird sofort angelegt, wenn eine lebensbedrohliche Blutung anders nicht rechtzeitig gestoppt werden kann.', 1, 'Bei MANV, Dunkelheit, mehreren Verletzten oder Gefahrenlagen primär.'),
    ('Tranexamsäure 1 g als Bolus über 10 min bei drohendem oder manifestem hämorrhagischem Schock.', 1, 'Möglichst innerhalb von 3 h nach Trauma.'),
    ('Bei vermutetem SHT wird ebenfalls permissive Hypotension mit RRsys 70 mmHg angestrebt.', 0, 'Bei SHT Normotension: RRsys ≥ 90 mmHg.'),
    ('Ein Tourniquet wird präklinisch alle 15 min zur Reperfusion gelöst.', 0, 'Nicht intermittierend lockern – Blutverlust und Reperfusionsschaden.'),
], S3PT, 1),

mtf('TRA-02', T, 'Spannungspneumothorax', 'Spannungspneumothorax:', [
    ('Beim Beatmeten typisch: steigende Beatmungsdrücke, SpO₂-Abfall, Hypotonie, einseitig fehlendes Atemgeräusch.', 1, 'Halsvenenstauung kann bei Hypovolämie fehlen.'),
    ('Die Dekompression erfolgt umgehend, sobald der Verdacht klinisch besteht.', 1, 'Keine Bildgebung abwarten (Empfehlungsgrad A).'),
    ('Nadeldekompression im 2. ICR medioklavikulär oder im 4./5. ICR in der vorderen bis mittleren Axillarlinie.', 1, 'Ausreichend lange Kanüle; lateral oft geringere Thoraxwanddicke.'),
    ('Nach Nadeldekompression ist keine weitere Maßnahme nötig, da die Kanüle zuverlässig offen bleibt.', 0, 'Abknicken/Verlegung häufig – ggf. Minithorakotomie.'),
    ('Ein offener Pneumothorax wird mit einem an allen vier Seiten luftdicht verklebten Verband verschlossen.', 0, 'Ventilverband – sonst Gefahr eines Spannungspneumothorax.'),
], S3PT, 2),

mtf('TRA-03', T, 'Wirbelsäule', 'Wirbelsäulenverletzung und Immobilisation:', [
    ('Bewusstlose Traumapatienten gelten bis zum Beweis des Gegenteils als wirbelsäulenverletzt.', 1, 'Empfehlungsgrad A.'),
    ('Bei Sofortrettung (Feuer, Explosionsgefahr) hat die Rettung Vorrang vor der HWS-Immobilisation.', 1, 'Crash-Rettung.'),
    ('Das Spineboard ist das bevorzugte Transportmittel für längere Transporte.', 0, 'Spineboard = Rettungsmittel; Transport auf Vakuummatratze.'),
    ('Klinische Entscheidungsregeln (NEXUS, Canadian C-Spine Rule) helfen, unnötige Immobilisation zu vermeiden.', 1, 'Immobilisation hat Nebenwirkungen (Druck, Aspiration, Hirndruck).'),
    ('Eine Zervikalstütze allein garantiert eine vollständige HWS-Immobilisation.', 0, 'Nur in Kombination mit Kopffixierung/Vakuummatratze.'),
], S3PT, 1),

mtf('TRA-04', T, 'Becken & Schock', 'Beckenverletzung und hämorrhagischer Schock:', [
    ('Bei Verdacht auf instabile Beckenverletzung und Kreislaufinstabilität: Beckenschlinge auf Höhe der Trochanteres majores.', 1, 'Nicht über den Beckenkämmen.'),
    ('Das Becken wird zur Diagnostik mehrfach auf Stabilität geprüft.', 0, 'Wiederholte Kompression löst Gerinnsel – Verdacht reicht.'),
    ('Hypothermie, Azidose und Koagulopathie bilden die „letale Trias“.', 1, 'Wärmeerhalt ist Blutungstherapie.'),
    ('Volumentherapie mit balancierten, isotonen Kristalloiden, idealerweise gewärmt.', 1, 'Empfehlungsgrad A.'),
    ('Kolloide (HES) sind beim Trauma Mittel der Wahl.', 0, 'Nicht empfohlen (Niere, Gerinnung).'),
], S3PT, 1),

mtf('TRA-05', T, 'Verbrennung', 'Verbrennungen:', [
    ('Neunerregel Erwachsene: Kopf 9 %, je Arm 9 %, Rumpf vorn 18 %, hinten 18 %, je Bein 18 %, Genitale 1 %.', 1, 'Für Kinder angepasste Tabellen (größerer Kopf).'),
    ('Die Handfläche des Patienten (inkl. Finger) entspricht ca. 5 % KOF.', 0, 'Etwa 1 %.'),
    ('Großflächige Verbrennungen (> 20 % VKOF) bei Erwachsenen werden 30 min mit kaltem Wasser gekühlt.', 0, 'Hypothermiegefahr – nur kleine Flächen kurz kühlen, Wärmeerhalt.'),
    ('Erstgradige Verbrennungen (Rötung ohne Blasen) werden bei der VKOF nicht mitgezählt.', 1, 'Nur ab Grad 2.'),
    ('Hinweise auf Inhalationstrauma: Ruß im Mund, versengte Nasenhaare, Heiserkeit, Stridor.', 1, 'Frühe Atemwegssicherung erwägen – Schwellung nimmt zu.'),
], BURN, 1),

mtf('TRA-06', T, 'Amputation & Pfählung', 'Amputations- und Pfählungsverletzungen:', [
    ('Amputat trocken in sterile Kompressen, in einen Beutel, diesen in einen zweiten Beutel mit Eiswasser.', 1, 'Indirekte Kühlung.'),
    ('Das Amputat wird direkt auf Eis gelegt, um maximal zu kühlen.', 0, 'Erfrierungsschäden – Replantation gefährdet.'),
    ('Pfählende Gegenstände werden belassen und fixiert.', 1, 'Tamponieren die Blutung; Entfernung erst im OP.'),
    ('Bei Teilamputation wird die Gewebebrücke durchtrennt, um den Transport zu erleichtern.', 0, 'Gewebebrücke erhalten (Gefäße/Nerven).'),
    ('Blutung am Amputationsstumpf: Tourniquet, wenn der Druckverband nicht ausreicht.', 1, 'Zeit dokumentieren.'),
], S3PT + '; ' + ROSSAINT, 1),

mtf('TRA-07', T, 'Analgesie', 'Analgesie beim Traumapatienten (S3 Polytrauma):', [
    ('Zielwert NRS ≤ 4.', 1, 'Empfehlungsgrad A.'),
    ('Fentanyl, Ketamin und Morphin sind bei spontan atmenden Patienten vergleichbar wirksam.', 1, 'Auswahl nach Kreislauf und Erfahrung.'),
    ('Im Schock ist die intramuskuläre Opioidgabe die bevorzugte Route.', 0, 'Unzuverlässige Resorption – i.v., i.o. oder i.n.'),
    ('Schienung und Lagerung sind Teil der Analgesie.', 1, 'Physikalische Maßnahmen zusätzlich.'),
    ('Analgesie verschleiert die Diagnostik und wird deshalb bis zur Klinik zurückgehalten.', 0, 'Adäquate Analgesie ist Pflicht.'),
], S3PT, 1),

order('TRA-08', T, '<c>ABCDE', 'Bringe die Prioritäten des <c>ABCDE-Schemas in die richtige Reihenfolge.', [
    '<c> kritische Blutung stoppen',
    'A – Atemweg (mit HWS-Stabilisierung)',
    'B – Belüftung/Atmung',
    'C – Kreislauf',
    'D – Neurologie',
    'E – Exposure/Entkleiden, Wärmeerhalt',
], '„Treat first what kills first“ – lebensbedrohliche Blutungen vor dem Atemweg.', S3PT, 1),

order('TRA-09', T, 'Tourniquet', 'Anlage eines Tourniquets:', [
    'Blutungsquelle identifizieren, Eigenschutz',
    'Tourniquet 5–7 cm proximal der Wunde (nicht über einem Gelenk) anlegen; bei unklarer Quelle „hoch und fest“',
    'Festziehen und Knebel drehen, bis Blutung steht und distaler Puls fehlt',
    'Knebel sichern',
    'Uhrzeit dokumentieren',
    'Reevaluieren – ggf. zweites Tourniquet proximal',
], 'Ein unzureichend angezogenes Tourniquet staut nur venös und verstärkt die Blutung.', S3PT + '; ' + TEL, 1),

match('TRA-10', T, 'Mechanismus → Verdacht', 'Ordne dem Befund die Verdachtsdiagnose zu.', [
    ['Lenkradabdruck am Thorax', 'Herzkontusion/Aortenverletzung'],
    ['Gurtmarke am Unterbauch', 'Darm-/Mesenterialverletzung, LWS-Flexionsfraktur'],
    ['Brillenhämatom', 'Schädelbasisfraktur'],
    ['Paradoxe Atembewegung', 'Instabiler Thorax (Rippenserienfraktur)'],
    ['Prellmarke linker Oberbauch mit Schock', 'Milzruptur'],
], 'Unfallmechanismus und äußere Zeichen lenken die Verdachtsdiagnose und Zielklinik.', ROSSAINT, 1),

match('TRA-11', T, 'Schockraum-Kriterien', 'Ordne dem Kriterium den Grenzwert für die Schockraumaktivierung zu (S3).', [
    ['Systolischer Blutdruck', '< 90 mmHg'],
    ['Schockindex', '> 0,9'],
    ['GCS', '≤ 12'],
    ['Körperkerntemperatur', '< 35,0 °C'],
    ['Herzfrequenz', '> 120/min'],
], 'Pathologische Vitalparameter, Verletzungsmuster und Unfallmechanismus führen zur Schockraumalarmierung.', S3PT2, 2),

cloze('TRA-12', T, 'Permissive Hypotension', 'Bei nicht beherrschbarer Blutung ohne SHT werden ein RRsys von ca. {0} mmHg bzw. ein MAP von ca. {1} mmHg toleriert; bei SHT RRsys ≥ {2} mmHg.', [
    ['80', ['60', '100', '120']],
    ['65', ['50', '80', '90']],
    ['90', ['70', '80', '120']],
], 'Ohne Hinweis auf Volumenmangel auf Volumen verzichten.', S3PT, 1),

cloze('TRA-13', T, 'Parkland-Formel', 'Parkland-Formel: {0} ml × kg KG × % VKOF in 24 h, davon die Hälfte in den ersten {1} h ab {2}.', [
    ['4', ['2', '10', '1']],
    ['8', ['4', '12', '24']],
    ['Unfallzeitpunkt', ['Klinikaufnahme', 'Infusionsbeginn', 'Diagnosestellung']],
], 'Präklinisch Startrate nach ABLS: ≥ 14 J. 500 ml/h, 6–13 J. 250 ml/h, ≤ 5 J. 125 ml/h.', BURN, 2),

num('TRA-14', T, 'Parkland', 'Verbrennung bei 80 kg, 30 % VKOF (Grad 2–3). Volumen nach Parkland in den ersten 8 h (ml)?', 'ml', 4800, 100,
    '4 × 80 × 30 = 9600 ml/24 h → Hälfte = 4800 ml in 8 h.', BURN, 2),

num('TRA-15', T, 'Neunerregel', 'Erwachsener: Verbrennung des ganzen rechten Arms und der gesamten Rumpfvorderseite (Grad 2). % VKOF?', '%', 27, 0,
    '9 % + 18 % = 27 %.', BURN, 1),

num('TRA-16', T, 'Schockindex', 'HF 126/min, RR 90/60 mmHg. Schockindex?', '', 1.4, 0.05,
    '126 ÷ 90 = 1,4 – deutlicher Schockhinweis.', S3PT2, 1),
]

T = 'PAE'
Q += [
mtf('PAE-01', T, 'Kinderreanimation', 'Reanimation von Säuglingen und Kindern (ERC 2025):', [
    ('Die Reanimation beginnt mit 5 initialen Beatmungen.', 1, 'Hypoxie ist die häufigste Ursache.'),
    ('Laien ohne Kinder-Ausbildung dürfen nicht 30:2 reanimieren.', 0, 'Besser 30:2 als nichts; Profis 15:2.'),
    ('Adrenalin 10 µg/kg i.v./i.o. (max. 1 mg) alle 3–5 min.', 1, '0,01 mg/kg.'),
    ('Erster Schock 4 J/kg; bei refraktärem VF stufenweise Steigerung bis max. 8 J/kg.', 1, 'Nicht über die Erwachsenen-Maximalenergie.'),
    ('Bei Säuglingen werden die Kompressionen mit beiden Handballen durchgeführt.', 0, 'Zwei-Daumen-Technik (umgreifend) oder zwei Finger.'),
], ERC_PLS, 1),

mtf('PAE-02', T, 'Krupp & Epiglottitis', 'Atemnot mit Stridor beim Kleinkind:', [
    ('Pseudokrupp: bellender Husten, inspiratorischer Stridor, meist nachts, Infektanamnese.', 1, 'Viral, 6 Monate bis 3 Jahre.'),
    ('Kortikosteroide (z. B. Dexamethason 0,15–0,6 mg/kg p.o. oder Prednison rektal) sind Basis der Therapie.', 1, 'Wirkt nach 1–2 h.'),
    ('Beim schweren Krupp mit Ruhestridor wird Adrenalin vernebelt.', 1, 'Rasche, aber kurze Wirkung – Überwachung.'),
    ('Bei Verdacht auf Epiglottitis wird der Rachen mit dem Spatel inspiziert.', 0, 'Gefahr der kompletten Verlegung – keine Manipulation.'),
    ('Das Kind wird zur Untersuchung hingelegt und von den Eltern getrennt.', 0, 'Aufregung verschlechtert den Stridor – in Elternarmen, sitzend.'),
], ROSSAINT + '; ' + NFG, 1),

mtf('PAE-03', T, 'Fieberkrampf', 'Fieberkrampf:', [
    ('Einfacher Fieberkrampf: generalisiert, < 15 min, keine Wiederholung in 24 h, Alter ca. 6 Monate bis 5 Jahre.', 1, 'Sonst „komplizierter“ Fieberkrampf.'),
    ('Midazolam buccal oder intranasal ist eine Option ohne Zugang.', 1, 'Dosis nach Alter/Gewicht.'),
    ('Fiebersenkende Mittel verhindern Rezidive sicher.', 0, 'Kein Beleg; dienen dem Wohlbefinden.'),
    ('Nach einem Fieberkrampf ist eine Meningitis sicher ausgeschlossen.', 0, 'Besonders bei Säuglingen an ZNS-Infektion denken.'),
    ('Ein Anfall > 5 min wird medikamentös durchbrochen.', 1, 'Wie beim Status epilepticus.'),
], ROSSAINT + '; ' + NFG, 1),

mtf('PAE-04', T, 'Neugeborenenversorgung', 'Versorgung des Neugeborenen (ERC NLS):', [
    ('Wärmeerhalt: abtrocknen, warme Tücher; Frühgeborene < 32 SSW in Folienbeutel.', 1, 'Hypothermie erhöht die Letalität.'),
    ('Bei Apnoe/Schnappatmung: 5 Blähbeatmungen (je 2–3 s Inspiration).', 1, 'Füllt die Lunge mit Luft.'),
    ('Thoraxkompressionen bei HF < 60/min trotz 30 s effektiver Beatmung, Verhältnis 3:1.', 1, 'Mit 100 % O₂.'),
    ('Routinemäßiges Absaugen von Mund und Nase wird bei jedem Neugeborenen empfohlen.', 0, 'Nur bei Verlegung.'),
    ('Ein vitales Neugeborenes wird sofort abgenabelt, um eine Polyglobulie zu vermeiden.', 0, 'Verzögertes Abnabeln (≥ 60 s) wird empfohlen.'),
], ERC_NLS, 2),

mtf('PAE-05', T, 'Geburtshilfliche Notfälle', 'Geburtshilfliche Notfälle:', [
    ('Vena-cava-Kompressionssyndrom: Linksseitenlage (ab ca. 20. SSW).', 1, 'Entlastet V. cava und Aorta.'),
    ('Eklampsie: Magnesiumsulfat 4–6 g i.v. über 15–20 min.', 1, 'Erhaltung 1–2 g/h; Reflexe und Atmung überwachen.'),
    ('Postpartale Blutung: Uterusmassage, Oxytocin, Tranexamsäure 1 g, Blase entleeren.', 1, 'Die „4 T“: Tonus, Trauma, Tissue, Thrombin.'),
    ('Nabelschnurvorfall: Die Nabelschnur wird in die Scheide zurückgeschoben.', 0, 'Kindlichen Kopf hochschieben, Beckenhochlagerung/Knie-Ellenbogen-Lage, nicht reponieren.'),
    ('Eine Schulterdystokie wird durch kräftigen Fundusdruck gelöst.', 0, 'Fundusdruck verkeilt weiter – McRoberts-Manöver und suprasymphysärer Druck.'),
], ROSSAINT, 2),

mtf('PAE-06', T, 'Kindliche Besonderheiten', 'Physiologische Besonderheiten bei Kindern:', [
    ('Gewichtsschätzung für 1–10 Jahre: (Alter + 4) × 2.', 1, 'Alternativ Maßband-Systeme.'),
    ('Die normale Herzfrequenz eines Säuglings liegt bei 60–80/min.', 0, 'Ca. 110–160/min.'),
    ('Hypotonie ist beim Kind ein frühes Schockzeichen.', 0, 'Spätes Zeichen – vorher Tachykardie, verlängerte Rekapillarisierung.'),
    ('Eine Bradykardie beim kritisch kranken Kind ist meist Folge einer Hypoxie.', 1, 'Erst oxygenieren/beatmen.'),
    ('Säuglinge sind bevorzugt Nasenatmer – eine verlegte Nase kann relevante Atemnot verursachen.', 1, 'Nase freimachen.'),
], ERC_PLS + '; ' + ROSSAINT, 1),

order('PAE-07', T, 'Neugeborenenversorgung', 'Erstversorgung eines nicht vitalen Neugeborenen:', [
    'Uhr starten, abtrocknen, warm einwickeln',
    'Atmung, Herzfrequenz und Tonus beurteilen',
    'Atemwege öffnen (Kopf in Neutralposition)',
    '5 Blähbeatmungen bei Apnoe/Schnappatmung',
    'Thoraxbewegung und HF prüfen, Beatmung 30 s fortführen',
    'Bei HF < 60/min: Thoraxkompressionen 3:1',
], 'Beatmung ist die wichtigste Maßnahme – Kompressionen erst nach effektiver Belüftung.', ERC_NLS, 1),

order('PAE-08', T, 'Spontangeburt', 'Bringe die Schritte einer normalen Spontangeburt (Austreibungs- und Nachgeburtsphase) in die richtige Reihenfolge.', [
    'Kopf entwickeln, Dammschutz',
    'Nabelschnurumschlingung tasten und ggf. lösen',
    'Vordere Schulter entwickeln (Kopf leicht nach unten führen)',
    'Hintere Schulter entwickeln (Kopf nach oben führen)',
    'Kind abtrocknen, Haut-zu-Haut auf die Mutter',
    'Abnabeln nach ≥ 60 s (zwei Klemmen)',
    'Plazentageburt abwarten, Blutung beobachten',
], 'Nicht an der Nabelschnur ziehen; Plazenta mit in die Klinik nehmen.', ROSSAINT, 2),

match('PAE-09', T, 'Tubusgrößen', 'Ordne dem Alter die passende Tubusgröße (ID, gecufft) zu.', [
    ['Reifes Neugeborenes', '3,0'],
    ['2 Jahre', '4,0'],
    ['6 Jahre', '5,0'],
    ['10 Jahre', '6,0'],
    ['Erwachsene Frau', '7,0'],
], 'Gecufft: Alter/4 + 3,5 (ab 2 Jahren).', ERC_PLS, 2),

match('PAE-10', T, 'APGAR', 'Ordne dem APGAR-Kriterium den Befund für 2 Punkte zu.', [
    ['Atmung', 'regelmäßig, kräftiges Schreien'],
    ['Puls', '> 100/min'],
    ['Grundtonus', 'aktive Bewegungen'],
    ['Aussehen (Hautfarbe)', 'rosig am ganzen Körper'],
    ['Reflexe', 'Schreien/Niesen bei Reiz'],
], 'Erhebung nach 1, 5 und 10 Minuten.', ERC_NLS, 1),

cloze('PAE-11', T, 'Kinderreanimation', 'Kinderreanimation: Adrenalin {0} µg/kg, Amiodaron {1} mg/kg, Defibrillation initial {2} J/kg.', [
    ['10', ['1', '100', '50']],
    ['5', ['1', '10', '0,5']],
    ['4', ['2', '10', '1']],
], 'Amiodaron max. 300 mg pro Gabe.', ERC_PLS, 1),

cloze('PAE-12', T, 'APGAR', 'Der APGAR-Score wird nach {0}, {1} und {2} Minuten erhoben.', [
    ['1', ['2', '3', '0']],
    ['5', ['4', '6', '3']],
    ['10', ['15', '20', '30']],
], 'Reanimationsmaßnahmen werden nicht vom APGAR-Wert nach 1 min abhängig gemacht.', ERC_NLS, 1),

num('PAE-13', T, 'Gewichtsschätzung', 'Kind, 4 Jahre. Geschätztes Gewicht (kg) nach (Alter + 4) × 2?', 'kg', 16, 0,
    '(4 + 4) × 2 = 16 kg.', ERC_PLS, 1),

num('PAE-14', T, 'Adrenalin beim Kind', 'Kind, 16 kg, Kreislaufstillstand. Adrenalin-Einzeldosis in µg?', 'µg', 160, 0,
    '10 µg/kg × 16 = 160 µg = 0,16 mg (z. B. 1 mg auf 10 ml → 1,6 ml).', ERC_PLS, 1),

num('PAE-15', T, 'Defibrillation beim Kind', 'Kind, 16 kg, Kammerflimmern. Energie für den ersten Schock (J)?', 'J', 64, 6,
    '4 J/kg × 16 = 64 J – nächstmögliche Geräteeinstellung wählen.', ERC_PLS, 1),

num('PAE-16', T, 'Volumenbolus', 'Kind, 25 kg, im Schock. Volumen für einen Bolus von 10 ml/kg (ml)?', 'ml', 250, 0,
    '10 × 25 = 250 ml balancierte Kristalloide, danach reevaluieren.', ERC_PLS, 1),
]
