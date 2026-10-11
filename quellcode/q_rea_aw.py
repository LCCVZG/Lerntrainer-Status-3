from qlib import *

Q = []
T = 'REA'
Q += [
mtf('REA-01', T, 'ALS – Medikamente', 'Zur Medikamentengabe bei der Reanimation Erwachsener (ERC 2025) gilt:', [
    ('Bei nicht defibrillierbarem Rhythmus (Asystolie/PEA) wird 1 mg Adrenalin so früh wie möglich gegeben.', 1,
     'Sobald ein Zugang liegt: 1 mg Adrenalin, dann alle 3–5 min.'),
    ('Bei Kammerflimmern wird Adrenalin 1 mg bereits nach dem ersten erfolglosen Schock gegeben.', 0,
     'Bei VF/pVT erst nach dem 3. Schock, dann alle 3–5 min.'),
    ('Amiodaron 300 mg nach dem 3. Schock, weitere 150 mg nach dem 5. Schock – egal ob das VF refraktär oder rezidivierend ist.', 1,
     'So explizit in ERC 2025 formuliert.'),
    ('Lidocain 100 mg ist eine Alternative zu Amiodaron; nach dem 5. Schock können weitere 50 mg folgen.', 1,
     'Lidocain 100 mg, zusätzlich 50 mg nach dem 5. Schock.'),
    ('Natriumbicarbonat und Calcium werden nach 20 min Reanimation routinemäßig zum Azidoseausgleich gegeben.', 0,
     'Calcium, Bicarbonat und Steroide werden nicht routinemäßig gegeben – nur bei spezifischer Indikation (z. B. Hyperkaliämie, Ca-Antagonisten-, TCA-Intoxikation).'),
], ERC_ALS, 1, memo='Schockbar: Adrenalin & Amiodaron nach Schock 3 – Amiodaron 150 nach Schock 5.'),

mtf('REA-02', T, 'ALS – Defibrillation', 'Zur Defibrillation nach ERC 2025 treffen zu:', [
    ('Die Pause vor dem Schock soll unter 5 s liegen.', 1, 'Prä-Schock-Pause minimieren – Kompressionen während des Ladens fortführen.'),
    ('Feines Kammerflimmern wird nicht defibrilliert, sondern wie eine Asystolie behandelt.', 0,
     'Neu klargestellt: VF jeder Amplitude (auch feines VF) sofort defibrillieren.'),
    ('Refraktäres VF = VF nach drei aufeinanderfolgenden Schocks; dann Pad-Position prüfen und einen Vektorwechsel (anterior-posterior) erwägen.', 1,
     'Erst korrekte anterolaterale Lage sichern (apikales Pad unter der Achsel, mittlere Axillarlinie), dann a.-p.'),
    ('Die doppelt-sequenzielle Defibrillation ist bei refraktärem VF die empfohlene Standardmaßnahme.', 0,
     'DSD wird nicht routinemäßig empfohlen – nur im Rahmen von Studien.'),
    ('Bis zu drei Schocks in Folge sind beim beobachteten, monitorüberwachten Stillstand mit sofort verfügbarem Defibrillator angezeigt.', 1,
     'Klassisches Beispiel: Herzkatheterlabor, Intensivstation, Monitor-RTW.'),
], ERC_ALS, 2),

mtf('REA-03', T, 'ALS – Atemweg & Kapnografie', 'Atemwegsmanagement und Kapnografie unter Reanimation – was stimmt?', [
    ('Ein Intubationsversuch soll die Thoraxkompressionen nicht länger als 5 s unterbrechen.', 1, 'Nur Anwender mit > 95 % Erfolg in zwei Versuchen; Videolaryngoskop, wenn sofort verfügbar.'),
    ('Die ERC bevorzugt den Larynxtubus gegenüber der i-gel als supraglottische Atemwegshilfe.', 0, 'ERC 2025: i-gel wird gegenüber dem Larynxtubus bevorzugt.'),
    ('Nach Sicherung mit Endotrachealtubus: Beatmungsfrequenz 10/min bei kontinuierlichen Kompressionen.', 1, 'Bei undichter SGA ggf. zurück zu 30:2.'),
    ('Eine anhaltende Kapnografiekurve schließt eine ösophageale Tubuslage aus.', 1, 'Kurvenform über mehrere Atemzüge = Standard der Lagekontrolle.'),
    ('Ein niedriger etCO₂ nach 20 min ist allein ein ausreichender Grund, die Reanimation zu beenden.', 0, 'Nicht allein aufgrund niedriger etCO₂-Werte abbrechen.'),
], ERC_ALS, 2),

mtf('REA-04', T, 'ALS – Zugang & Sonderverfahren', 'Weitere ALS-Empfehlungen (ERC 2025):', [
    ('Beim Erwachsenen primär i.v.; i.o. erwägen, wenn zwei i.v.-Versuche scheitern.', 1, 'Neu in 2025: i.v. vor i.o.'),
    ('Mechanische Reanimationshilfen sollen bei jedem präklinischen Stillstand eingesetzt werden.', 0,
     'Nur wenn hochwertige manuelle CPR nicht möglich ist oder Helfer gefährdet (z. B. Transport, Treppenhaus).'),
    ('Bei vermuteter Lungenembolie: Thrombolyse unter CPR erwägen und ggf. 60–90 min weiter reanimieren.', 1, 'Fibrinolytikum braucht Zeit – nicht zu früh abbrechen.'),
    ('Der präkordiale Faustschlag ist in den Leitlinien 2025 nicht mehr enthalten.', 1, 'Explizit gestrichen.'),
    ('eCPR ist für jeden Patienten mit präklinischem Stillstand ab Minute 5 Standard.', 0,
     'eCPR kann für ausgewählte Patienten erwogen werden, wenn konventionelle CPR versagt und das System sie zeitgerecht anbietet.'),
], ERC_ALS, 2),

mtf('REA-05', T, 'Postreanimationsbehandlung', 'Nach ROSC (ERC/ESICM 2025) gilt:', [
    ('Ziel-SpO₂ 94–98 %, Hyperoxämie vermeiden.', 1, 'Sobald SpO₂ zuverlässig messbar ist, FiO₂ herunter titrieren.'),
    ('Eine ST-Hebung im Post-ROSC-EKG rechtfertigt erst nach 24 h Stabilisierung eine Koronarangiografie.', 0, 'ST-Hebung → umgehende Herzkatheteruntersuchung.'),
    ('MAP > 65 mmHg anstreben.', 1, 'Hypotonie vermeiden; Urinausscheidung und Laktat als Steuergrößen.'),
    ('Fieber (> 37,7 °C) wird bei komatösen Patienten für mindestens 72 h aktiv verhindert.', 1, 'Temperaturkontrolle statt starrer Hypothermie.'),
    ('Präklinisch soll mit 30 ml/kg 4 °C kalter Infusion gekühlt werden.', 0, 'Präklinische Kühlung mit kalten Infusionen wird nicht empfohlen (Lungenödem, Re-Arrest).'),
], ERC_POST, 2, memo='Post-ROSC: 94–98 % · CO₂ normal · MAP > 65 · kein Fieber 72 h · STE → Katheter.'),

mtf('REA-06', T, 'Reversible Ursachen', 'Reversible Ursachen und besondere Situationen:', [
    ('Zu den „4 H“ zählen Hypoxie, Hypovolämie, Hypothermie und hypertensive Krise.', 0,
     'Die 4 H: Hypoxie, Hypovolämie, Hypo-/Hyperkaliämie bzw. metabolisch, Hypo-/Hyperthermie.'),
    ('„HITS“ = Herzbeuteltamponade, Intoxikation, Thromboembolie, Spannungspneumothorax.', 1, 'Englisch: 4 Ts – Tamponade, Toxins, Thrombosis, Tension pneumothorax.'),
    ('Im traumatischen Kreislaufstillstand haben Thoraxkompressionen Vorrang vor Blutstillung und Thoraxentlastung.', 0,
     'Beim traumatischen Stillstand werden reversible Ursachen (Blutung, Hypoxie, Spannungspneu, Tamponade) zeitgleich bzw. vorrangig behandelt.'),
    ('Bei Schwangeren ab ca. 20. SSW wird der Uterus manuell nach links verlagert.', 1, 'Aortokavale Kompression aufheben.'),
    ('Bei erfolgloser Reanimation einer Schwangeren (≥ 20. SSW) ist eine Notfall-Hysterotomie innerhalb von ca. 5 min anzustreben.', 1, 'Verbessert die Chancen für Mutter und Kind – praktisch meist erst in der Klinik möglich.'),
], ERC_SPEC, 2, memo='4 H + HITS'),

order('REA-07', T, 'ALS – Ablauf', 'Bringe die Schritte bei einem nicht beobachteten Kreislaufstillstand mit Kammerflimmern (Erwachsener, ALS-Team) in die richtige Reihenfolge.', [
    'Bewusstsein und Atmung prüfen (max. 10 s)',
    'Hilfe/Team alarmieren, Defibrillator holen lassen',
    'Thoraxkompressionen 30:2 beginnen',
    'Pads aufkleben, Rhythmusanalyse mit minimaler Pause',
    'Schock abgeben (Kompressionen bis zum Laden fortführen)',
    'Sofort 2 min CPR, dann erneute Rhythmusanalyse',
    'Nach dem 3. Schock: Adrenalin 1 mg und Amiodaron 300 mg',
], 'Kompressionen und Defibrillation stehen am Anfang; Medikamente folgen erst nach dem 3. Schock.', ERC_ALS, 1),

order('REA-08', T, 'BLS durch Laien (2025)', 'Reihenfolge für Ersthelfer nach ERC/GRC 2025:', [
    'Reaktion prüfen (ansprechen, anfassen)',
    'Notruf 112 – Telefon auf Lautsprecher, AED holen lassen',
    'Atemwege freimachen und Atmung prüfen (mit Leitstelle)',
    'Thoraxkompressionen 100–120/min, 5–6 cm tief',
    'AED einschalten, Pads kleben, Anweisungen folgen',
], 'Neu 2025: Laien prüfen die Atmung erst nach dem Notruf und mit Unterstützung der Leitstelle – damit die Kompressionen früher beginnen.', ERC_BLS, 1),

match('REA-09', T, 'Reversible Ursachen – Therapie', 'Ordne jeder reversiblen Ursache die spezifische Maßnahme zu.', [
    ['Spannungspneumothorax', 'Thoraxentlastung (Dekompression)'],
    ['Perikardtamponade', 'Perikardpunktion/Entlastung'],
    ['Hyperkaliämie', 'Calcium, Insulin-Glukose, ggf. Bicarbonat'],
    ['Lungenembolie', 'Thrombolyse'],
    ['Hämorrhagische Hypovolämie', 'Blutstillung, Volumen/Blutprodukte'],
], 'Die Suche nach reversiblen Ursachen läuft parallel zur CPR – Ultraschall nur durch Geübte und ohne zusätzliche Pausen.', ERC_ALS, 1),

cloze('REA-10', T, 'Thoraxkompressionen', 'Thoraxkompressionen beim Erwachsenen: Frequenz {0}/min, Drucktiefe {1} cm, Verhältnis {2} ohne gesicherten Atemweg; Druckpunkt {3}.', [
    ['100–120', ['80–100', '120–140', '60–80']],
    ['5–6', ['3–4', '4–5', '6–8']],
    ['30:2', ['15:2', '5:1', '3:1']],
    ['untere Sternumhälfte', ['Processus xiphoideus', 'obere Sternumhälfte', 'linke Medioklavikularlinie']],
], 'Vollständige Entlastung nach jeder Kompression, Unterbrechungen minimieren.', ERC_BLS, 1),

cloze('REA-11', T, 'Bradykardie', 'Instabile Bradykardie: Atropin {0} i.v., wiederholbar alle 3–5 min bis maximal {1}. Zweitlinie: Adrenalin {2} µg/min oder transkutanes Pacing.', [
    ['0,5 mg', ['1 mg', '0,1 mg', '2 mg']],
    ['3 mg', ['1 mg', '6 mg', '10 mg']],
    ['2–10', ['20–50', '0,1–0,5', '50–100']],
], 'ERC 2025: Atropin 500 µg bis 3 mg; Isoprenalin 5 µg/min oder Adrenalin 2–10 µg/min; Atropin meiden bei Herztransplantation und hochgradigem AV-Block mit breitem QRS.', ERC_TACHY, 2),

cloze('REA-12', T, 'Kardioversion', 'Synchronisierte Kardioversion: Vorhofflimmern initial mit {0}, Vorhofflattern/PSVT initial {1}, VT mit Puls initial {2}.', [
    ['maximaler Energie', ['50 J', '70–120 J', '4 J/kg']],
    ['70–120 J', ['200 J', 'maximaler Energie', '20 J']],
    ['120–150 J', ['50 J', '360 J', '70 J']],
], 'Neu in ERC 2025: Vorhofflimmern direkt mit maximaler Energie kardiovertieren.', ERC_TACHY, 2),

num('REA-13', T, 'Amiodaron', 'Refraktäres Kammerflimmern beim Erwachsenen: Welche kumulative Amiodaron-Dosis (mg) hat der Patient nach dem 5. Schock erhalten?', 'mg', 450, 0,
    '300 mg nach dem 3. Schock + 150 mg nach dem 5. Schock = 450 mg.', ERC_ALS, 1),

num('REA-14', T, 'Physiologisch gesteuerte CPR', 'Welcher etCO₂-Wert (mmHg) wird in ERC 2025 als pragmatisches Ziel einer physiologisch gesteuerten CPR genannt?', 'mmHg', 25, 2,
    'Ziele: etCO₂ ≈ 25 mmHg (3,3 kPa) und – bei liegender Arterie – diastolischer Druck ≈ 30 mmHg.', ERC_ALS, 3),

img('REA-15', T, 'Rhythmus', 'vf', 'Ein Mann kollabiert vor Ihren Augen, keine normale Atmung. Der Monitor zeigt:', [
    'Kammerflimmern', 'Torsade de pointes', 'Asystolie mit Bewegungsartefakt', 'Vorhofflimmern mit schneller Überleitung'],
    'Chaotische, unregelmäßige Wellen ohne abgrenzbare QRS-Komplexe = VF. Sofort defibrillieren – jede Amplitude.', ERC_ALS, 1),

img('REA-16', T, 'Rhythmus', 'pasys', 'Bewusstlose, pulslose Patientin. Was zeigt der Monitor – und was folgt daraus?', [
    'P-Wellen-Asystolie – nicht schockbar; CPR, Adrenalin, Schrittmacher erwägen',
    'Sinusbradykardie – Atropin',
    'AV-Block I – keine Therapie',
    'Feines Kammerflimmern – defibrillieren'],
    'Vorhofaktion ohne Kammerantwort: ventrikuläre Asystolie. Nicht defibrillierbar. Hier kann Pacing wirksam sein – anders als bei vollständiger Asystolie.', ERC_ALS, 2),

img('REA-17', T, 'Rhythmus', 'tdp', 'Patientin unter Methadon und Antibiotikum, Synkopen. Der Monitor zeigt:', [
    'Torsade de pointes', 'Kammerflattern', 'Präexzitiertes Vorhofflimmern', 'Monomorphe VT'],
    'Spindelförmig an- und abschwellende polymorphe VT bei Long-QT = TdP. Magnesium 2 g i.v.; pulslos → defibrillieren; QT-verlängernde Medikamente absetzen, Kalium ausgleichen.', ERC_ALS, 2),

img('REA-18', T, 'Kapnografie unter CPR', 'capno_rosc', 'Laufende Reanimation, Patient intubiert. Die Kapnografie ändert sich plötzlich wie abgebildet. Bewertung?', [
    'Möglicher ROSC – bei der nächsten Rhythmusanalyse Puls prüfen; Kompressionen nicht allein deshalb unterbrechen',
    'Tubusdislokation in den Ösophagus',
    'Hyperventilation durch den Helfer',
    'Messfehler durch Feuchtigkeit in der Küvette'],
    'Ein abrupter, anhaltender etCO₂-Anstieg spricht für ROSC. ERC 2025: Die Kompression nicht allein wegen eines etCO₂-Anstiegs unterbrechen.', ERC_ALS, 1),
]

T = 'AW'
Q += [
mtf('AW-01', T, 'Notfallnarkose – Indikationen', 'Indikationen zur prähospitalen Notfallnarkose/Intubation beim Trauma (S3 Polytrauma):', [
    ('Apnoe oder Schnappatmung (AF < 6/min).', 1, 'Empfehlungsgrad A.'),
    ('SpO₂ < 90 % trotz O₂-Gabe nach Ausschluss eines Spannungspneumothorax.', 1, 'Empfehlungsgrad B.'),
    ('GCS 10 nach SHT ist für sich allein eine zwingende Intubationsindikation.', 0, 'Schwelle ist GCS < 9.'),
    ('Etomidat ist das empfohlene Hypnotikum, Ketamin soll vermieden werden.', 0, 'Umgekehrt: Etomidat meiden, Ketamin ist meist eine gute Alternative.'),
    ('Schweres Thoraxtrauma mit AF > 29/min.', 1, 'Ebenfalls Empfehlungsgrad B.'),
], S3PT, 2),

mtf('AW-02', T, 'Atemwegsmanagement', 'Prähospitales Atemwegsmanagement – was trifft zu?', [
    ('Die Auskultation ersetzt die Kapnografie als sichere Lagekontrolle.', 0, 'Kapnografie ist obligat; Auskultation allein ist unzuverlässig.'),
    ('Nach zwei erfolglosen Intubationsversuchen soll auf eine supraglottische Atemwegshilfe gewechselt werden.', 1, 'Begrenzung der Versuche schützt vor Hypoxie und Schwellung.'),
    ('Die Präoxygenierung kann bei kritischen Patienten zugunsten der Zeit entfallen.', 0, 'Präoxygenierung (Grad A) verlängert die sichere Apnoezeit.'),
    ('Ein Videolaryngoskop sollte bei Verfügbarkeit primär genutzt werden.', 1, 'Höhere Erstversuchs-Erfolgsrate, v. a. bei weniger Geübten.'),
    ('Bei CICO-Situation (cannot intubate, cannot oxygenate) ist die Koniotomie indiziert.', 1, 'Nicht zu lange zögern – Skalpell-Bougie-Tubus.'),
], AWM, 2),

mtf('AW-03', T, 'Asthma', 'Akuter Asthmaanfall beim Erwachsenen:', [
    ('„Silent chest“, Zyanose und Erschöpfung sind Zeichen eines lebensbedrohlichen Anfalls.', 1, 'Leises Atemgeräusch = kaum Luftfluss.'),
    ('Kurzwirksames β₂-Mimetikum (z. B. Salbutamol 2,5–5 mg vernebelt) ist Mittel der ersten Wahl, ggf. plus Ipratropiumbromid.', 1, 'Wiederholt bzw. kontinuierlich vernebeln.'),
    ('Systemische Glukokortikoide wirken nach wenigen Minuten und ersetzen die Bronchodilatation.', 0, 'Wirkeintritt erst nach Stunden – trotzdem früh geben (z. B. 50 mg Prednisolon).'),
    ('Magnesiumsulfat 2 g i.v. über 20 min kann beim schweren Anfall gegeben werden.', 1, 'Zusatztherapie bei unzureichendem Ansprechen.'),
    ('Benzodiazepine gegen Angst und Tachypnoe sind Standard.', 0, 'Sedierung kann eine respiratorische Erschöpfung demaskieren – nur unter Intubationsbereitschaft.'),
], NVL_ASTHMA, 2),

mtf('AW-04', T, 'Sauerstoff & COPD', 'Sauerstofftherapie und AECOPD:', [
    ('Bei Hyperkapnierisiko (z. B. COPD) Ziel-SpO₂ 88–92 %.', 1, 'Vermeidet hyperoxische Hyperkapnie.'),
    ('Sauerstoff wird COPD-Patienten grundsätzlich vorenthalten, um den Atemantrieb zu erhalten.', 0, 'Hypoxämie ist gefährlicher – titrieren statt vorenthalten.'),
    ('NIV ist bei hyperkapnischer AECOPD mit respiratorischer Azidose Therapie der Wahl, sofern keine Kontraindikationen bestehen.', 1, 'Reduziert Intubationsrate und Letalität.'),
    ('Die deutsche S3-Leitlinie empfiehlt für die meisten akut Kranken einen SpO₂-Zielbereich von 92–96 %.', 1, 'Abweichend von 94–98 % in manchen internationalen Empfehlungen.'),
    ('Beim ACS wird O₂ routinemäßig auch bei SpO₂ 97 % gegeben.', 0, 'O₂ nur bei SpO₂ < 90 % (ESC).'),
], O2LL + '; ' + NIV, 2),

mtf('AW-05', T, 'Kardiales Lungenödem', 'Präklinische Therapie des kardialen Lungenödems:', [
    ('Oberkörperhochlagerung mit herabhängenden Beinen senkt die Vorlast.', 1, 'Einfach, sofort, wirksam.'),
    ('CPAP/NIV verbessert die Oxygenierung und senkt Vor- und Nachlast des linken Ventrikels.', 1, 'Frühzeitig einsetzen, wenn Patient kooperativ und Schutzreflexe vorhanden.'),
    ('Glyceroltrinitrat ist auch bei RRsys 85 mmHg indiziert, da es primär diuretisch wirkt.', 0, 'Nitrate wirken venodilatierend; bei Hypotonie kontraindiziert.'),
    ('Furosemid 40 mg langsam i.v. ist Teil des NUN-Versorgungspfads.', 1, 'Nach Nitrat und NIV; Wirkung zunächst venodilatierend.'),
    ('Großzügige Volumengabe verbessert die Nierenperfusion und ist Basistherapie.', 0, 'Volumen verschlechtert die Stauung.'),
], NUN + '; ' + NIV, 1),

mtf('AW-06', T, 'Fremdkörperaspiration', 'Fremdkörperverlegung der Atemwege beim Erwachsenen:', [
    ('Bei effektivem Husten zum Weiterhusten auffordern.', 1, 'Nicht eingreifen, beobachten.'),
    ('Bei ineffektivem Husten (wach): bis zu 5 Rückenschläge, dann bis zu 5 Oberbauchkompressionen, im Wechsel.', 1, 'ERC-Sequenz.'),
    ('Wird der Patient bewusstlos, wird mit CPR begonnen.', 1, 'Kompressionen erzeugen höhere Atemwegsdrücke als Oberbauchkompressionen.'),
    ('Blindes Auswischen des Mundes mit dem Finger ist Standard.', 0, 'Gefahr, den Fremdkörper tiefer zu schieben; nur sichtbare Fremdkörper entfernen.'),
    ('Nach erfolgreichen Oberbauchkompressionen ist keine ärztliche Abklärung nötig.', 0, 'Abklärung wegen möglicher innerer Verletzungen.'),
], ERC_BLS, 1),

order('AW-07', T, 'RSI', 'Bringe die Schritte der prähospitalen Notfallnarkose (RSI) in die richtige Reihenfolge.', [
    'Team-Briefing mit Checkliste, Material und Plan B/C',
    'Präoxygenierung (≥ 3 min, dichte Maske, ggf. NIV)',
    'Hypnotikum und Analgetikum zügig injizieren',
    'Muskelrelaxans (Rocuronium oder Succinylcholin) unmittelbar nachspülen',
    'Laryngoskopie (bevorzugt Video) und Intubation',
    'Lagekontrolle mit Kapnografie (Kurve!)',
    'Tubus fixieren, Beatmung einstellen, Narkose aufrechterhalten',
], 'Checkliste und Präoxygenierung zuerst, Kapnografie vor allem anderen nach der Intubation.', NARK, 2),

order('AW-08', T, 'Schwieriger Atemweg', 'Eskalation bei unerwartet schwierigem Atemweg (Erwachsener):', [
    'Plan A: optimierte Intubation (Lagerung, Video, Bougie) – max. 2 Versuche',
    'Plan B: supraglottische Atemwegshilfe (z. B. i-gel)',
    'Plan C: Maskenbeatmung mit 2-Helfer-Technik und Guedel/Wendl',
    'Plan D: Koniotomie (Skalpell–Bougie–Tubus)',
], 'Entspricht dem DAS-Algorithmus: Oxygenierung hat immer Vorrang vor der Intubation.', AWM, 2),

match('AW-09', T, 'Beatmung nach Intubation', 'Ordne den Beatmungsparametern einen sinnvollen Startwert zu.', [
    ['Tidalvolumen', '6–8 ml/kg Idealgewicht'],
    ['PEEP', '≥ 5 cmH₂O'],
    ['Plateaudruck', '< 30 cmH₂O'],
    ['etCO₂ (Normoventilation)', '35–40 mmHg'],
    ['FiO₂ unmittelbar nach Intubation', '1,0 – dann nach SpO₂ titrieren'],
], 'Lungenprotektiv beatmen, Hyperventilation vermeiden.', MARINO + '; ' + NARK, 2),

match('AW-10', T, 'Auskultation', 'Ordne Krankheitsbild und typischen Befund zu.', [
    ['Asthmaanfall', 'Giemen, verlängertes Exspirium'],
    ['Kardiales Lungenödem', 'feuchte Rasselgeräusche basal'],
    ['Pseudokrupp', 'inspiratorischer Stridor, bellender Husten'],
    ['Spannungspneumothorax', 'einseitig aufgehobenes Atemgeräusch, hypersonorer Klopfschall'],
    ['Pleuraerguss', 'gedämpfter Klopfschall, abgeschwächtes Atemgeräusch'],
], 'Auskultation und Perkussion bleiben schnelle Basisinstrumente.', ROSSAINT, 1),

cloze('AW-11', T, 'CPAP', 'CPAP beim kardialen Lungenödem wird meist mit {0} cmH₂O begonnen. Kontraindikationen sind u. a. {1} und {2}.', [
    ['5–10', ['15–20', '0–2', '25–30']],
    ['fehlende Schutzreflexe', ['Tachykardie', 'Hypertonie', 'Angst']],
    ['Erbrechen/Aspirationsgefahr', ['Hypoxämie', 'Tachypnoe', 'Orthopnoe']],
], 'Weitere Kontraindikationen: Spannungspneumothorax, fehlende Kooperation, Gesichtstrauma, Schock.', NIV, 2),

cloze('AW-12', T, 'Koniotomie', 'Bei der Skalpell-Koniotomie wird die Membrana {0} zwischen Schild- und {1} aufgesucht; über einen {2} wird ein Tubus {3} eingeführt.', [
    ['cricothyroidea', ['thyrohyoidea', 'atlantooccipitalis', 'tectoria']],
    ['Ringknorpel', ['Stellknorpel', 'Zungenbein', 'Kehldeckel']],
    ['Bougie', ['Trokar', 'Magensonde', 'Führungsdraht ohne Inzision']],
    ['ID 6,0 (gecufft)', ['ID 8,5', 'ID 3,0', 'Larynxtubus Gr. 4']],
], 'Skalpell (Nr. 10), horizontaler Schnitt, 90° drehen, Bougie, Tubus 6,0 – Lagekontrolle mit Kapnografie.', AWM, 3),

num('AW-13', T, 'Lungenprotektive Beatmung', 'Mann, 180 cm. Idealgewicht nach ARDSNet = 50 + 0,91 × (Größe − 152,4). Welches Tidalvolumen (ml) entspricht 6 ml/kg?', 'ml', 450, 15,
    'IBW = 50 + 0,91 × 27,6 ≈ 75 kg → 6 × 75 ≈ 450 ml. Das tatsächliche Gewicht spielt keine Rolle.', MARINO, 2),

num('AW-14', T, 'Sauerstoffvorrat', 'Eine 2-l-Sauerstoffflasche zeigt 200 bar. Wie viele Minuten reicht sie bei 15 l/min (ohne Restdruck-Reserve)?', 'min', 27, 1,
    'Vorrat = 2 l × 200 bar = 400 l; 400 / 15 ≈ 27 min. In der Praxis Reserve einplanen!', ROSSAINT, 1),

num('AW-15', T, 'Präoxygenierung', 'Wie viele Minuten soll vor der RSI mindestens mit dicht sitzender Maske und hoher FiO₂ präoxygeniert werden?', 'min', 3, 0,
    'Mindestens 3 min (alternativ 8 tiefe Atemzüge); bei kritischer Hypoxämie NIV-gestützt.', NARK, 1),

img('AW-16', T, 'Kapnografie', 'capno_eso', 'Kapnografie unmittelbar nach Intubation eines Patienten mit erhaltenem Kreislauf. Bewertung?', [
    'Ösophageale Fehlintubation – Tubus entfernen, oxygenieren, neu intubieren',
    'Bronchospasmus',
    'Normale Kurve nach Intubation',
    'Leckage am Cuff'],
    'Wenige kleiner werdende Kurven (CO₂ aus dem durch Maskenbeatmung geblähten Magen), dann Nulllinie = Ösophagus. „No trace = wrong place.“', AWM, 1),

img('AW-17', T, 'Kapnografie', 'capno_shark', 'Beatmeter Patient, steigende Spitzendrücke. Die Kapnografie zeigt:', [
    'Obstruktion der unteren Atemwege (Bronchospasmus) – „Haifischflosse“',
    'Hypoventilation',
    'Rückatmung',
    'Ösophageale Tubuslage'],
    'Verzögerter, schräger Anstieg ohne Plateau = behinderte Exspiration. Bronchodilatation, lange Exspiration, Auto-PEEP vermeiden.', AWM, 1),

img('AW-18', T, 'Kapnografie', 'capno_cleft', 'Intubierter, relaxierter Patient auf dem Transport. Die Plateauphase zeigt eine Kerbe. Bedeutung?', [
    'Spontane Atemanstrengung – Narkose/Relaxierung lässt nach („Curare-Kerbe“)',
    'Cuff-Leckage',
    'Herzrhythmusstörung',
    'Ösophageale Lage'],
    'Eigenatmung gegen das Gerät: Narkosetiefe prüfen, ggf. nachdosieren – Gefahr von Pressen und Tubusdislokation.', AWM, 2),
]
