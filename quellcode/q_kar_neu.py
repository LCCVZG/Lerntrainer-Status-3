from qlib import *

Q = []
T = 'KAR'
Q += [
mtf('KAR-01', T, 'ACS – Akuttherapie', 'Präklinische Therapie bei Verdacht auf akutes Koronarsyndrom:', [
    ('ASS 150–300 mg p.o. (bzw. 75–250 mg i.v.) erhalten alle Patienten ohne Kontraindikation.', 1, 'NUN: 300 mg p.o. bzw. 250 mg i.v.'),
    ('Unfraktioniertes Heparin 70–100 IE/kg i.v. bei STEMI mit geplanter primärer PCI.', 1, 'NUN: 5000 IE (≈ 70 IE/kg).'),
    ('Sauerstoff wird beim ACS routinemäßig unabhängig von der SpO₂ gegeben.', 0, 'Nur bei SpO₂ < 90 %.'),
    ('Nitrate sind bei Hypotonie, Rechtsherzinfarkt und nach PDE-5-Hemmer-Einnahme kontraindiziert.', 1, 'Gefahr schwerer Hypotonie.'),
    ('Beim NSTE-ACS wird eine routinemäßige präklinische P2Y12-Vorbehandlung empfohlen.', 0, 'ESC 2023: bei früh-invasiver Strategie nicht routinemäßig.'),
], ESC_ACS + '; ' + NUN, 1),

mtf('KAR-02', T, 'Reperfusion', 'Reperfusionsstrategie beim akuten Koronarverschluss:', [
    ('Primäre PCI ist Strategie der Wahl, wenn von Diagnose bis Drahtpassage ≤ 120 min erwartet werden.', 1, 'Sonst Fibrinolyse.'),
    ('Ist die PCI nicht rechtzeitig verfügbar, soll die Fibrinolyse innerhalb von 10 min nach Diagnose beginnen.', 1, 'Danach Transport in ein PCI-Zentrum.'),
    ('Fehlende ST-Hebungen schließen einen akuten Koronarverschluss aus.', 0, 'Ein relevanter Anteil der Verschlüsse (OMI) erfüllt die STEMI-Kriterien nicht.'),
    ('Zielklinik ist immer das nächstgelegene Krankenhaus, unabhängig von der PCI-Bereitschaft.', 0, 'Direkt in ein Zentrum mit 24/7-Katheterlabor.'),
    ('Direktübergabe ins Katheterlabor unter Umgehung der Notaufnahme verkürzt die Ischämiezeit.', 1, 'Voranmeldung mit EKG-Übertragung.'),
], ESC_ACS, 2),

mtf('KAR-03', T, 'OMI-Konzept', 'Aussagen zum Okklusionsinfarkt (OMI) nach dem Konzept von Smith/Meyers:', [
    ('In Studien hatte etwa ein Viertel der als NSTEMI eingeordneten Patienten ein verschlossenes Infarktgefäß.', 1, 'Diese Patienten erhalten oft verzögert die Reperfusion.'),
    ('Hyperakute T-Wellen (breit, symmetrisch, groß im Verhältnis zum QRS) können das früheste Zeichen eines Verschlusses sein.', 1, 'Häufig vor der ST-Hebung.'),
    ('Eine in V1–V4 maximale ST-Senkung spricht bei ACS-Symptomen für einen posterioren OMI.', 1, 'Meyers et al. (JAHA 2021): hoch spezifisch.'),
    ('Jede ST-Senkung in aVL bei inferiorer ST-Hebung spricht für eine Perikarditis.', 0, 'Reziproke Senkung in aVL spricht für einen inferioren OMI und gegen Perikarditis.'),
    ('Ein normales Erst-EKG schließt einen OMI aus; Folge-EKGs sind entbehrlich.', 0, 'Serielle EKGs bei anhaltenden Beschwerden!'),
], SMITH_OMI + '; ' + SMITH_DW, 3, memo='OMI statt STEMI: Verschluss ≠ ST-Hebungs-Kriterien.'),

mtf('KAR-04', T, 'Tachykardien', 'Tachykarde Rhythmusstörungen (ERC 2025):', [
    ('Instabile Tachykardie (Schock, Synkope, Ischämie, Herzinsuffizienz): synchronisierte Kardioversion unter Analgosedierung.', 1, 'Instabil = elektrisch.'),
    ('Nach erfolgloser Kardioversion: Amiodaron 300 mg über 10–20 min, dann erneut kardiovertieren.', 1, 'Alternativ Procainamid.'),
    ('Stabile regelmäßige Schmalkomplex-Tachykardie: zunächst vagale Manöver (modifizierter Valsalva), dann Adenosin.', 1, 'Modifizierter Valsalva: pressen, dann flach mit Beinhochlagerung.'),
    ('Adenosin wird langsam über 2 min injiziert, um Nebenwirkungen zu vermeiden.', 0, 'Halbwertszeit Sekunden: schneller Bolus, sofort nachspülen.'),
    ('Bei unregelmäßiger Breitkomplex-Tachykardie mit Präexzitation ist Verapamil Mittel der Wahl.', 0, 'AV-Knoten-Blocker sind bei präexzitiertem VHF kontraindiziert (Kammerflimmern).'),
], ERC_TACHY, 2),

mtf('KAR-05', T, 'Bradykardien', 'Bradykardie mit Instabilitätszeichen:', [
    ('Atropin ist bei herztransplantierten Patienten Mittel der Wahl.', 0, 'Denerviertes Herz: Atropin meiden; Aminophyllin/Adrenalin.'),
    ('Beim AV-Block III mit breitem Ersatzrhythmus ist Atropin oft unwirksam – früh Adrenalin oder Pacing.', 1, 'Block unterhalb des AV-Knotens.'),
    ('Transkutanes Pacing ist schmerzlos und benötigt keine Analgosedierung.', 0, 'Schmerzhaft – Analgosedierung.'),
    ('Beim Pacing muss der elektrische Capture durch einen tastbaren Puls bestätigt werden.', 1, 'Femoral tasten – Artefakte täuschen QRS vor.'),
    ('Eine Bradykardie bei Betablocker-Intoxikation kann mit Glukagon behandelt werden.', 1, 'Rezeptorunabhängige cAMP-Steigerung.'),
], ERC_TACHY, 2),

mtf('KAR-06', T, 'Lungenembolie', 'Akute Lungenembolie:', [
    ('Hochrisiko-LE = LE mit Schock, persistierender Hypotonie oder Reanimationspflicht.', 1, 'ESC 2019.'),
    ('Beim Hochrisiko-Patienten ist die systemische Thrombolyse indiziert.', 1, 'Alternativ interventionell/chirurgisch.'),
    ('Ein unauffälliges EKG schließt eine LE aus.', 0, 'EKG ist unspezifisch; Sinustachykardie häufigster Befund.'),
    ('Bei begründetem Verdacht ist UFH (z. B. 5000 IE i.v.) präklinisch vertretbar, wenn keine Kontraindikationen bestehen.', 1, 'Antikoagulation bei hoher Wahrscheinlichkeit nicht verzögern.'),
    ('Großzügige Volumengabe (> 2 l) ist die wichtigste Maßnahme bei Rechtsherzversagen.', 0, 'Volumen überdehnt den RV; vorsichtig, eher Noradrenalin.'),
], ESC_LE, 2),

mtf('KAR-07', T, 'Hypertensiver Notfall', 'Hypertensiver Notfall und Aortendissektion:', [
    ('Ein hypertensiver Notfall ist durch akute Endorganschäden definiert, nicht allein durch die Höhe des Blutdrucks.', 1, 'Ohne Organschaden: hypertensive Entgleisung.'),
    ('In der ersten Stunde wird der MAP um höchstens 20–25 % gesenkt (Ausnahmen: Dissektion, Lungenödem).', 1, 'Zu schnelle Senkung → zerebrale/koronare Ischämie.'),
    ('Bei Aortendissektion werden RRsys ≤ 120 mmHg und HF ≈ 60/min angestrebt.', 1, 'Wandspannung senken, Betablocker + Vasodilatator.'),
    ('Urapidil ist wegen Reflextachykardie bei KHK kontraindiziert.', 0, 'Urapidil verursacht kaum Reflextachykardie (zentrale 5-HT1A-Wirkung); NUN: 5-mg-Schritte, max. 25 mg.'),
    ('Nifedipin-Kapseln sublingual sind Mittel der Wahl zur raschen Senkung.', 0, 'Unkontrollierbarer RR-Abfall – obsolet.'),
], ESC_AORTA + '; ' + NUN, 2),

order('KAR-08', T, 'Kardioversion – Ablauf', 'Bringe die Schritte der synchronisierten Kardioversion in die richtige Reihenfolge.', [
    'Indikation prüfen, Team briefen, Pads anterolateral oder a.-p. kleben',
    'Analgosedierung und Atemwegsbereitschaft',
    'Synchronisation aktivieren, Marker auf den R-Zacken prüfen',
    'Energie wählen und laden',
    'Sicherheitscheck („Alle weg, Sauerstoff weg“), Schock auslösen',
    'Rhythmus kontrollieren – vor erneutem Schock Synchronisation erneut prüfen',
], 'Viele Geräte schalten die Synchronisation nach dem Schock ab – vor jedem weiteren Versuch kontrollieren.', ERC_TACHY, 2),

match('KAR-09', T, 'EKG-Muster nach Smith', 'Ordne jedem EKG-Muster seine Bedeutung zu.', [
    ['De-Winter-T-Wellen', 'Proximaler LAD-Verschluss (OMI-Äquivalent)'],
    ['Wellens-Muster A (biphasische T in V2–V3, schmerzfrei)', 'Kritische LAD-Stenose nach spontaner Reperfusion'],
    ['ST-Senkung maximal in V1–V4', 'Posteriorer OMI'],
    ['ST-Senkung in aVL bei inferiorer Hebung', 'Reziproke Veränderung bei inferiorem OMI'],
    ['ST/S-Verhältnis ≤ −0,25 bei LSB', 'OMI trotz Linksschenkelblock (Smith-Sgarbossa)'],
], 'Alle Muster verlangen eine dringliche Koronardiagnostik, auch ohne klassische STEMI-Kriterien.', SMITH, 3),

match('KAR-10', T, 'Schockformen', 'Ordne der Schockform das typische Befundmuster zu.', [
    ['Kardiogen', 'HZV ↓, Füllungsdrücke ↑, kalte Peripherie, Lungenstauung'],
    ['Hypovolämisch', 'HZV ↓, Füllungsdrücke ↓, flache Halsvenen'],
    ['Distributiv (septisch, früh)', 'SVR ↓, warme Peripherie'],
    ['Obstruktiv', 'gestaute Halsvenen trotz Hypotonie (Tamponade, Spannungspneu, LE)'],
    ['Neurogen', 'Hypotonie mit Bradykardie, warme Haut'],
], 'Halsvenen, Hauttemperatur und Herzfrequenz erlauben eine schnelle Einordnung am Patienten.', MARINO, 2),

cloze('KAR-11', T, 'Adenosin', 'Adenosin bei stabiler Schmalkomplex-Tachykardie: initial {0}, dann {1}, dann {2} als schneller Bolus. Eine Kontraindikation ist u. a. {3}.', [
    ['6 mg', ['3 mg', '12 mg', '0,5 mg']],
    ['12 mg', ['6 mg', '24 mg', '1 mg']],
    ['18 mg', ['12 mg', '36 mg', '3 mg']],
    ['schweres Asthma', ['Hypertonie', 'Vorhofflattern', 'Diabetes']],
], 'Patient vorwarnen (kurzes Engegefühl, „Herzstillstand-Gefühl“); 12-Kanal-EKG mitlaufen lassen.', ERC_TACHY, 2),

cloze('KAR-12', T, 'Schockindex', 'Schockindex = {0} geteilt durch {1}; ein Wert > {2} gilt als Schockhinweis und ist ein Kriterium für die Schockraumaktivierung.', [
    ['Herzfrequenz', ['systolischer RR', 'MAP', 'Atemfrequenz']],
    ['systolischen Blutdruck', ['Herzfrequenz', 'diastolischen Blutdruck', 'SpO₂']],
    ['0,9', ['0,3', '0,5', '2,5']],
], 'Vorsicht bei Betablockade, Schrittmacher und jungen Patienten.', S3PT2, 1),

num('KAR-13', T, 'Heparin', 'STEMI, Patient 85 kg. Heparin 70 IE/kg i.v. – welche Dosis (IE, auf 500 gerundet)?', 'IE', 6000, 250,
    '70 × 85 = 5950 ≈ 6000 IE. Der NUN-Pfad nennt pauschal 5000 IE.', ESC_ACS + '; ' + NUN, 1),

num('KAR-14', T, 'Noradrenalin', 'Noradrenalin 5 mg auf 50 ml (0,1 mg/ml). Ziel: 0,1 µg/kg/min bei 80 kg. Laufrate in ml/h?', 'ml/h', 4.8, 0.2,
    '0,1 × 80 = 8 µg/min = 480 µg/h = 0,48 mg/h → 4,8 ml/h.', PHARM, 2),

img('KAR-15', T, 'Breitkomplextachykardie', 'vt', '62-Jähriger, Z. n. Herzinfarkt, Palpitationen, RR 85/50 mmHg, kaltschweißig. Diagnose und Konsequenz?', [
    'Monomorphe VT – instabil: synchronisierte Kardioversion',
    'Sinustachykardie bei Volumenmangel – Volumen',
    'Vorhofflattern 2:1 – Adenosin',
    'Torsade de pointes – Magnesium'],
    'Regelmäßige Breitkomplextachykardie bei KHK = VT bis zum Beweis des Gegenteils. Instabil → Kardioversion (initial 120–150 J), danach Amiodaron.', ERC_TACHY, 1),

img('KAR-16', T, 'Bradykardie', 'avb3', '84-Jährige, Schwindel, HF 36/min. Was zeigt der Streifen?', [
    'AV-Block III. Grades mit breitem Kammerersatzrhythmus',
    'AV-Block II Typ Wenckebach',
    'Sinusbradykardie',
    'Vorhofflimmern mit langsamer Überleitung'],
    'P-Wellen regelmäßig (≈ 85/min), QRS regelmäßig (≈ 36/min), keine Beziehung. Atropin oft wirkungslos – Adrenalin 2–10 µg/min oder Pacing.', ERC_TACHY, 1),

img('KAR-17', T, 'Bradykardie', 'mob2', 'Patient mit Synkope. Rhythmusstreifen:', [
    'AV-Block II Typ Mobitz II (3:2)',
    'AV-Block II Typ Wenckebach',
    'AV-Block I',
    'Blockierte supraventrikuläre Extrasystolen'],
    'Konstante PQ-Zeit, dann plötzlich ausfallender QRS. Gefahr des Übergangs in AV-Block III – Schrittmacherbereitschaft.', ERC_TACHY, 2),

img('KAR-18', T, 'Tachykardie', 'afib', '78-Jähriger, Palpitationen seit gestern, RR 130/80. Rhythmus?', [
    'Tachyarrhythmia absoluta bei Vorhofflimmern',
    'Sinustachykardie mit Extrasystolen',
    'Vorhofflattern 2:1',
    'AV-Knoten-Reentry'],
    'Absolut unregelmäßige RR-Abstände, keine P-Wellen, flimmernde Grundlinie. Stabil: Frequenzkontrolle, Antikoagulation klären.', ERC_TACHY, 1),

img('KAR-19', T, 'Tachykardie', 'svt', '24-Jährige, plötzlich Herzrasen, RR 115/70. Rhythmus?', [
    'AV-Knoten-Reentry-Tachykardie (regelmäßig, schmal)',
    'Sinustachykardie',
    'Vorhofflimmern',
    'Ventrikuläre Tachykardie'],
    'Regelmäßige Schmalkomplextachykardie um 190/min ohne sichtbare P-Wellen. Modifiziertes Valsalva, dann Adenosin 6–12–18 mg.', ERC_TACHY, 1),

img('KAR-20', T, 'Tachykardie', 'flutter', '70-Jähriger, Dyspnoe, Herzfrequenz konstant genau 150/min. Rhythmus?', [
    'Vorhofflattern mit 2:1-Überleitung',
    'Sinustachykardie',
    'AV-Knoten-Reentry',
    'Vorhofflimmern'],
    'Sägezahnartige Flatterwellen (≈ 300/min) in II; eine starre Frequenz von 150/min ist verdächtig. Adenosin demaskiert die Flatterwellen, beendet das Flattern aber nicht.', ERC_TACHY, 2),

img('KAR-21', T, '12-Kanal-EKG', 'inf_omi', '58-Jähriger, seit 40 min retrosternaler Druck, Übelkeit, RR 100/60. Befund?', [
    'Inferiorer OMI mit reziproker ST-Senkung in aVL – Katheterlabor',
    'Akute Perikarditis',
    'Frühe Repolarisation (Normvariante)',
    'Lungenembolie mit SI-QIII-Typ'],
    'ST-Hebung II, III, aVF (III > II), ST-Senkung und T-Negativierung in aVL. Leichte ST-Hebung in V1 → an RV-Beteiligung denken: V4R ableiten, keine Nitrate, Volumen vorsichtig.', SMITH + '; ' + ESC_ACS, 2),

img('KAR-22', T, '12-Kanal-EKG', 'ant_hyper', '46-Jähriger, seit 20 min Brustschmerz. Wie interpretieren Sie die Vorderwandableitungen?', [
    'Hyperakute T-Wellen anterior – früher LAD-Verschluss (OMI)',
    'Hyperkaliämie',
    'Normvariante bei Sportlerherz',
    'Linksventrikuläre Hypertrophie'],
    'Breite, voluminöse, symmetrische T-Wellen in V2–V4 im Verhältnis zum QRS, beginnende ST-Hebung, Hebung in aVL und reziproke Senkung in III. Hyperkaliämie-T sind schmal und spitz.', SMITH, 3),

img('KAR-23', T, '12-Kanal-EKG', 'dewinter', '52-Jährige mit typischem Brustschmerz. Welches Muster liegt vor?', [
    'De-Winter-Muster – proximaler LAD-Verschluss',
    'Hyperkaliämie',
    'Posteriorer Infarkt',
    'Digitaliseffekt'],
    'Aszendierende ST-Senkung am J-Punkt mit hohen, symmetrischen T-Wellen in V2–V6, leichte ST-Hebung in aVR. Nach Smith instabil (geht in ST-Hebung über) – wie STEMI behandeln.', SMITH_DW, 3),

img('KAR-24', T, '12-Kanal-EKG', 'wellens', 'Patient ist jetzt schmerzfrei; gestern Abend 30 min Brustschmerz. Bewertung?', [
    'Wellens-Muster A – kritische proximale LAD-Stenose',
    'Normalbefund',
    'Rechtsschenkelblock',
    'Perikarditis Stadium III'],
    'Biphasische T-Wellen (erst positiv, dann terminal negativ) in V2–V3 bei erhaltenen R-Zacken. Reperfundierter Verschluss mit hohem Re-Okklusionsrisiko: keine Belastungstests, zeitnahe Koronarangiografie. Pseudonormalisierung bei neuem Schmerz = Re-Okklusion.', SMITH_WEL, 3),

img('KAR-25', T, '12-Kanal-EKG', 'post_omi', '66-Jährige, akuter Brustschmerz seit 1 h. Bewertung?', [
    'Posteriorer OMI – V7–V9 ableiten, Katheterlabor',
    'Diffuse subendokardiale Ischämie (Hauptstamm)',
    'Digitalismulde',
    'Rechtsschenkelblock'],
    'ST-Senkung maximal in V2–V3 mit aufrechten T und prominenten R-Zacken = Spiegelbild der Hinterwand. Posteriore Ableitungen: schon > 0,5 mm Hebung ist beweisend.', SMITH_OMI, 3),

img('KAR-26', T, '12-Kanal-EKG', 'lbbb_sgarb', 'Brustschmerz, Linksschenkelblock ohne Vor-EKG. In V2 beträgt die ST-Hebung 5,5 mm bei 16 mm tiefer S-Zacke. Bewertung?', [
    'OMI nach Smith-modifizierten Sgarbossa-Kriterien (ST/S ≈ −0,34)',
    'Unkomplizierter Linksschenkelblock ohne Ischämiezeichen',
    'Hyperkaliämie',
    'Ventrikuläre Tachykardie'],
    'Übermäßige Diskordanz: ST-Hebung ÷ S-Tiefe ≤ −0,25 (hier 5,5 / −16 ≈ −0,34), mindestens 1 mm, in einer Ableitung genügt. Weitere Kriterien: konkordante Hebung ≥ 1 mm oder konkordante Senkung V1–V3 ≥ 1 mm.', SMITH_SG, 3),

img('KAR-27', T, '12-Kanal-EKG', 'lv_aneurysm', 'Atypischer Thoraxschmerz, Z. n. Vorderwandinfarkt vor 2 Jahren. Bewertung?', [
    'Persistierende ST-Hebung bei LV-Aneurysma (niedriges T/QRS-Verhältnis)',
    'Akuter Vorderwand-OMI',
    'Brugada-Muster',
    'Perikarditis'],
    'QS-Komplexe V1–V3 mit mäßiger ST-Hebung und kleinen T-Wellen. Smith-Regel: Summe T ÷ Summe QRS in V1–V4 < 0,22 spricht für Aneurysma; eine einzelne Ableitung mit T/QRS > 0,36 spricht für akuten STEMI. Vor-EKG vergleichen!', SMITH_LVA, 3),

img('KAR-28', T, '12-Kanal-EKG', 'wpw', '22-Jähriger mit anamnestischem Herzrasen; aktuelles Ruhe-EKG. Befund?', [
    'WPW-Muster (Präexzitation: kurze PQ-Zeit, Delta-Welle)',
    'Linksschenkelblock',
    'AV-Block I',
    'Hypokaliämie'],
    'Kurzes PQ, träger QRS-Beginn (Delta-Welle), verbreiterter QRS. Bei Vorhofflimmern mit Präexzitation keine AV-Knoten-Blocker – Kardioversion.', ERC_TACHY, 2),

img('KAR-29', T, '12-Kanal-EKG', 'brugada', '35-Jähriger, Synkope bei Fieber 39,5 °C. Befund in V1–V2?', [
    'Brugada-Muster Typ 1 (coved) – Hochrisiko nach Synkope',
    'Inkompletter Rechtsschenkelblock (Normvariante)',
    'Anteroseptaler OMI',
    'Frühe Repolarisation'],
    'Schulterförmige („coved“) ST-Hebung ≥ 2 mm mit negativem T in V1–V2. Fieber demaskiert; senken, monitoren, kardiologisch abklären (ICD-Indikation).', SMITH + '; ' + ERC_SPEC, 2),
]

T = 'NEU'
Q += [
mtf('NEU-01', T, 'Schlaganfall – Präklinik', 'Präklinisches Vorgehen bei Verdacht auf Schlaganfall:', [
    ('BE-FAST: das „B“ steht für Blutdruck.', 0, 'B = Balance (Gleichgewicht), E = Eyes (Sehstörung).'),
    ('Der Blutzucker wird bei jedem Verdacht gemessen – eine Hypoglykämie kann einen Schlaganfall imitieren.', 1, 'Klassischer Stroke-Mimic.'),
    ('Präklinisch wird der Blutdruck routinemäßig auf < 140 mmHg gesenkt.', 0, 'Nur bei Werten > 220/120 mmHg vorsichtig senken.'),
    ('Der Zeitpunkt „zuletzt gesund gesehen“ ist zentral und wird dokumentiert.', 1, 'Mit Uhrzeit und Quelle; Zeugen-Telefonnummer mitnehmen.'),
    ('Bei Verdacht auf großen Gefäßverschluss kann der direkte Transport in ein Thrombektomiezentrum sinnvoll sein.', 1, 'Regionale Konzepte (Mothership/Drip-and-Ship) beachten.'),
], DGN_STROKE, 1),

mtf('NEU-02', T, 'Schlaganfall – Rekanalisation', 'Rekanalisationstherapie beim ischämischen Schlaganfall:', [
    ('Die i.v.-Thrombolyse ist innerhalb von 4,5 h nach Symptombeginn möglich, darüber hinaus nur mit Bildgebungs-Selektion.', 1, 'Mismatch-Konzepte z. B. beim Wake-up-Stroke.'),
    ('Die Thrombektomie bei großem Gefäßverschluss ist in ausgewählten Fällen bis 24 h möglich.', 1, 'Bildgebungs-gestützte Selektion.'),
    ('Vor der Lyse muss der Blutdruck < 185/110 mmHg liegen.', 1, 'Während und nach der Lyse < 180/105 mmHg.'),
    ('Antikoagulierte Patienten sind grundsätzlich von jeder Rekanalisation ausgeschlossen.', 0, 'Die Thrombektomie bleibt möglich.'),
    ('Präklinisch ist ASS sinnvoll, da 85 % der Schlaganfälle ischämisch sind.', 0, 'Blutung ist präklinisch nicht ausgeschlossen; ASS gefährdet zudem die Lyseoption.'),
], DGN_STROKE, 2),

mtf('NEU-03', T, 'Status epilepticus', 'Status epilepticus beim Erwachsenen:', [
    ('Ein generalisierter tonisch-klonischer Anfall gilt ab 5 min Dauer als Status epilepticus.', 1, 'Operational t1 = 5 min.'),
    ('Midazolam 10 mg i.m. (> 40 kg) ist eine gleichwertige Option, wenn kein i.v.-Zugang besteht.', 1, 'Auch buccal/intranasal möglich.'),
    ('Diazepam rektal ist bei Erwachsenen die Erstlinientherapie der Wahl.', 0, 'Erstlinie: Lorazepam i.v., Midazolam i.m./i.n., Diazepam i.v.'),
    ('Nach zweifacher Benzodiazepin-Gabe ohne Erfolg folgt Levetiracetam 60 mg/kg (max. 4500 mg) oder Valproat 40 mg/kg i.v.', 1, 'Stufe 2; alternativ Phenytoin.'),
    ('Benzodiazepine werden erst nach 20 min Anfallsdauer gegeben, um eine Spontanremission abzuwarten.', 0, 'Je länger der Anfall, desto schlechter das Ansprechen – früh und ausreichend dosieren.'),
], DGN_SE, 2),

mtf('NEU-04', T, 'Schädel-Hirn-Trauma', 'Präklinische Versorgung des SHT:', [
    ('Hypoxie (SpO₂ < 90 %) und Hypotonie (RRsys < 90 mmHg) verschlechtern die Prognose und sind zu vermeiden.', 1, 'Sekundärschäden verhindern.'),
    ('Prophylaktische Hyperventilation (etCO₂ 25 mmHg) wird zur Hirndrucksenkung empfohlen.', 0, 'Normoventilation – Hyperventilation führt zu zerebraler Ischämie.'),
    ('Oberkörperhochlage 30° bei stabilem Kreislauf, Kopf in Neutralposition.', 1, 'Venösen Abfluss sichern; HWS-Immobilisation nicht zu eng.'),
    ('Anisokorie und Streckkrämpfe beim bewusstlosen SHT-Patienten sind Zeichen einer Einklemmung.', 1, 'Zügiger Transport in ein neurochirurgisches Zentrum.'),
    ('Ein GCS von 13 entspricht einem schweren SHT.', 0, 'GCS 13–15 leicht, 9–12 mittelschwer, ≤ 8 schwer.'),
], S3PT, 1),

mtf('NEU-05', T, 'Hypoglykämie', 'Hypoglykämie:', [
    ('Eine Hypoglykämie liegt bei BZ < 70 mg/dl (3,9 mmol/l) mit Symptomen vor.', 1, 'Schwere Hypoglykämie: Fremdhilfe nötig.'),
    ('Glukose i.v. titriert (z. B. 8–16 g, 0,2 g/kg) ist Therapie der Wahl bei Bewusstseinsstörung.', 1, 'NUN-Versorgungspfad Hypoglykämie.'),
    ('Glukagon 1 mg i.m. ist bei Alkoholikern mit leeren Glykogenspeichern besonders wirksam.', 0, 'Glukagon braucht Glykogen – bei Alkoholismus/Kachexie oft unwirksam.'),
    ('Nach Sulfonylharnstoff-Hypoglykämie ist ein Transportverzicht unproblematisch.', 0, 'Lange Wirkdauer – Rezidivgefahr; stationäre Überwachung.'),
    ('Nasales Glukagon (3 mg) ist eine Alternative ohne Gefäßzugang.', 1, 'Für Laien und Angehörige zugelassen.'),
], NUN + '; ' + HYPO_LL, 1),

mtf('NEU-06', T, 'Meningitis', 'Verdacht auf bakterielle Meningitis/Meningokokkensepsis:', [
    ('Die Antibiotikatherapie darf nicht durch Diagnostik verzögert werden.', 1, 'Zeit bis Antibiose ist prognosebestimmend.'),
    ('Petechien und Fieber bei Bewusstseinsstörung sind Warnzeichen einer Meningokokkensepsis.', 1, 'Glastest: Petechien verblassen nicht.'),
    ('Mund-Nasen-Schutz (FFP2) für das Team; enge Kontaktpersonen erhalten eine Chemoprophylaxe.', 1, 'Gesundheitsamt informieren.'),
    ('Eine Nackensteifigkeit ist immer vorhanden.', 0, 'Fehlt oft, besonders bei Säuglingen, Älteren und Bewusstlosen.'),
    ('Fehlendes Fieber schließt eine Meningitis aus.', 0, 'Kein Ausschlusskriterium.'),
], DGN_MEN, 2),

order('NEU-07', T, 'Status epilepticus', 'Stufentherapie des Status epilepticus beim Erwachsenen:', [
    'Eigenschutz, Verletzungsschutz, Zeit notieren, Blutzucker messen',
    'Benzodiazepin (z. B. Midazolam 10 mg i.m./i.n. oder Lorazepam i.v.)',
    'Benzodiazepin einmal wiederholen bei Persistenz',
    'Levetiracetam oder Valproat i.v. (Stufe 2)',
    'Refraktärer Status: Narkose (z. B. Propofol, Midazolam) und Intubation',
], 'Zeitkritisch: Benzodiazepine früh und ausreichend dosiert; nicht mehr als zwei Gaben.', DGN_SE, 1),

match('NEU-08', T, 'Glasgow Coma Scale', 'Ordne den Befund dem GCS-Wert zu.', [
    ['Augenöffnen auf Schmerzreiz', 'E2'],
    ['Gezielte Abwehr auf Schmerz', 'M5'],
    ['Abnorme Beugung (Beugesynergismen)', 'M3'],
    ['Unangemessene Worte', 'V3'],
    ['Orientiert', 'V5'],
], 'E 1–4, V 1–5, M 1–6; GCS 3–15.', ROSSAINT, 1),

match('NEU-09', T, 'Pupillen', 'Ordne Pupillenbefund und naheliegende Ursache zu.', [
    ['Beidseits stecknadelkopfgroß', 'Opioid-Intoxikation'],
    ['Einseitig weit und lichtstarr', 'Einklemmung (ipsilaterale Raumforderung)'],
    ['Beidseits weit', 'Anticholinergika, Sympathomimetika, Hypoxie'],
    ['Miosis mit Hypersalivation und Bradykardie', 'Organophosphat-Vergiftung'],
    ['Miosis mit Ptosis (Horner)', 'Karotisdissektion'],
], 'Pupillen immer im Kontext von Bewusstsein, Vitalparametern und Anamnese deuten.', ROSSAINT, 2),

cloze('NEU-10', T, 'GCS', 'Die GCS reicht von {0} bis {1} Punkten; ein schweres SHT liegt bei GCS ≤ {2} vor.', [
    ['3', ['0', '1', '5']],
    ['15', ['10', '12', '20']],
    ['8', ['10', '12', '5']],
], 'GCS ≤ 8: Atemwegssicherung erwägen („less than eight – intubate“).', S3PT, 1),

cloze('NEU-11', T, 'Status epilepticus', 'Ein Status liegt beim generalisierten tonisch-klonischen Anfall ab {0} min vor, beim fokalen Anfall mit Bewusstseinsstörung ab {1} min. Midazolam i.m. beim Erwachsenen (> 40 kg): {2}.', [
    ['5', ['2', '10', '30']],
    ['10', ['5', '30', '60']],
    ['10 mg', ['2 mg', '5 mg', '20 mg']],
], '13–40 kg: 5 mg i.m.', DGN_SE, 2),

cloze('NEU-12', T, 'Thrombolyse', 'Alteplase beim ischämischen Schlaganfall: {0} mg/kg (max. {1} mg), davon {2} % als Bolus, Rest über 60 min.', [
    ['0,9', ['0,25', '1,5', '0,1']],
    ['90', ['50', '100', '25']],
    ['10', ['50', '20', '5']],
], 'Tenecteplase: 0,25 mg/kg (max. 25 mg) als Einzelbolus.', DGN_STROKE, 2),

num('NEU-13', T, 'Alteplase', 'Gesamtdosis Alteplase (mg) für einen 80-kg-Patienten mit ischämischem Schlaganfall?', 'mg', 72, 0,
    '0,9 × 80 = 72 mg (7,2 mg Bolus, 64,8 mg über 60 min).', DGN_STROKE, 1),

num('NEU-14', T, 'Tenecteplase', 'Tenecteplase beim Schlaganfall: 0,25 mg/kg, max. 25 mg. Dosis (mg) für 70 kg?', 'mg', 17.5, 0.5,
    '0,25 × 70 = 17,5 mg als Einzelbolus.', DGN_STROKE, 2),

img('NEU-15', T, 'Kapnografie beim SHT', 'capno_hypervent', 'Intubierter SHT-Patient, manuelle Beutelbeatmung während des Transports. Bewertung?', [
    'Hyperventilation (etCO₂ ≈ 21 mmHg) – Frequenz senken, Ziel 35–40 mmHg',
    'Normoventilation',
    'Bronchospasmus',
    'Tubusdislokation'],
    'Hohe Frequenz, niedriger etCO₂: zerebrale Vasokonstriktion mit Ischämiegefahr. Möglichst Respirator mit Kapnografie-gesteuerter Normoventilation.', S3PT, 1),
]
