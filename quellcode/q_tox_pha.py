from qlib import *

Q = []
T = 'TOX'
Q += [
mtf('TOX-01', T, 'Toxidrome', 'Toxidrome:', [
    ('Anticholinerg: trockene, heiße, rote Haut, Mydriasis, Tachykardie, Harnverhalt, Delir.', 1, '„Blind as a bat, mad as a hatter, red as a beet, hot as a hare, dry as a bone.“'),
    ('Cholinerg: Miosis, Bradykardie, Bronchorrhö, Speichelfluss, Durchfall.', 1, 'SLUDGE/DUMBELS.'),
    ('Opioid-Toxidrom: Mydriasis, Tachypnoe, Hyperthermie.', 0, 'Miosis, Bradypnoe, Bewusstseinsminderung.'),
    ('Das sympathomimetische unterscheidet sich vom anticholinergen Toxidrom u. a. durch Schwitzen.', 1, 'Haut nass statt trocken.'),
    ('Das Serotoninsyndrom zeigt Rigor ohne Klonus und entwickelt sich langsam über Tage.', 0, 'Rascher Beginn mit Hyperreflexie und Klonus; das beschriebene Bild passt zum malignen neuroleptischen Syndrom.'),
], GIZ, 2),

mtf('TOX-02', T, 'Rauchgas & CO', 'CO- und Rauchgasvergiftung:', [
    ('Die Standard-Pulsoxymetrie erkennt CO-Hb zuverlässig.', 0, 'CO-Hb wird als O₂-Hb gemessen – SpO₂ falsch normal; SpCO-Messung nötig.'),
    ('Therapie: 100 % O₂ mit hohem Flow (Reservoirmaske), unabhängig von der SpO₂.', 1, 'Verkürzt die CO-Hb-Halbwertszeit deutlich.'),
    ('Bei Brandrauch mit Bewusstlosigkeit und hohem Laktat an Cyanid denken: Hydroxocobalamin 70 mg/kg (Erw. 5 g) i.v.', 1, 'Cyanid entsteht bei Verbrennung von Kunststoffen.'),
    ('CO ist schwerer als Luft und sammelt sich am Boden.', 0, 'Etwa gleich schwer wie Luft – verteilt sich im Raum, geruchlos.'),
    ('Bei Schwangeren mit relevanter CO-Exposition ist eine hyperbare Oxygenierung zu erwägen.', 1, 'Fetales Hb bindet CO stärker.'),
], GIZ + '; ' + ERC_SPEC, 2),

mtf('TOX-03', T, 'Opioide', 'Opioid-Intoxikation:', [
    ('Naloxon wird titriert; Ziel ist ausreichende Spontanatmung, nicht volle Wachheit.', 1, 'Vermeidet Entzug, Agitation, Lungenödem.'),
    ('Naloxon wirkt kürzer als viele Opioide – Rebound-Gefahr.', 1, 'Überwachung bzw. Transport.'),
    ('Bei Buprenorphin-Intoxikation ist Naloxon in Standarddosis immer voll wirksam.', 0, 'Hohe Rezeptoraffinität – oft höhere Dosen nötig.'),
    ('Beim apnoischen Patienten ist die erste Maßnahme die Beatmung, nicht das Antidot.', 1, 'Oxygenierung zuerst.'),
    ('Nach Naloxon kann ein wacher Patient regelhaft ohne Überwachung vor Ort bleiben.', 0, 'Rebound; Transportverweigerung sorgfältig dokumentieren.'),
], GIZ + '; ' + NUN, 1),

mtf('TOX-04', T, 'Hypothermie', 'Akzidentelle Hypothermie (ERC 2025):', [
    ('Unter 30 °C Kerntemperatur wird Adrenalin zurückgehalten und maximal dreimal defibrilliert.', 1, 'Medikamente akkumulieren, Myokard spricht schlecht an.'),
    ('Zwischen 30 und 35 °C wird Adrenalin in halbierten Intervallen (alle 1–2 min) gegeben.', 0, 'Intervalle verdoppeln (alle 6–10 min).'),
    ('Hypotherme Patienten im Kreislaufstillstand werden in ein Zentrum mit ECLS transportiert.', 1, 'Wiedererwärmung an der ECLS.'),
    ('Rettung möglichst horizontal und schonend (Bergungstod, „Afterdrop“).', 1, 'Grobe Bewegung kann Kammerflimmern auslösen.'),
    ('„Nobody is dead until warm and dead“ gilt ohne jede Ausnahme.', 0, 'Ausnahmen: tödliche Verletzungen, durchgefrorener Körper, verlegte Atemwege bei Lawine > 60 min, hohes Kalium.'),
], ERC_SPEC, 2),

mtf('TOX-05', T, 'Hitze & Ertrinken', 'Hitzschlag und Ertrinken:', [
    ('Hitzschlag: Körpertemperatur > 40 °C mit ZNS-Störung – sofort aggressiv kühlen (z. B. Kaltwasser-Immersion).', 1, 'Aktive Kühlung bis ca. 38 °C.'),
    ('Beim Ertrinken beginnt die Reanimation mit 5 Beatmungen.', 1, 'Hypoxischer Stillstand.'),
    ('Bei jedem Ertrinkungsunfall wird routinemäßig die HWS immobilisiert.', 0, 'Nur bei Hinweis auf Trauma (z. B. Kopfsprung).'),
    ('Antipyretika wie Paracetamol sind beim Hitzschlag wirksam.', 0, 'Kein zentraler Sollwert-Fehler – physikalisch kühlen.'),
    ('Nach Beinahe-Ertrinken mit Symptomen ist eine stationäre Überwachung sinnvoll (verzögertes Lungenödem).', 1, 'Husten, Dyspnoe, Rasselgeräusche ernst nehmen.'),
], ERC_SPEC, 1),

mtf('TOX-06', T, 'Elektrounfall', 'Strom- und Blitzunfälle:', [
    ('Bei Hochspannung (> 1000 V) Sicherheitsabstand wahren und Freischaltung durch Fachpersonal abwarten.', 1, 'Spannungstrichter beachten.'),
    ('Ein asymptomatischer Haushaltsstromunfall (230 V) mit unauffälligem EKG erfordert immer 24 h Monitoring.', 0, 'Bei unauffälligem Befund ist keine Routine-Überwachung nötig.'),
    ('Der Hautbefund korreliert verlässlich mit der inneren Schädigung.', 0, 'Strommarken können klein sein trotz schwerer Muskelschäden.'),
    ('Beim Blitzschlag mit mehreren Opfern werden zuerst scheinbar Leblose reanimiert („reverse triage“).', 1, 'Gute Prognose bei rascher CPR.'),
    ('Bei Starkstromunfällen sind Kompartmentsyndrom und Rhabdomyolyse möglich.', 1, 'Urin, CK, Kalium im Blick.'),
], ERC_SPEC, 2),

order('TOX-07', T, 'Vorgehen bei Vergiftung', 'Strukturiertes Vorgehen bei Vergiftungsverdacht:', [
    'Eigenschutz (Gase, Gefahrstoffe, Täter)',
    'Vitalfunktionen sichern (ABCDE)',
    'Toxidrom erkennen, Asservate sichern (Packungen, Reste)',
    'Giftinformationszentrum kontaktieren (z. B. GIZ-Nord Göttingen)',
    'Spezifische Therapie/Antidot',
    'Transport in geeignete Klinik, Asservate mitgeben',
], 'Symptomatische Therapie geht vor Antidot – Ausnahme: Antidot ist lebensrettend (z. B. Cyanid).', GIZ, 1),

match('TOX-08', T, 'Antidote I', 'Ordne dem Gift das Antidot zu.', [
    ['Paracetamol', 'N-Acetylcystein'],
    ['Cyanid', 'Hydroxocobalamin'],
    ['Benzodiazepine', 'Flumazenil'],
    ['Methämoglobinbildner', 'Methylenblau/Toloniumchlorid'],
    ['Organophosphate', 'Atropin (+ Obidoxim)'],
], 'Flumazenil bei Mischintoxikation/Benzodiazepin-Gewöhnung zurückhaltend (Krampfanfälle).', GIZ, 1),

match('TOX-09', T, 'Antidote II', 'Ordne dem Gift die spezifische Therapie zu.', [
    ['Betablocker', 'Glukagon, Hochdosis-Insulin'],
    ['Digitalis', 'Digitalis-Antitoxin (Fab-Fragmente)'],
    ['Heparin', 'Protamin'],
    ['Trizyklika mit QRS-Verbreiterung', 'Natriumbicarbonat'],
    ['Calciumantagonisten', 'Calcium'],
], 'Lipidemulsion bei Lokalanästhetika-Intoxikation ergänzend merken.', GIZ, 2),

match('TOX-10', T, 'Substanz → Leitsymptom', 'Ordne der Substanz das typische Leitsymptom zu.', [
    ['Ecstasy (MDMA)', 'Hyperthermie, Hyponatriämie'],
    ['GHB/GBL', 'abrupte tiefe Bewusstlosigkeit, rasches Erwachen'],
    ['Kokain', 'Thoraxschmerz, Hypertonie, Tachykardie'],
    ['Methanol', 'Sehstörung, metabolische Azidose'],
    ['Knollenblätterpilz', 'Gastroenteritis nach > 6 h, später Leberversagen'],
], 'Latenzzeiten (Pilze, Methanol) sind diagnostisch wertvoll.', GIZ, 2),

cloze('TOX-11', T, 'Organophosphate', 'Bei Organophosphat-Vergiftung wird Atropin initial mit {0} mg i.v. gegeben und alle 5 min {1}, bis {2}.', [
    ['2–5', ['0,5', '0,01', '20']],
    ['verdoppelt', ['halbiert', 'beibehalten', 'verzehnfacht']],
    ['die Bronchialsekretion sistiert', ['die Pupillen weit sind', 'die HF > 140/min ist', 'der Patient erwacht']],
], 'Zielkriterium ist die „trockene Lunge“ – nicht Pupillen oder Herzfrequenz. Gesamtdosen von mehreren hundert mg sind möglich.', GIZ + '; ' + FWDV500, 2),

cloze('TOX-12', T, 'Hypothermie-Stadien', 'Klassische Schweizer Stadien: HT I = {0}; HT II = {1}; HT III = {2}; HT IV = {3}.', [
    ['wach, Kältezittern', ['bewusstlos', 'keine Vitalzeichen', 'getrübt, kein Zittern']],
    ['getrübt, kein Zittern', ['wach, Kältezittern', 'keine Vitalzeichen', 'bewusstlos']],
    ['bewusstlos', ['wach, Kältezittern', 'getrübt, kein Zittern', 'keine Vitalzeichen']],
    ['keine Vitalzeichen', ['bewusstlos', 'wach, Kältezittern', 'getrübt, kein Zittern']],
], 'ERC 2025 nutzt das revidierte Schweizer System (Bewusstseinslage nach AVPU), da die Kerntemperatur präklinisch oft nicht messbar ist.', ERC_SPEC, 1),

num('TOX-13', T, 'Hydroxocobalamin', 'Kind, 20 kg, Rauchgasintoxikation mit Verdacht auf Cyanid. Hydroxocobalamin 70 mg/kg – Dosis in g?', 'g', 1.4, 0.05,
    '70 × 20 = 1400 mg = 1,4 g (Erwachsene 5 g).', GIZ, 2),

num('TOX-14', T, 'Naloxon titrieren', 'Naloxon 0,4 mg/1 ml wird auf 10 ml verdünnt. Wie viele ml entsprechen einem Titrationsschritt von 0,04 mg?', 'ml', 1, 0,
    '0,4 mg/10 ml = 0,04 mg/ml → 1 ml.', GIZ, 1),

img('TOX-15', T, 'Metabolisch', 'hyperk', 'Dialysepatient, letzte Dialyse vor 4 Tagen, Muskelschwäche, HF 64/min. Befund?', [
    'Hyperkaliämie (spitze T, breiter QRS, flache P)',
    'Hyperakute T-Wellen bei Vorderwand-OMI',
    'Hypokaliämie',
    'Hypokalzämie'],
    'Schmale, hohe, zeltförmige T-Wellen mit QRS-Verbreiterung und kaum sichtbaren P-Wellen. Calcium zur Membranstabilisierung, Insulin-Glukose, Salbutamol; Dialyse organisieren.', SMITH_K + '; ' + ERC_SPEC, 2),
]

T = 'PHA'
Q += [
mtf('PHA-01', T, 'Analgesie', 'Analgetika im Rettungsdienst:', [
    ('Esketamin 0,125–0,25 mg/kg i.v. (bzw. Ketamin-Razemat 0,25–0,5 mg/kg) zur Analgesie.', 1, 'Analgetische Dosis deutlich unter der Narkosedosis.'),
    ('Fentanyl wirkt ca. 100-fach stärker als Morphin.', 1, 'Schneller Wirkeintritt, kurze Wirkdauer.'),
    ('Metamizol kann bei schneller Injektion einen ausgeprägten Blutdruckabfall verursachen.', 1, 'Langsam bzw. als Kurzinfusion.'),
    ('Opioide sind beim akuten Abdomen kontraindiziert, weil sie die Diagnose verschleiern.', 0, 'Analgesie erschwert die Diagnostik nicht relevant.'),
    ('Paracetamol i.v. wird beim Erwachsenen > 50 kg mit 3 g als Einzeldosis gegeben.', 0, '1 g; max. 4 g/Tag.'),
], PHARM + '; ' + NUN, 1),

mtf('PHA-02', T, 'Katecholamine', 'Vasopressoren und Inotropika:', [
    ('Noradrenalin wirkt überwiegend α₁-adrenerg vasokonstriktorisch.', 1, 'Mit geringer β₁-Komponente.'),
    ('Adrenalin als „Push-Dose“ (z. B. 10–20 µg i.v.) ist eine Option bei Peri-Arrest-Hypotonie.', 1, 'Verdünnung sorgfältig, Spritze beschriften.'),
    ('Akrinor (Cafedrin/Theodrenalin) steigert vor allem das Herzzeitvolumen bei weitgehend unveränderter HF.', 1, 'Häufig bei Narkose-induzierter Hypotonie.'),
    ('Dobutamin ist Mittel der Wahl beim vasoplegischen septischen Schock.', 0, 'Vasopressor der Wahl ist Noradrenalin.'),
    ('Katecholamin-Perfusoren und Bolusgaben laufen über denselben Schenkel im Wechsel.', 0, 'Bolus spült Katecholamin mit – gefährliche Spitzen.'),
], PHARM + '; ' + MARINO, 2),

mtf('PHA-03', T, 'Narkosemedikamente', 'Medikamente der Notfallnarkose:', [
    ('Ketamin erhält Atemantrieb und Schutzreflexe weitgehend und wirkt sympathomimetisch.', 1, 'Daher günstig bei Schock und Bronchospasmus.'),
    ('Propofol verursacht häufig einen Blutdruckabfall, besonders bei Hypovolämie.', 1, 'Dosis reduzieren, Vasopressor bereit.'),
    ('Succinylcholin ist bei Hyperkaliämie, Verbrennung > 24 h und längerer Immobilisation kontraindiziert.', 1, 'Kaliumfreisetzung.'),
    ('Rocuronium wird für die RSI mit 0,3 mg/kg dosiert.', 0, '1,0–1,2 mg/kg.'),
    ('Etomidat ist beim septischen Schock wegen fehlender Nebennierensuppression unbedenklich.', 0, 'Etomidat hemmt die Kortisolsynthese.'),
], NARK + '; ' + PHARM, 2),

mtf('PHA-04', T, 'Antiarrhythmika', 'Antiarrhythmika und kardiale Medikamente:', [
    ('Amiodaron kann Hypotonie und Bradykardie verursachen – beim stabilen Patienten als Kurzinfusion.', 1, '300 mg über 10–20 min.'),
    ('Verapamil ist bei ventrikulärer Tachykardie unbedenklich.', 0, 'Kann zum Kreislaufkollaps führen.'),
    ('Magnesium 2 g i.v. ist bei Torsade de pointes indiziert.', 1, 'Unabhängig vom Serumspiegel.'),
    ('Theophyllin schwächt, Dipyridamol verstärkt die Adenosinwirkung.', 1, 'Dosis anpassen.'),
    ('Betablocker sind beim Kokain-induzierten ACS Mittel der ersten Wahl.', 0, 'Benzodiazepine und Nitrate zuerst.'),
], ERC_TACHY + '; ' + PHARM, 2),

mtf('PHA-05', T, 'Anaphylaxie', 'Medikamentöse Therapie der Anaphylaxie:', [
    ('Adrenalin i.m. 0,01 mg/kg (Erwachsene 0,3–0,5 mg) in den lateralen Oberschenkel.', 1, 'Erstes Medikament.'),
    ('Eine Wiederholung der i.m.-Gabe ist frühestens nach 30 min zulässig.', 0, 'Nach 5–10 min wiederholen.'),
    ('Antihistaminika und Glukokortikoide sind beim anaphylaktischen Schock gleichwertig zu Adrenalin.', 0, 'Nur Ergänzung.'),
    ('Adrenalin i.v. wird beim Erwachsenen in kleinen Boli (z. B. 10–50 µg) unter Monitoring titriert.', 1, 'Nur durch Erfahrene, Arrhythmiegefahr.'),
    ('Unter Betablocker sprechen Patienten schlechter auf Adrenalin an – Glukagon erwägen.', 1, 'Rezeptorunabhängig.'),
], ANA + '; ' + NUN, 1, memo='Anaphylaxie: Adrenalin i.m. – früh, Oberschenkel, nach 5–10 min wiederholen.'),

order('PHA-06', T, 'Medikamentensicherheit', 'Sichere Medikamentengabe im Notfall:', [
    'Medikament und Konzentration prüfen (Ampulle laut vorlesen)',
    'Aufziehen und Spritze sofort beschriften (Normetikett)',
    'Dosis im Vier-Augen-Prinzip bestätigen (Closed Loop)',
    'Applizieren und nachspülen',
    'Wirkung beobachten und dokumentieren',
], 'Unbeschriftete Spritzen sind eine der häufigsten Fehlerquellen.', CRM, 1),

match('PHA-07', T, 'Wirkmechanismen', 'Ordne dem Medikament den Wirkmechanismus zu.', [
    ['Urapidil', 'α₁-Blockade + zentraler 5-HT1A-Agonismus'],
    ['Butylscopolamin', 'Muskarinrezeptor-Antagonist (Spasmolyse)'],
    ['Ondansetron', '5-HT3-Antagonist'],
    ['Tranexamsäure', 'Antifibrinolytikum'],
    ['Esketamin', 'NMDA-Rezeptor-Antagonist'],
], 'Mechanismus erklärt Nebenwirkungen: Butylscopolamin → Tachykardie, Ondansetron → QT-Verlängerung.', PHARM, 2),

match('PHA-08', T, 'Dosierungen', 'Ordne dem Medikament die typische Erwachsenendosis im Notfall zu.', [
    ['Atropin (Bradykardie)', '0,5 mg i.v.'],
    ['Amiodaron (Reanimation)', '300 mg i.v.'],
    ['Tranexamsäure', '1 g i.v. über 10 min'],
    ['Midazolam (Status, i.m.)', '10 mg'],
    ['Adrenalin i.m. (Anaphylaxie)', '0,5 mg'],
], 'Regionale SOP/NUN-Pfade beachten.', NUN + '; ' + ERC_ALS, 1),

match('PHA-09', T, 'Antagonisten', 'Ordne jedem Antagonisten den Wirkstoff zu, den er aufhebt.', [
    ['Naloxon', 'Opioide'],
    ['Flumazenil', 'Benzodiazepine'],
    ['Sugammadex', 'Rocuronium/Vecuronium'],
    ['Protamin', 'Heparin'],
    ['Idarucizumab', 'Dabigatran'],
], 'Kürzere Wirkdauer vieler Antagonisten → Überwachung.', PHARM, 1),

cloze('PHA-10', T, 'Esketamin', 'Esketamin ist das {0}-Enantiomer von Ketamin und etwa {1} so potent; analgetische Dosis i.v. {2} mg/kg.', [
    ['S', ['R', 'D', 'L']],
    ['doppelt', ['halb', 'zehnmal', 'gleich']],
    ['0,125–0,25', ['1–2', '0,01', '2–3']],
], 'Narkoseeinleitung mit Esketamin ca. 0,5–1 mg/kg.', PHARM, 1),

cloze('PHA-11', T, 'Rocuronium', 'Rocuronium zur RSI: {0} mg/kg; sofortige Aufhebung mit Sugammadex {1} mg/kg.', [
    ['1,0–1,2', ['0,3', '0,1', '3']],
    ['16', ['2', '4', '0,5']],
], 'Sugammadex 2–4 mg/kg bei moderater/tiefer Blockade; 16 mg/kg zur sofortigen Reversierung.', PHARM, 2),

num('PHA-12', T, 'Midazolam', 'Midazolam 15 mg/3 ml. Sie benötigen 2 mg. Wie viele ml?', 'ml', 0.4, 0.02,
    '5 mg/ml → 2 mg = 0,4 ml. Tipp: auf 1 mg/ml verdünnen (15 ml).', PHARM, 1),

num('PHA-13', T, 'Fentanyl', 'Fentanyl 0,1 mg/2 ml. Dosis 1,5 µg/kg bei 70 kg – wie viele ml?', 'ml', 2.1, 0.1,
    '1,5 × 70 = 105 µg; 50 µg/ml → 2,1 ml.', PHARM, 2),

num('PHA-14', T, 'Adrenalin-Perfusor', 'Adrenalin 1 mg auf 50 ml. Ziel 5 µg/min. Laufrate in ml/h?', 'ml/h', 15, 0.5,
    '20 µg/ml; 5 µg/min = 300 µg/h → 15 ml/h.', PHARM, 2),

num('PHA-15', T, 'Ketamin', 'Ketamin 50 mg/ml. Analgesie mit 0,5 mg/kg bei 80 kg – wie viele ml?', 'ml', 0.8, 0.05,
    '0,5 × 80 = 40 mg → 0,8 ml. Für die Praxis verdünnen.', PHARM, 1),
]
