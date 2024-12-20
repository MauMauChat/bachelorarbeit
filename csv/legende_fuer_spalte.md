# Legende zu den Spalte der CSV-Files

### Datei: `Alle Fragen.csv`

| Spalte                     | Beschreibung |
|----------------------------|--------------|
| `RLV_KEY`                  | Eindeutiger Schlüssel für die Lehrveranstaltung (LV). |
| `SEMESTER`                 | Semesterbezeichnung (z.B., "15S" für Sommersemester 2015). |
| `TYP`                      | Typ der Lehrveranstaltung (z.B., SE für Seminar). |
| `STUNDEN`                  | Wöchentliche Stundenanzahl für die LV. |
| `CREDITS`                  | Vergebene ECTS-Punkte für die LV. |
| `LV_STATUS_NR`             | Statusnummer der LV. |
| `LV_STATUS`                | Status der LV (z.B., genehmigt). |
| `FRAGE_KEY`                | Eindeutiger Schlüssel für die Frage. |
| `KOMPONENTE_NUMMERIERUNG`  | Nummerierung der Komponente innerhalb der LV. |
| `FRAGE_NUMMERIERUNG`       | Nummer der Frage innerhalb des Fragebogens. |
| `VEROEFFENTLICHEN`         | Gibt an, ob die Frage veröffentlicht wurde (J/N). |
| `RLV_KOMPONENTEN_LEHRER`   | Anzahl der Dozenten in der LV-Komponente. |
| `ANZ_RUECKLAUF`            | Anzahl der Rückmeldungen zur Frage. |
| `ANZ_FEEDBACK`             | Anzahl der erhaltenen Feedbacks. |
| `ANZ_ABGELEHNT`            | Anzahl der abgelehnten Rückmeldungen. |
| `ANZ_ABGELEHNT_ANMERKUNG`  | Anmerkungen zu abgelehnten Rückmeldungen. |
| `IST_GESAMTFRAGE`          | Kennzeichnung, ob es eine allgemeine Frage ist (J/N). |
| `FRAGETEXT`                | Text der Frage. |
| `FRAGE_TYP`                | Typ der Frage (z.B., Optionen oder Freitext). |
| `FRAGETYP_BEZEICHNUNG`     | Beschreibung des Fragetyp. |
| `KEINE_ANTWORT_MOEGLICH`   | Gibt an, ob keine Antwort möglich ist (J/N). |
| `OPTIONEN`                 | Antwortoptionen für die Frage. |
| `ANZ_OPTIONEN`             | Anzahl der Antwortoptionen. |
| `EINS` bis `ZWOELF`        | Antworten in einer Skala (1–12). |
| `ANZ_ANTWORT_FRAGE_GESAMT` | Anzahl der Antworten für die gesamte Frage. |
| `ANZ_ANTWORT_FRAGE`        | Anzahl der Antworten zur spezifischen Frage. |
| `ANZ_KEINE_ANTWORT_FRAGE`  | Anzahl der Fragen, die ohne Antwort geblieben sind. |
| `ANZ_FREITEXT_ANTWORT`     | Anzahl der Freitextantworten. |

---

### Datei: `FB Freitextantworten.csv`

| Spalte               | Beschreibung |
|----------------------|--------------|
| `RLVKEY`             | Schlüssel für die LV. |
| `SEMESTER`           | Semesterbezeichnung. |
| `TYP`                | Typ der LV. |
| `STUNDEN`            | Wöchentliche Stundenanzahl. |
| `CREDITS`            | Vergebene ECTS-Punkte. |
| `LV_STATUS_NR`       | Statusnummer der LV. |
| `LV_STATUS`          | Status der LV (z.B., genehmigt). |
| `KOMPONENTEN_TYP`    | Typ der LV-Komponente (z.B., Uni). |
| `FRAGE_TYP`          | Fragetyp (z.B., Freitext). |
| `FRAGETEXT`          | Text der Frage. |
| `OPTIONEN`           | Antwortoptionen (falls vorhanden). |
| `ANTWORT`            | Antwortnummer (z.B., für Auswahlfragen). |
| `OPTIONNR`           | Nummer der gewählten Option. |
| `FREITEXT`           | Freitextantwort des Befragten. |

---

### Datei: `Alle Fragebögen.csv`

| Spalte                       | Beschreibung |
|------------------------------|--------------|
| `SEM`                        | Semester-ID oder Kürzel. |
| `RLVKEY`                     | Schlüssel für die LV. |
| `SEMESTER`                   | Semesterbezeichnung. |
| `TYP`                        | Typ der LV. |
| `STUNDEN`                    | Wöchentliche Stundenanzahl. |
| `CREDITS`                    | Vergebene ECTS-Punkte. |
| `LV_STATUS_NR`               | Statusnummer der LV. |
| `LV_STATUS`                  | Status der LV. |
| `FRAGEBOGEN_ID`              | ID des Fragebogens. |
| `BEZEICHNUNG`                | Bezeichnung des Fragebogens. |
| `BEGINN_BEFRAGUNG`           | Beginn der Befragung. |
| `ENDE_BEFRAGUNG`             | Ende der Befragung. |
| `ENDE_STELLUNGNAHME`         | Ende der Stellungnahme. |
| `BEGINN_VEROEFFENTLICHUNG`   | Beginn der Veröffentlichung der Ergebnisse. |
| `HAT_STELLUNGNAHME`          | Ob eine Stellungnahme abgegeben wurde (J/N). |
| `DATUM_STELLUNGNAHME`        | Datum der Stellungnahme. |
| `STELLUNGNAHME`              | Text der Stellungnahme. |
| `GESAMTFRAGE`                | Ob es sich um eine allgemeine Frage handelt. |
| `FRAGE_KEY`                  | Schlüssel der Frage. |
| `IST_GESAMTFRAGE`            | Kennzeichnung für allgemeine Frage (J/N). |
| `FRAGETEXT`                  | Text der Frage. |
| `FRAGE_TYP`                  | Typ der Frage (Optionen, Freitext). |
| `FRAGETYP_BEZEICHNUNG`       | Beschreibung des Fragetyp. |
| `KOMPONENTEN_TYP`            | Typ der LV-Komponente. |
| `KOMPONENTE_NUMMERIERUNG`    | Nummer der Komponente in der LV. |
| `FRAGE_NUMMERIERUNG`         | Nummer der Frage. |
| `KEINE_ANTWORT_MOEGLICH`     | Ob keine Antwort möglich ist (J/N). |
| `FREITEXT_MOEGLICH`          | Ob Freitextantwort möglich ist. |
| `SINGLE_MULTIPLE`            | Ob es sich um eine Einzelauswahl oder Mehrfachauswahl handelt. |
| `AUSWERTUNG`                 | Kennzeichnung zur Auswertung (z.B., ob Frage bewertet wird). |
| `OPTIONEN_GRUPPE_BEZ`        | Bezeichnung der Optionsgruppe. |
| `OPTIONEN`                   | Antwortoptionen der Frage. |
| `ANZ_OPTIONEN`               | Anzahl der Antwortoptionen. |
| `VEROEFFENTLICHEN`           | Ob die Ergebnisse veröffentlicht werden. |
| `RLV_KOMPONENTEN_GESAMT`     | Gesamtanzahl der LV-Komponenten. |
| `RLV_KOMPONENTEN_UNI`        | Anzahl der universitätsweiten Komponenten. |
| `RLV_KOMPONENTEN_LEHRER`     | Anzahl der Dozenten in den LV-Komponenten. |
| `ANZ_RUECKLAUF`              | Anzahl der Rückmeldungen zur Frage. |
| `ANZ_FEEDBACK`               | Anzahl der erhaltenen Feedbacks. |
| `ANZ_ABGELEHNT`              | Anzahl der abgelehnten Rückmeldungen. |
| `ANZ_ABGELEHNT_ANMERKUNG`    | Anmerkungen zu abgelehnten Rückmeldungen. |
| `ANZ_ANTWORT_FRAGE_GESAMT`   | Gesamtanzahl der Antworten zur Frage. |
| `ANZ_ANTWORT_FRAGE`          | Anzahl der Antworten zur spezifischen Frage. |
| `ANZ_KEINE_ANTWORT_FRAGE`    | Anzahl unbeantworteter Fragen. |
| `ANZ_FREITEXT_ANTWORT`       | Anzahl der Freitextantworten. |
| `BEANTWORTET`                | Anzahl der beantworteten Fragen. |
| `KEINE_ANTWORT`              | Anzahl der unbeantworteten Fragen. |
| `EINS` bis `ZWOELF`          | Antworten auf einer Skala (1–12). |
| `ANTWORT`                    | Antwortinhalt (z.B., gewählte Option). |
| `FREITEXT`                   | Freitextantwort. |
| `ANTWORT_FREITEXT`           | Detaillierte Freitextantwort. |
| `FEEDBACK_GEWERTET`          | Ob Feedback bewertet wurde. |
| `FEEDBACK_VEROEFFENTLICHEN`  | Ob Feedback veröffentlicht wurde. |
| `FEEDBACK_SICHTBAR`          | Ob Feedback sichtbar ist. |
| `NOTE_IN_PROZENT`            | Bewertungsnote in Prozent. |
| `NOTE`                       | Endnote der LV. |

---
