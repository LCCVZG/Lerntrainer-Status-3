"""Hardened versions (EDAIC-Paper-B-Niveau). Replace questions with the same ID."""
from qlib import *

HARD = [
mtf('REA-01', 'REA', 'ALS – Medikamente', 'Medikamentöse Therapie während der Reanimation Erwachsener (ERC 2025):', [
    ('Liegt bereits eine invasive Blutdruckmessung, kann Adrenalin initial in Boli von 50–100 µg titriert werden statt als 1-mg-Bolus.', 1,
     'Neu in ERC 2025 für den „highly monitored arrest“; bleibt nach insgesamt 1 mg die Wirkung aus, an Paravasat denken.'),
    ('Bei initial schockbarem Rhythmus wird die erste Adrenalin-Gabe bereits nach dem 2. Schock empfohlen, sofern ein i.o.-Zugang liegt.', 0,
     'Unabhängig vom Zugangsweg: erst nach dem 3. Schock.'),
    ('Amiodaron 150 mg nach dem 5. Schock wird auch gegeben, wenn zwischenzeitlich ROSC bestand und das VF erneut auftritt.', 1,
     'ERC 2025: „refraktär oder rezidivierend“ – beides zählt.'),
    ('Lidocain ist nur bei Kontraindikation gegen Amiodaron zulässig und wird mit 1,5 mg/kg dosiert.', 0,
     'Gleichwertige Alternative: 100 mg, nach dem 5. Schock weitere 50 mg.'),
    ('Bei Stillstand durch Hypovolämie sind isotone Kristalloide indiziert; ein routinemäßiger Volumenbolus bei normovolämer Ursache wird nicht empfohlen.', 1,
     'Volumen nur bei vermuteter Hypovolämie.'),
], ERC_ALS, 3),

mtf('REA-03', 'REA', 'ALS – Atemweg & Beatmung', 'Atemweg und Beatmung unter Reanimation (ERC 2025):', [
    ('Intubieren sollen unter CPR nur Anwender mit > 95 % Erfolgsrate innerhalb von zwei Versuchen.', 1, 'Sonst supraglottisch (bevorzugt i-gel).'),
    ('Mit Respirator unter CPR: volumenkontrolliert 6–8 ml/kg Idealgewicht, AF 10/min, PEEP 0–5 cmH₂O, Trigger aus.', 1, 'Erstmals konkrete Respirator-Einstellungen in ERC 2025.'),
    ('Die Spitzendruck-Alarmgrenze wird auf 30 cmH₂O gesetzt, damit Kompressionen keine Barotraumen verursachen.', 0,
     'Empfohlen sind 60–70 cmH₂O – sonst bricht der Respirator jeden Hub ab und das Volumen wird nicht appliziert.'),
    ('Leckt eine supraglottische Atemwegshilfe bei kontinuierlichen Kompressionen relevant, wird auf 30:2 gewechselt.', 1, 'Beatmungspausen sichern die Ventilation.'),
    ('Ein etCO₂ < 10 mmHg nach 20 min ALS ist nach ERC 2025 ein ausreichendes alleiniges Abbruchkriterium.', 0, 'Niedriger etCO₂ allein rechtfertigt keinen Abbruch.'),
], ERC_ALS, 3),

mtf('REA-04', 'REA', 'Physiologisch gesteuerte CPR', 'Monitoring und Sonderverfahren unter Reanimation (ERC 2025):', [
    ('Bei invasiver Druckmessung ist ein diastolischer Druck von ≈ 30 mmHg ein pragmatisches Ziel.', 1, 'Zusammen mit etCO₂ ≈ 25 mmHg.'),
    ('Ein plötzlicher etCO₂-Abfall bei einem Patienten mit Kreislauf kann einen (Re-)Arrest anzeigen.', 1, 'Kapnografie als Kreislaufmonitor.'),
    ('Fällt der systolische Druck eines monitorüberwachten Patienten anhaltend unter 50 mmHg, können Kompressionen begonnen werden, auch wenn noch ein Rhythmus mit Puls besteht.', 1,
     'ERC 2025 für den „highly monitored arrest“.'),
    ('Eine isolierte RV-Dilatation im Notfallultraschall unter CPR beweist eine Lungenembolie.', 0, 'RV-Dilatation tritt unter CPR auch ohne LE auf.'),
    ('REBOA ist beim traumatischen Kreislaufstillstand präklinisch Standard.', 0, 'Nicht routinemäßig außerhalb von Studien.'),
], ERC_ALS, 3),

mtf('REA-06', 'REA', 'Besondere Umstände', 'Reversible Ursachen und besondere Situationen:', [
    ('Beim traumatischen Kreislaufstillstand kann eine beidseitige Thoraxentlastung (Thorakostomie) Teil der Ursachenbehandlung sein, auch ohne gesicherten Spannungspneumothorax.', 1,
     'HOTT-Prinzip: Hypovolämie, Oxygenierung, Tamponade, Spannungspneu – parallel behandeln.'),
    ('Die manuelle Uterusverlagerung nach links verbessert den venösen Rückstrom, weil die V. cava inferior rechts der Wirbelsäule verläuft.', 1, 'Aortokavale Kompression aufheben.'),
    ('Beim hyperkaliämischen Kreislaufstillstand wird Calciumchlorid 10 % (10 ml) gegeben, obwohl Calcium sonst nicht routinemäßig indiziert ist.', 1, 'Membranstabilisierung; zusätzlich Insulin-Glukose, ggf. Bicarbonat, Dialyse/ECLS.'),
    ('Beim Stillstand nach Lokalanästhetika-Intoxikation ist Lipidemulsion 20 % kontraindiziert, da sie die Adrenalinwirkung aufhebt.', 0, 'Lipid 20 % 1,5 ml/kg Bolus ist indiziert; Reanimation verlängern.'),
    ('Eine Notfall-Hysterotomie wird erst ab der 32. SSW erwogen, da vorher kein hämodynamischer Effekt besteht.', 0, 'Ab ca. 20. SSW (Fundus auf Nabelhöhe) relevant.'),
], ERC_SPEC, 3),

mtf('AW-03', 'AW', 'Schweres Asthma', 'Schwerer Asthmaanfall und Beatmung:', [
    ('Ein normaler oder steigender PaCO₂ bei einem tachypnoeischen Asthmatiker ist ein Warnzeichen der Erschöpfung.', 1, 'Erwartet wäre Hypokapnie.'),
    ('Bei invasiver Beatmung sind niedrige AF und langes I:E (z. B. 1:4) sinnvoll, um die dynamische Überblähung zu begrenzen.', 1, 'Exspirationszeit ist entscheidend.'),
    ('Permissive Hyperkapnie wird vermieden; Ziel ist Normokapnie innerhalb der ersten Stunde.', 0, 'Permissive Hyperkapnie wird zugunsten geringer Überblähung akzeptiert.'),
    ('Ketamin wirkt u. a. über Katecholaminfreisetzung bronchodilatierend und ist zur Einleitung günstig.', 1, 'Zusätzlich kreislaufstabil.'),
    ('Ein PEEP von 15 cmH₂O ist beim beatmeten Asthmatiker immer indiziert, um Auto-PEEP zu verhindern.', 0, 'Hoher externer PEEP kann die Überblähung verstärken – niedrig wählen, intrinsischen PEEP messen.'),
], NVL_ASTHMA + '; ' + NARK, 3),

mtf('AW-04', 'AW', 'Sauerstoff & AECOPD', 'Sauerstofftherapie und NIV bei AECOPD:', [
    ('Hyperoxie erhöht bei COPD den PaCO₂ v. a. durch Aufhebung der hypoxischen Vasokonstriktion (V/Q-Verschlechterung) und den Haldane-Effekt, weniger durch Wegfall des Atemantriebs.', 1,
     'Klassischer Prüfungsfallstrick.'),
    ('Die deutsche S3-Leitlinie empfiehlt für die meisten akut Kranken einen SpO₂-Zielbereich von 92–96 %.', 1, 'Bei Hyperkapnierisiko 88–92 %.'),
    ('Ein pH < 7,25 ist eine absolute Kontraindikation für NIV bei AECOPD.', 0, 'Höheres Versagensrisiko, aber unter Intubationsbereitschaft ein NIV-Versuch möglich.'),
    ('Eine hyperkapnische Bewusstseinseintrübung schließt einen NIV-Versuch unter engmaschiger Überwachung nicht aus.', 1, 'Oft rasche Besserung mit sinkendem CO₂.'),
    ('Venturi-Masken liefern keine definierte FiO₂, da diese stark vom Atemmuster abhängt.', 0, 'Gerade Venturi-Masken liefern eine weitgehend definierte FiO₂.'),
], O2LL + '; ' + NIV, 3),

mtf('AW-05', 'AW', 'Akute Herzinsuffizienz', 'Kardiales Lungenödem – Pathophysiologie und Therapie:', [
    ('CPAP senkt die LV-Nachlast, weil der erhöhte intrathorakale Druck den transmuralen Druck des linken Ventrikels reduziert.', 1, 'Zusätzlich Vorlastsenkung und Rekrutierung.'),
    ('Bei RRsys 85 mmHg ist Nitroglycerin Mittel der Wahl, da es primär die Nachlast senkt.', 0, 'Nitrate wirken v. a. venös; bei Hypotonie kontraindiziert.'),
    ('Furosemid wirkt bereits vor Einsetzen der Diurese über Venodilatation.', 1, 'Frühe Vorlastsenkung.'),
    ('Beim hypertensiven Lungenödem darf der RR in der ersten Stunde stärker als 25 % gesenkt werden.', 1, 'Ausnahme von der 25-%-Regel (wie Aortendissektion).'),
    ('Morphin wird zur Dyspnoe-Reduktion routinemäßig empfohlen.', 0, 'Nicht routinemäßig (Atemdepression, Übelkeit, schlechtere Outcomes in Registern).'),
], NIV + '; ' + NUN, 3),

mtf('KAR-01', 'KAR', 'ACS – Fallstricke', 'Akutes Koronarsyndrom – Fallstricke der Akuttherapie:', [
    ('Nitrate sind nach Sildenafil innerhalb von 24 h bzw. Tadalafil innerhalb von 48 h kontraindiziert.', 1, 'Schwere Hypotonie.'),
    ('Beim inferioren Infarkt mit RV-Beteiligung führt Nitroglycerin über Vorlastsenkung häufig zu ausgeprägter Hypotonie.', 1, 'RV ist vorlastabhängig.'),
    ('ESC 2023 empfiehlt beim NSTE-ACS eine routinemäßige P2Y12-Vorbehandlung, wenn die Angiografie innerhalb von 24 h geplant ist.', 0, 'Nicht routinemäßig bei früh-invasiver Strategie.'),
    ('Unfraktioniertes Heparin 70–100 IE/kg bei geplanter PCI; Enoxaparin ist eine Alternative.', 1, 'ESC 2023.'),
    ('Wegen verzögerter Resorption oraler P2Y12-Hemmer sind Opioide beim ACS grundsätzlich kontraindiziert.', 0, 'Interaktion bekannt, aber Opioide können erwogen werden.'),
], ESC_ACS, 3),

mtf('KAR-02', 'KAR', 'Reperfusion', 'Reperfusionsstrategie beim akuten Koronarverschluss:', [
    ('Primäre PCI ist Strategie der Wahl, wenn von Diagnose bis Drahtpassage ≤ 120 min erwartet werden.', 1, 'Sonst Lyse ≤ 10 min nach Diagnose.'),
    ('Nach präklinischer Fibrinolyse wird routinemäßig in ein PCI-Zentrum transportiert; Angiografie innerhalb von 2–24 h.', 1, 'Pharmakoinvasive Strategie; bei Lyseversagen Rescue-PCI.'),
    ('Anhaltender Brustschmerz mit hämodynamischer Instabilität ohne ST-Hebung wird wie ein STEMI sofort invasiv versorgt.', 1, 'Very-high-risk NSTE-ACS: < 2 h.'),
    ('Ein Symptombeginn > 12 h schließt eine Reperfusion grundsätzlich aus, auch bei persistierender Ischämie.', 0, 'Bei anhaltender Ischämie, Instabilität oder Rhythmusstörungen weiterhin PCI.'),
    ('Fehlende ST-Hebungen schließen einen akuten Koronarverschluss aus.', 0, 'OMI ohne STEMI-Kriterien ist häufig.'),
], ESC_ACS + '; ' + SMITH_OMI, 3),

mtf('KAR-04', 'KAR', 'Tachykardien – Fallstricke', 'Tachykarde Rhythmusstörungen – Fallstricke:', [
    ('Bei Herztransplantierten kann Adenosin eine verlängerte Asystolie auslösen; die Dosis wird reduziert.', 1, 'Denervierte Überempfindlichkeit, z. B. 3 mg initial.'),
    ('Eine regelmäßige Breitkomplextachykardie bei bekannter KHK ist bis zum Beweis des Gegenteils eine VT.', 1, 'SVT mit Schenkelblock ist die Ausnahme.'),
    ('Beim präexzitierten Vorhofflimmern ist Amiodaron das sichere Mittel der Wahl, da es den AV-Knoten nicht beeinflusst.', 0,
     'Amiodaron wirkt auch am AV-Knoten; bevorzugt Kardioversion. AV-Knoten-Blocker meiden.'),
    ('Bei Vorhofflattern 2:1 kann Adenosin die Flatterwellen demaskieren, beendet das Flattern aber typischerweise nicht.', 1, 'Diagnostischer Nutzen.'),
    ('ERC 2025 empfiehlt bei instabilem Vorhofflimmern eine initiale Kardioversion mit 70 J.', 0, 'Maximale Energie.'),
], ERC_TACHY, 3),

mtf('KAR-05', 'KAR', 'Bradykardien – Fallstricke', 'Bradykardie mit Instabilitätszeichen – Fallstricke:', [
    ('Atropin ist beim hochgradigen AV-Block mit breitem Ersatzrhythmus meist unwirksam und wird gemieden.', 1, 'Infranodaler Block.'),
    ('Bei Bradykardie nach Herztransplantation oder hoher Querschnittläsion ist Aminophyllin eine Option.', 1, 'ERC 2025.'),
    ('Isoprenalin 5 µg/min ist eine Zweitlinienoption.', 1, 'Alternativ Adrenalin 2–10 µg/min.'),
    ('Ein breiter Komplex nach jedem Pacing-Spike beweist die mechanische Kapture.', 0, 'Artefakte täuschen Komplexe vor – Puls femoral tasten.'),
    ('Atropin-Dosen unter 0,5 mg sind sicherer, da paradoxe Bradykardien nur bei hohen Dosen auftreten.', 0, 'Paradoxe Bradykardie gerade bei zu niedriger Dosis.'),
], ERC_TACHY, 3),

mtf('KAR-06', 'KAR', 'Lungenembolie – Hämodynamik', 'Hochrisiko-Lungenembolie – Pathophysiologie und Management:', [
    ('Volumen > 500 ml kann über Septumverlagerung das LV-Schlagvolumen weiter senken.', 1, 'Ventrikuläre Interdependenz.'),
    ('Noradrenalin ist Vasopressor der Wahl im LE-bedingten Schock.', 1, 'Erhält koronare Perfusion des RV.'),
    ('Ein normales Troponin schließt eine Hochrisiko-LE aus.', 0, 'Hochrisiko wird klinisch definiert (Schock).'),
    ('Bei Narkoseeinleitung ist mit Kreislaufkollaps zu rechnen, da Vasodilatation und Überdruckbeatmung die RV-Funktion verschlechtern.', 1, 'Wenn möglich vermeiden; sonst kreislaufstabil einleiten, Vasopressor laufen lassen.'),
    ('Der Wells-Score ersetzt bei hämodynamischer Instabilität die Bildgebung.', 0, 'Instabil: Echo am Bett/CT, ggf. sofortige Lyse.'),
], ESC_LE, 3),

mtf('NEU-01', 'NEU', 'Schlaganfall – Fallstricke', 'Präklinisches Schlaganfall-Management – Fallstricke:', [
    ('Ein Blutzucker < 50 mg/dl kann fokal-neurologische Defizite verursachen, die einen Schlaganfall imitieren.', 1, 'Immer BZ messen.'),
    ('Präklinische Skalen wie RACE oder FAST-ED dienen der Abschätzung eines großen Gefäßverschlusses.', 1, 'Steuern die Zielklinik.'),
    ('Da für die Lyse RR < 185/110 mmHg nötig ist, wird bereits präklinisch auf diesen Wert gesenkt.', 0, 'Präklinisch nur > 220/120 mmHg vorsichtig senken.'),
    ('Beim Wake-up-Stroke ist eine Lyse mit MRT-Mismatch (DWI/FLAIR) möglich.', 1, 'Bildgebungs-gestützte Selektion.'),
    ('Eine Oberkörperhochlage von 30° ist bei jedem Schlaganfall Pflicht, da sie die Penumbraperfusion verbessert.', 0, 'Kein Nutzen belegt (HeadPoST); Lagerung nach Klinik/Aspirationsrisiko.'),
], DGN_STROKE, 3),

mtf('NEU-04', 'NEU', 'SHT – Sekundärschäden', 'Schweres SHT – Pathophysiologie und Präklinik:', [
    ('Bereits eine einzelne hypotone Episode (RRsys < 90 mmHg) ist beim schweren SHT mit erhöhter Letalität assoziiert.', 1, 'Sekundärschaden.'),
    ('Bei Einklemmungszeichen kann kurzfristig eine moderate Hyperventilation (etCO₂ ≈ 30–35 mmHg) als Überbrückung erwogen werden.', 1, 'Nur kurzfristig, nicht prophylaktisch.'),
    ('Die Cushing-Trias umfasst Hypertonie, Bradykardie und unregelmäßige Atmung.', 1, 'Spätzeichen erhöhten Hirndrucks.'),
    ('Hypertone Kochsalzlösung ist präklinisch Standard bei jedem GCS ≤ 8.', 0, 'Nur bei Herniationszeichen erwägen.'),
    ('Eine Zervikalstütze ist beim SHT unbedenklich, da sie den venösen Abfluss nicht beeinträchtigt.', 0, 'Zu enge Anlage kann den ICP erhöhen.'),
], S3PT + '; ' + ROSSAINT, 3),

mtf('NEU-05', 'NEU', 'Hypoglykämie – Fallstricke', 'Hypoglykämie – Fallstricke:', [
    ('Glukose 10 % reduziert gegenüber 40 % Venenreizung und Überkorrektur, braucht aber mehr Volumen.', 1, 'Gleiche Grammzahl, mehr Volumen.'),
    ('Glukagon wirkt über hepatische Glykogenolyse und ist daher bei Alkoholikern und Hungerzuständen oft unwirksam.', 1, 'Leere Speicher.'),
    ('Nach Hypoglykämie durch Basalinsulin-Überdosis ist ein Transportverzicht nach BZ-Normalisierung unbedenklich.', 0, 'Lang wirksam – Rezidivgefahr.'),
    ('Betablocker verstärken die adrenergen Warnsymptome der Hypoglykämie.', 0, 'Sie maskieren Tremor und Tachykardie (Schwitzen bleibt).'),
    ('Bei Sulfonylharnstoff-Hypoglykämie ist Octreotid in der Klinik eine spezifische Option.', 1, 'Hemmt die Insulinsekretion.'),
], NUN + '; ' + HYPO_LL + '; ' + GIZ, 3),

mtf('TRA-01', 'TRA', 'Blutungskontrolle', 'Hämorrhagischer Schock beim Trauma:', [
    ('Tranexamsäure sollte innerhalb von 3 h gegeben werden; eine spätere Erstgabe ist mit höherer Letalität assoziiert.', 1, 'CRASH-2.'),
    ('Permissive Hypotension gilt nicht beim SHT; dort RRsys ≥ 90 mmHg.', 1, 'S3 Polytrauma.'),
    ('Beim penetrierenden Rumpftrauma wird die Zeit vor Ort für maximale präklinische Volumentherapie genutzt.', 0, 'Schnellstmöglicher Transport ins nächste Traumazentrum.'),
    ('Chitosan-Hämostyptika werden bei blutenden Stichwunden ≥ 3 cm zur Tamponade empfohlen.', 1, 'S3, Empfehlungsgrad A.'),
    ('Tourniquets sind an Unterarm und Unterschenkel grundsätzlich kontraindiziert.', 0, 'Möglich, wegen zwei Knochen evtl. weniger effektiv – dann proximal.'),
], S3PT, 3),

mtf('TRA-03', 'TRA', 'Wirbelsäule', 'Wirbelsäulentrauma und Immobilisation:', [
    ('NEXUS: keine Bildgebung bei fehlendem Mittellinien-Druckschmerz, fehlendem fokalem Defizit, normaler Vigilanz, ohne Intoxikation und ablenkende Verletzung.', 1, 'Alle fünf Kriterien müssen erfüllt sein.'),
    ('Die Canadian C-Spine Rule prüft bei Niedrigrisiko-Patienten die aktive Rotation (45° beidseits).', 1, 'Nur wenn sicher möglich.'),
    ('Eine Zervikalstütze kann den Hirndruck erhöhen und die Atemwegssicherung erschweren.', 1, 'Nebenwirkungen beachten.'),
    ('Beim isolierten penetrierenden Halstrauma ohne Defizit verbessert eine HWS-Immobilisation regelhaft das Outcome.', 0, 'Eher schlechteres Outcome (Verzögerung, verdeckte Befunde).'),
    ('Spinaler und neurogener Schock sind Synonyme.', 0, 'Spinaler Schock = Reflexverlust; neurogener Schock = Hypotonie + Bradykardie.'),
], S3PT + '; ' + ROSSAINT, 3),

mtf('TRA-04', 'TRA', 'Trauma-Koagulopathie', 'Becken, Schock und Gerinnung:', [
    ('Eine zu hoch angelegte Beckenschlinge (über den Beckenkämmen) kann eine Open-Book-Verletzung aufspreizen.', 1, 'Auf Höhe der Trochanteres majores.'),
    ('Hypothermie hemmt die Gerinnungsenzyme; Standardtests bei 37 °C bilden das nicht ab.', 1, 'Labor wird bei 37 °C gemessen.'),
    ('Eine Hypokalzämie nach Massivtransfusion beeinträchtigt Gerinnung und Kontraktilität.', 1, 'Citrat bindet Calcium.'),
    ('Ein normaler Schockindex schließt bei jungen Patienten eine relevante Blutung aus.', 0, 'Junge kompensieren lange.'),
    ('HES-Lösungen werden beim Trauma empfohlen, da sie länger intravasal verbleiben.', 0, 'Nicht empfohlen.'),
], S3PT + '; ' + MARINO, 3),

mtf('TRA-05', 'TRA', 'Verbrennung – Feinheiten', 'Verbrennungen – Feinheiten:', [
    ('Bei Kindern wird die VKOF nach Lund-Browder bzw. angepasster Neunerregel geschätzt, da der Kopfanteil größer ist.', 1, 'Säugling Kopf ≈ 18 %.'),
    ('Ein Inhalationstrauma erhöht den Volumenbedarf über die Parkland-Kalkulation hinaus.', 1, 'Formel ist nur Startwert.'),
    ('Zirkuläre drittgradige Thoraxverbrennungen können eine Escharotomie erfordern.', 1, 'Ventilationseinschränkung.'),
    ('Erstgradige Verbrennungen werden in die Parkland-Berechnung einbezogen.', 0, 'Nur ab Grad 2.'),
    ('Bei 20 % VKOF wird präklinisch die volle Parkland-Menge der ersten 8 h in der ersten Stunde infundiert.', 0, 'Überinfusion („Fluid Creep“) vermeiden.'),
], BURN, 3),

mtf('TRA-07', 'TRA', 'Analgesie – Feinheiten', 'Analgesie und Analgosedierung im Einsatz:', [
    ('Ketamin ist beim SHT unter kontrollierter Ventilation nicht kontraindiziert.', 1, 'Kein relevanter ICP-Anstieg bei Normokapnie.'),
    ('Intranasales Fentanyl wird mit ca. 1–2 µg/kg dosiert.', 1, 'Mukosaler Zerstäuber.'),
    ('Opioid + Benzodiazepin wirken synergistisch atemdepressiv.', 1, 'Dosis reduzieren.'),
    ('Metamizol ist bei Kolikschmerz unwirksam, da es nicht spasmolytisch wirkt.', 0, 'Metamizol wirkt auch spasmolytisch.'),
    ('Im hämorrhagischen Schock sind Opioide absolut kontraindiziert.', 0, 'Vorsichtig titrieren bzw. Ketamin bevorzugen.'),
], S3PT + '; ' + PHARM, 3),

mtf('PAE-01', 'PAE', 'Kinderreanimation 2025', 'Pädiatrische Reanimation und Schock (ERC 2025):', [
    ('Beim beobachteten, monitorüberwachten Kammerflimmern sind bis zu drei Schocks à 4 J/kg in Folge möglich.', 1, 'Analog zum Erwachsenen.'),
    ('Bei refraktärem VF ist eine stufenweise Steigerung bis 8 J/kg möglich, ohne das Erwachsenenmaximum zu überschreiten.', 1, 'Neu 2025.'),
    ('Volumenbolus 10 ml/kg; bei Jugendlichen nun bis max. 500 ml pro Bolus.', 1, 'Vorher 250 ml.'),
    ('Im hämorrhagischen Schock des Kindes werden Kristalloide ohne Obergrenze gegeben, bis Normotonie erreicht ist.', 0, 'Kristalloide auf 20 ml/kg begrenzen, früh Blutprodukte.'),
    ('Ein i.o.-Zugang wird erst nach 10 min erfolgloser i.v.-Versuche empfohlen.', 0, 'Spätestens nach 5 min.'),
], ERC_PLS, 3),

mtf('PAE-02', 'PAE', 'Stridor beim Kind', 'Obere Atemwegsobstruktion beim Kind:', [
    ('Dexamethason 0,15 mg/kg ist beim leichten bis mittelschweren Krupp ähnlich wirksam wie höhere Dosen.', 1, 'Niedrige Dosis genügt meist.'),
    ('Nach vernebeltem Adrenalin wird wegen möglichem Rebound mindestens 2–4 h überwacht.', 1, 'Wirkung lässt nach.'),
    ('Epiglottitis: Speichelfluss, kloßige Sprache, vornübergebeugtes Sitzen und hohes Fieber.', 1, 'Seit Hib-Impfung selten.'),
    ('Die bakterielle Tracheitis bessert sich typischerweise rasch auf Adrenalin-Inhalation.', 0, 'Spricht schlecht an – toxisches Kind, Intubation oft nötig.'),
    ('Beim Säugling mit Fremdkörper werden Oberbauchkompressionen statt Thoraxkompressionen durchgeführt.', 0, 'Säugling: Rückenschläge + Thoraxkompressionen.'),
], ERC_PLS + '; ' + ROSSAINT, 3),

mtf('PAE-06', 'PAE', 'Kindliche Physiologie', 'Physiologische Besonderheiten bei Kindern:', [
    ('Kinder kompensieren Volumenverlust lange über Tachykardie und Vasokonstriktion; Hypotonie ist ein Spätzeichen.', 1, 'Dekompensation droht.'),
    ('Die untere Grenze des systolischen RR ab 1 Jahr lässt sich mit 70 + 2 × Alter (mmHg) abschätzen.', 1, 'PALS-Faustregel.'),
    ('Säuglinge haben wegen höheren O₂-Verbrauchs eine kürzere Apnoetoleranz.', 1, 'Rasche Desaturation.'),
    ('Die hypoxische Bradykardie des Säuglings wird primär mit Atropin behandelt.', 0, 'Oxygenieren und beatmen.'),
    ('Säuglinge haben einen relativ kleinen Hinterkopf, daher wird der Kopf zur Neutralposition erhöht gelagert.', 0, 'Großes Okziput – eher Schulterrolle.'),
], ERC_PLS + '; ' + ROSSAINT, 3),

mtf('TOX-03', 'TOX', 'Opioide – Fallstricke', 'Opioid-Intoxikation – Fallstricke:', [
    ('Naloxon kann bei Abhängigen ein akutes Entzugssyndrom mit Lungenödem und Tachyarrhythmien auslösen.', 1, 'Titrieren!'),
    ('Bei Fentanyl-Analoga (z. B. Carfentanil) sind oft wiederholte oder höhere Naloxon-Dosen nötig.', 1, 'Hohe Potenz.'),
    ('Thoraxrigidität („Wooden Chest“) unter Fentanyl kann die Maskenbeatmung erschweren.', 1, 'Ggf. Relaxierung.'),
    ('Die Halbwertszeit von Naloxon (ca. 60–90 min) ist länger als die von Methadon.', 0, 'Methadon wirkt viel länger (HWZ > 24 h) – Rebound.'),
    ('Eine Miosis fehlt bei Opioidintoxikation nie, auch nicht bei Hypoxie oder Mischintoxikation.', 0, 'Kann fehlen.'),
], GIZ, 3),

mtf('TOX-05', 'TOX', 'Ertrinken & Hitze', 'Ertrinken und Hitzschlag:', [
    ('Beim Ertrinken ist Hypoxie der Hauptmechanismus; Süß- vs. Salzwasser hat präklinisch keine therapeutische Relevanz.', 1, 'Elektrolytverschiebungen klinisch selten relevant.'),
    ('AED-Pads können nach Abtrocknen der Brust sicher verwendet werden.', 1, 'Patient aus dem Wasser.'),
    ('Aktive Kühlung beim Hitzschlag wird bei etwa 38 °C beendet.', 1, 'Überkühlung vermeiden.'),
    ('Beim belastungsinduzierten Hitzschlag ist Kaltwasser-Immersion wegen Kammerflimmern-Gefahr kontraindiziert.', 0, 'Immersion ist die effektivste Methode.'),
    ('Dantrolen ist Standardtherapie beim klassischen Hitzschlag.', 0, 'Kein Nutzen belegt.'),
], ERC_SPEC + '; ' + ERC_PLS, 3),

mtf('PHA-01', 'PHA', 'Analgetika – Pharmakologie', 'Analgetika – Pharmakologie:', [
    ('Esketamin ist etwa doppelt so potent wie das Razemat; die Dosis wird etwa halbiert.', 1, 'S-Enantiomer.'),
    ('Ketamin-Halluzinationen lassen sich durch niedrig dosierte Benzodiazepine reduzieren.', 1, 'Co-Medikation.'),
    ('Fentanyl setzt seltener Histamin frei als Morphin.', 1, 'Günstiger bei Hypotonie/Asthma.'),
    ('Paracetamol i.v. darf beim Erwachsenen > 50 kg unabhängig von Leberfunktion oder Alkoholabusus bis 4 g/24 h gegeben werden.', 0, 'Bei Risikofaktoren Dosis reduzieren.'),
    ('Nalbuphin (κ-Agonist/μ-Antagonist) verstärkt nachfolgende μ-Agonisten.', 0, 'Es schwächt sie ab (partieller Antagonismus, Ceiling-Effekt).'),
], PHARM, 3),

mtf('PHA-05', 'PHA', 'Anaphylaxie – Pharmakologie', 'Anaphylaxie – Pharmakologie:', [
    ('Adrenalin wirkt über α₁ (Vasokonstriktion, Ödemreduktion), β₁ (Inotropie) und β₂ (Bronchodilatation, Mastzellstabilisierung).', 1, 'Daher Mittel der Wahl.'),
    ('Bei therapierefraktärer Anaphylaxie kann eine titrierte Adrenalin-Infusion nötig werden.', 1, 'Unter Monitoring.'),
    ('Biphasische Reaktionen sind möglich; nach schwerer Anaphylaxie ist Überwachung sinnvoll.', 1, 'Stunden später.'),
    ('Glukokortikoide verhindern biphasische Reaktionen zuverlässig.', 0, 'Kein sicherer Beleg.'),
    ('Die subkutane Adrenalingabe ist der intramuskulären gleichwertig.', 0, 'i.m. erreicht schneller höhere Spiegel.'),
], ANA, 3),
]

NUMS = [
num('KAR-13', 'KAR', 'Heparin', 'STEMI, Patient 85 kg. Heparin 70 IE/kg; vorhanden: 25.000 IE/5 ml. Wie viele ml ziehen Sie auf?', 'ml', 1.2, 0.05,
    '70 × 85 = 5950 IE; 25.000 IE/5 ml = 5000 IE/ml → 5950/5000 ≈ 1,2 ml.', ESC_ACS + '; ' + NUN, 3),
num('AW-14', 'AW', 'Sauerstoffvorrat', '10-l-Flasche mit 150 bar. Respirator mit FiO₂ 1,0 und AMV 8 l/min (ohne Antriebsgasverbrauch); 20 bar Reserve einplanen. Wie viele Minuten reicht der Vorrat?', 'min', 162, 3,
    '(150 − 20) bar × 10 l = 1300 l; 1300 / 8 ≈ 162 min. Gasbetriebene Respiratoren verbrauchen zusätzlich Antriebsgas!', ROSSAINT, 3),
num('TRA-15', 'TRA', 'VKOF', 'Erwachsener: Verbrennung Grad 2 an Kopf, gesamter Rumpfvorderseite und linkem Arm; zusätzlich Grad-1-Rötung an beiden Beinen. Welche VKOF (%) geht in die Parkland-Formel ein?', '%', 36, 0,
    '9 + 18 + 9 = 36 %. Grad 1 zählt nicht.', BURN, 3),
num('PAE-14', 'PAE', 'Adrenalin beim Kind', 'Kind, 4 Jahre, Kreislaufstillstand. Gewicht nach (Alter + 4) × 2. Adrenalin 1 mg auf 10 ml verdünnt. Wie viele ml pro Gabe?', 'ml', 1.6, 0.05,
    '16 kg × 10 µg = 160 µg; 100 µg/ml → 1,6 ml.', ERC_PLS, 3),
num('PAE-16', 'PAE', 'Volumen im Blutungsschock', 'Kind, 7 Jahre, hämorrhagischer Schock. Gewicht nach (Alter + 4) × 2. Ab welcher kumulativen Kristalloidmenge (ml) sollen nach ERC 2025 Blutprodukte folgen (20 ml/kg)?', 'ml', 440, 5,
    '22 kg × 20 ml = 440 ml – danach Blutprodukte statt weiterer Kristalloide.', ERC_PLS, 3),
num('PHA-12', 'PHA', 'Midazolam verdünnt', 'Midazolam 15 mg/3 ml wird auf 15 ml verdünnt. Sedierung mit 0,05 mg/kg bei 70 kg: wie viele ml der Verdünnung?', 'ml', 3.5, 0.1,
    '15 mg/15 ml = 1 mg/ml; 0,05 × 70 = 3,5 mg → 3,5 ml.', PHARM, 2),
num('TOX-14', 'TOX', 'Paracetamol-Intoxikation', '70-kg-Patient hat 30 Tabletten Paracetamol à 500 mg eingenommen. Aufgenommene Dosis in mg/kg?', 'mg/kg', 214, 3,
    '15.000 mg / 70 kg ≈ 214 mg/kg – deutlich über der toxischen Schwelle (≈ 150 mg/kg): N-Acetylcystein, Spiegel nach 4 h.', GIZ, 3),
]

# harder distractors (correct answer stays at index 0)
OPTS = {
    'REA-15': ['Kammerflimmern', 'Polymorphe VT (Torsade de pointes)', 'Kammerflattern', 'Vorhofflimmern mit Schenkelblock und Artefakten'],
    'KAR-15': ['Monomorphe VT – instabil: synchronisierte Kardioversion', 'SVT mit vorbestehendem Schenkelblock – Adenosin', 'Präexzitiertes Vorhofflimmern – Ibutilid', 'Sinustachykardie bei Hyperkaliämie – Calcium'],
    'KAR-16': ['AV-Block III. Grades mit breitem Kammerersatzrhythmus', 'AV-Block II Typ Mobitz II 2:1', 'Sinusbradykardie mit AV-Block I', 'Vorhofflimmern mit langsamer Überleitung'],
    'KAR-17': ['AV-Block II Typ Mobitz II (3:2)', 'AV-Block II Typ Wenckebach (3:2)', 'Sinusarrest', 'Blockierte supraventrikuläre Extrasystolen'],
    'KAR-18': ['Tachyarrhythmia absoluta bei Vorhofflimmern', 'Multifokale atriale Tachykardie', 'Vorhofflattern mit wechselnder Überleitung', 'Sinustachykardie mit SVES'],
    'KAR-19': ['AV-Knoten-Reentry-Tachykardie', 'Vorhofflattern 2:1 mit verdeckten Flatterwellen', 'Sinustachykardie', 'Orthodrome AVRT bei WPW'],
    'KAR-20': ['Vorhofflattern mit 2:1-Überleitung', 'Atriale Tachykardie mit Block', 'AV-Knoten-Reentry', 'Sinustachykardie'],
    'KAR-21': ['Inferiorer OMI mit reziproker ST-Senkung in aVL – Katheterlabor', 'Akute Perikarditis', 'Frühe Repolarisation', 'Inferiorer Altinfarkt mit Aneurysma'],
    'KAR-22': ['Hyperakute T-Wellen anterior – früher LAD-Verschluss (OMI)', 'Hyperkaliämie', 'Benigne frühe Repolarisation', 'Linksventrikuläre Hypertrophie mit Strain'],
}
