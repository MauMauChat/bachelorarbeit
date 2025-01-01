
Ich benötige eine vollständige und professionell kommentierte Umsetzung der folgenden Bash-Skripte in Python für den Einsatz in einem **Unternehmensumfeld**. Bitte berücksichtige alle möglichen Fehlerquellen und Benutzer-Eingaben. Erstelle die Files mit echo oder cat und speichere sie mit >> in den Ordner ~/Documents/Notes/bachelorarbeit/erstelltes-programm. Erstelle auch alle folder mit mkdir -p. Alles soll in einem groß Block sein, den man rauskopieren kann. Ich möchte diesen Block direkt in das Termianl eingebe. Es soll somit das vollkommen fertige Programm in einem block in alle richitgen Ordner haben.

### Verwendete Technologien:
- **Python**
- **R** (für statistische Analysen und Visualisierungen)
- **Python GUI-Bibliothek** ( z. B. Tkinter oder PyQt)
- **AFINN** für die sentimental Analyse 
- **fpdf** from fpdf import FPDF für die Erstellung der Templates.
### **Empfohlene Struktur**


sentiment_analysis_app/
├── app.py                 # Hauptdatei zum Starten der GUI-Anwendung
├── gui/
│   ├── main_window.py      # GUI-Setup und Hauptfenster-Logik
│   ├── file_selector.py    # GUI-Komponenten für die Auswahl der Dateien/Ordner
├── analysis/
│   ├── sentiment_analyzer.py  # Logik für die Sentimentanalyse
│   ├── language_detector.py   # Sprachenerkennung und Sprachverwaltung
│   ├── report_generator.py    # Generiert PDF-Reports
│   ├── r_visualization.py     # Integration von R für statistische Analysen
├── utils/
│   ├── file_manager.py      # Dateioperationen und Verzeichnis-Management
│   ├── constants.py         # Globale Konstanten und Pfade
 

### Pfade
/home/lucy/Documents/zulöschen  // Hier soll die Output-pdf und bild speichrung (bilder sind in einem bild Ordner sein.
csv $ tree
.
└── LV-Feedback-Rohdaten
    ├── LV-Feedback_15S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_15W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_16S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_16W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_17S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_17W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_18S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_18W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_19S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_19W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_20S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_20W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_21S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_21W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_22S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_22W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_23S
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    ├── LV-Feedback_23W
    │   ├── Alle Fragebögen.csv
    │   ├── Alle Fragen.csv
    │   └── FB Freitextantworten.csv
    └── LV-Feedback_24S
        ├── Alle Fragebögen.csv
        ├── Alle Fragen.csv
        └── FB Freitextantworten.csv

20 directories, 57 files
csv $ pwd
/home/lucy/Documents/Notes/bachelorarbeit/csv
csv $ 

### **Details zur Aufteilung der Module**

1. **`app.py`**: Hauptstartpunkt der Anwendung. Diese Datei erstellt das Hauptfenster und verbindet alle Module.

2. **`gui/`**:
   - **`main_window.py`**: Hier ist die Hauptlogik für das GUI-Setup. Diese Datei verwaltet das Fenster, die Menüleisten und die zentralen Funktionen wie „Ordner auswählen“ und „Analyse starten“.
   - **`file_selector.py`**: Stellt Funktionen zur Auswahl der Dateien oder Ordner bereit und verwaltet die Benutzerinteraktion zum Auswählen von Verzeichnissen.

3. **`analysis/`**:
   - **`sentiment_analyzer.py`**: Enthält die Klassen und Methoden zur Durchführung der Sentimentanalyse (z. B. `SentimentAnalyzer`). Die Datei lädt die AFINN-Lexika und enthält Methoden zur Berechnung des Sentiments.
   - **`language_detector.py`**: Verwaltung der Sprachenerkennung und Zuweisung der Kommentare. Falls ein Kommentar nicht als Deutsch oder Englisch identifiziert werden kann, wird er in eine separate Datei geschrieben.
   - **`r_visualization.py`**: Stellt Funktionen für die statistische Analyse und Visualisierung mit R zur Verfügung. Hier werden die R-Bibliotheken und ggplot2 genutzt, um Diagramme zu generieren und in einem definierten Ausgabeordner zu speichern.

4. **`utils/`**:
   - **`file_manager.py`**: Enthält Funktionen zum Verwalten der Dateien und Verzeichnisse, z. B. zum Laden und Speichern von CSV-Dateien oder zum Erstellen der benötigten Ausgabeordner.
   - **`constants.py`**: Speichert globale Konstanten wie Standardpfade, Dateinamenskonventionen und andere wiederverwendbare Konstanten.


 
### Funktionalität der Software:
1. Beim Starten der Desktop-Anwendung wird der Benutzer professionell und respektvoll willkommen geheißen. Es wird eine kurze Einführung gegeben, die die verfügbaren Optionen und deren jeweilige Resultate beschreibt.
2. Der Benutzer kann über einen Button einen oder mehrere Ordner auswählen, in denen sich die zu analysierenden Dateien befinden. Eine Mehrfachauswahl (Strg + Klick) sollte möglich sein.
3. Die gewählten Ordner und ihre Unterordner werden durch die Python-Skripte verarbeitet. Der Inhalt umfasst verschiedene Spalten, darunter Fragen und Bewertungen von Studierenden.
4. Die Anwendung analysiert Kommentare in den Spalten mithilfe der **AFINN-Bibliothek** und kategorisiert sie in Englisch und Deutsch als positiv, neutral oder negativ. Die Ergebnisse werden je Sprache in separate Textdateien ausgegeben.
5. Kommentare in anderen Sprachen werden in eine separate Datei namens »Nicht zuordenbare Kommentare« geschrieben.
6. Die sortierten Kommentare werden in einer statistischen Analyse zusammengefasst. Grafische Auswertungen werden in Form eines Kreisdiagramms, Balkendiagramms und weiterer sinnvoller Diagramme erstellt. Diese werden in festen Positionen in einem im code intergrierten Template eingefügt.
7. Die Statistiken werden sowohl semester- und jahrweise für alle Antworten als auch für die Gesamtheit aller Jahre ausgewertet.(Erstelle ein Beispiel-Template zur Illustration.). Verwende dazu die oben genannten Technologien.
8. Die Ergebnisse und Diagramme werden schließlich in einem PDF-Format ausgegeben und automatisch geöffnet.

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

# Bereits Produzierte Probe files, welche du integrieren kannst, wie du willst
gui-probe.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow importieren

# Hauptfenster erstellen
root = tk.Tk()
root.title("Willkommen")
root.geometry("700x450")
root.configure(bg="#E8EAF6")  # Sanfte Hintergrundfarbe für professionelles Aussehen

# Stil für Widgets definieren
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#E8EAF6")
style.configure("Title.TLabel", font=("Arial", 28, "bold"), foreground="#3F51B5", background="#E8EAF6")
style.configure("Subtitle.TLabel", font=("Arial", 12), foreground="#5C6BC0", background="#E8EAF6")
style.configure("TButton", font=("Arial", 14), foreground="#FFFFFF", background="#3F51B5", padding=10)
style.map("TButton", background=[("active", "#3949AB")])  # Leichter Hover-Effekt für Button

# Container-Frame für zentrierte Ausrichtung
frame = ttk.Frame(root, padding=40, style="TFrame")
frame.pack(expand=True)

# Logo-Bereich (optional)
logo_frame = ttk.Frame(frame, style="TFrame")
logo_frame.pack(pady=(0, 20))

# Bild mit Pillow öffnen und in tkinter-kompatibles Format konvertieren
logo_image = Image.open("./logo.jpg")
logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Größe anpassen

logo = ImageTk.PhotoImage(logo_image)

# Logo anzeigen
logo_label = tk.Label(logo_frame, image=logo, bg="#E8EAF6")
logo_label.image = logo  # Referenz halten
logo_label.pack()

# Titel
title_label = ttk.Label(frame, text="Willkommen bei [Deine App]", style="Title.TLabel")
title_label.pack(pady=(0, 10))

# Untertitel
subtitle_label = ttk.Label(frame, text="Ihr zentraler Zugang zu Wissen und Ressourcen.", style="Subtitle.TLabel")
subtitle_label.pack(pady=(0, 30))

# Beschreibungstext für weiteren Kontext
description_label = ttk.Label(
    frame,
    text="Organisieren, vernetzen und entwickeln Sie sich mit unserer modernen Plattform.\nErleben Sie effiziente Zusammenarbeit und Informationsaustausch.",
    style="Subtitle.TLabel",
    wraplength=500,
    justify="center"
)
description_label.pack(pady=(0, 20))

# Start-Button
start_button = ttk.Button(frame, text="Loslegen", style="TButton")
start_button.pack(pady=(20, 0))

# Funktion für Button-Interaktion
def start_app():
    print("App gestartet")

# Button-Aktion verbinden
start_button.config(command=start_app)

# Fenster starten
root.mainloop()


Ordner.py
import tkinter as tk
from tkinter import ttk, messagebox
import os

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professioneller Ordnerbrowser")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.history = []
        self.history_index = -1

        # Aktuelles Verzeichnis
        self.current_path = os.path.expanduser("~")

        # Erstelle die GUI-Elemente
        self.create_widgets()

        # Zeige den Inhalt des aktuellen Verzeichnisses
        self.show_directory(self.current_path)

    def create_widgets(self):
        # Frame für Navigation
        nav_frame = tk.Frame(self, bg="#f0f0f0")
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Back Button
        self.back_button = tk.Button(nav_frame, text="←", command=self.go_back, state=tk.DISABLED)
        self.back_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Forward Button
        self.forward_button = tk.Button(nav_frame, text="→", command=self.go_forward, state=tk.DISABLED)
        self.forward_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Address Bar
        self.path_entry = tk.Entry(nav_frame)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        self.path_entry.bind("<Return>", self.on_enter_path)

        # Refresh Button
        self.refresh_button = tk.Button(nav_frame, text="Aktualisieren", command=self.refresh)
        self.refresh_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Main area for displaying folders and files
        self.tree = ttk.Treeview(self, columns=("Name", "Type"), selectmode="extended")
        self.tree.heading('#0', text='Name', anchor='w')
        self.tree.heading('#1', text='Typ', anchor='w')
        self.tree.column('#0', stretch=True)
        self.tree.column('#1', width=100)
        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<Double-1>", self.on_double_click)

        # Scrollbars
        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=hsb.set)

        # Button to show selected paths
        show_button = tk.Button(self, text="Auswahl anzeigen", font=("Arial", 12), command=self.show_selection, bg="#4CAF50", fg="white")
        show_button.pack(pady=10)

        # Ergebnisanzeige
        self.ergebnis_label = tk.Label(self, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.ergebnis_label.pack(pady=10)

    def show_directory(self, path):
        # Aktualisiert die Adresseingabe
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

        # Leert die Treeview
        self.tree.delete(*self.tree.get_children())

        # Holt die Inhalte des Verzeichnisses
        try:
            items = os.listdir(path)
        except PermissionError:
            messagebox.showerror("Fehler", f"Zugriff auf {path} verweigert.")
            return
        except FileNotFoundError:
            messagebox.showerror("Fehler", f"Verzeichnis {path} nicht gefunden.")
            return

        # Sortiere die Inhalte: Ordner zuerst
        items.sort()
        folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]

        # Füge die Ordner zur Treeview hinzu
        for folder in folders:
            self.tree.insert('', 'end', text=folder, values=('Ordner',))

        # Füge die Dateien zur Treeview hinzu (optional)
        # for file in files:
        #     self.tree.insert('', 'end', text=file, values=('Datei',))

        # Update current path
        self.current_path = path

        # Update navigation history
        if self.history_index == -1 or self.history[self.history_index] != path:
            self.history = self.history[:self.history_index+1]
            self.history.append(path)
            self.history_index += 1

        self.update_nav_buttons()

    def on_double_click(self, event):
        item_id = self.tree.focus()
        if not item_id:
            return
        item_text = self.tree.item(item_id, "text")
        new_path = os.path.join(self.current_path, item_text)
        if os.path.isdir(new_path):
            self.show_directory(new_path)

    def on_enter_path(self, event):
        path = self.path_entry.get()
        if os.path.isdir(path):
            self.show_directory(path)
        else:
            messagebox.showerror("Fehler", f"{path} ist kein gültiges Verzeichnis.")

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            path = self.history[self.history_index]
            self.show_directory(path)
        self.update_nav_buttons()

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            path = self.history[self.history_index]
            self.show_directory(path)
        self.update_nav_buttons()

    def update_nav_buttons(self):
        self.back_button.config(state=tk.NORMAL if self.history_index > 0 else tk.DISABLED)
        self.forward_button.config(state=tk.NORMAL if self.history_index < len(self.history) - 1 else tk.DISABLED)

    def refresh(self):
        self.show_directory(self.current_path)

    def show_selection(self):
        selected_items = self.tree.selection()
        paths = []
        for item in selected_items:
            item_text = self.tree.item(item, "text")
            path = os.path.join(self.current_path, item_text)
            if os.path.isdir(path):
                paths.append(path)
        if paths:
            ergebnis = "Ausgewählte Ordnerpfade:\n" + "\n".join(paths)
            self.ergebnis_label.config(text=ergebnis)
        else:
            self.ergebnis_label.config(text="Keine Ordner ausgewählt.")

if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()

# Hier sind die Spaltenname der jeweiligen Files
Filename: FB Freitextantworten.csv
'RLVKEY';'SEMESTER';'TYP';'STUNDEN';'CREDITS';'LV_STATUS_NR';'LV_STATUS';'KOMPONENTEN_TYP';'FRAGE_TYP';'FRAGETEXT';'OPTIONEN';'ANTWORT';'OPTIONNR';'FREITEXT'

Filename: Alle Fragebögen.csv
'SEM';'RLVKEY';'SEMESTER';'TYP';'STUNDEN';'CREDITS';'LV_STATUS_NR';'LV_STATUS';'FRAGEBOGEN_ID';'BEZEICHNUNG';'BEGINN_BEFRAGUNG';'ENDE_BEFRAGUNG';'ENDE_STELLUNGNAHME';'BEGINN_VEROEFFENTLICHUNG';'HAT_STELLUNGNAHME';'DATUM_STELLUNGNAHME';'STELLUNGNAHME';'GESAMTFRAGE';'FRAGE_KEY';'IST_GESAMTFRAGE';'FRAGETEXT';'FRAGE_TYP';'FRAGETYP_BEZEICHNUNG';'KOMPONENTEN_TYP';'KOMPONENTE_NUMMERIERUNG';'FRAGE_NUMMERIERUNG';'KEINE_ANTWORT_MOEGLICH';'FREITEXT_MOEGLICH';'SINGLE_MULTIPLE';'AUSWERTUNG';'OPTIONEN_GRUPPE_BEZ';'OPTIONEN';'ANZ_OPTIONEN';'VEROEFFENTLICHEN';'RLV_KOMPONENTEN_GESAMT';'RLV_KOMPONENTEN_UNI';'RLV_KOMPONENTEN_LEHRER';'ANZ_RUECKLAUF';'ANZ_FEEDBACK';'ANZ_ABGELEHNT';'ANZ_ABGELEHNT_ANMERKUNG';'ANZ_ANTWORT_FRAGE_GESAMT';'ANZ_ANTWORT_FRAGE';'ANZ_KEINE_ANTWORT_FRAGE';'ANZ_FREITEXT_ANTWORT';'BEANTWORTET';'KEINE_ANTWORT';'EINS';'ZWEI';'DREI';'VIER';'FUENF';'SECHS';'SIEBEN';'ACHT';'NEUN';'ZEHN';'ELF';'ZWOELF';'ANTWORT';'FREITEXT';'ANTWORT_FREITEXT';'FEEDBACK_GEWERTET';'FEEDBACK_VEROEFFENTLICHEN';'FEEDBACK_SICHTBAR';'NOTE_IN_PROZENT';'NOTE'

Filename: FB Freitextantworten.csv
'RLVKEY';'SEMESTER';'TYP';'STUNDEN';'CREDITS';'LV_STATUS_NR';'LV_STATUS';'KOMPONENTEN_TYP';'FRAGE_TYP';'FRAGETEXT';'OPTIONEN';'ANTWORT';'OPTIONNR';'FREITEXT'

Filename: Alle Fragebögen.csv
'SEM';'RLVKEY';'SEMESTER';'TYP';'STUNDEN';'CREDITS';'LV_STATUS_NR';'LV_STATUS';'FRAGEBOGEN_ID';'BEZEICHNUNG';'BEGINN_BEFRAGUNG';'ENDE_BEFRAGUNG';'ENDE_STELLUNGNAHME';'BEGINN_VEROEFFENTLICHUNG';'HAT_STELLUNGNAHME';'DATUM_STELLUNGNAHME';'STELLUNGNAHME';'GESAMTFRAGE';'FRAGE_KEY';'IST_GESAMTFRAGE';'FRAGETEXT';'FRAGE_TYP';'FRAGETYP_BEZEICHNUNG';'KOMPONENTEN_TYP';'KOMPONENTE_NUMMERIERUNG';'FRAGE_NUMMERIERUNG';'KEINE_ANTWORT_MOEGLICH';'FREITEXT_MOEGLICH';'SINGLE_MULTIPLE';'AUSWERTUNG';'OPTIONEN_GRUPPE_BEZ';'OPTIONEN';'ANZ_OPTIONEN';'VEROEFFENTLICHEN';'RLV_KOMPONENTEN_GESAMT';'RLV_KOMPONENTEN_UNI';'RLV_KOMPONENTEN_LEHRER';'ANZ_RUECKLAUF';'ANZ_FEEDBACK';'ANZ_ABGELEHNT';'ANZ_ABGELEHNT_ANMERKUNG';'ANZ_ANTWORT_FRAGE_GESAMT';'ANZ_ANTWORT_FRAGE';'ANZ_KEINE_ANTWORT_FRAGE';'ANZ_FREITEXT_ANTWORT';'BEANTWORTET';'KEINE_ANTWORT';'EINS';'ZWEI';'DREI';'VIER';'FUENF';'SECHS';'SIEBEN';'ACHT';'NEUN';'ZEHN';'ELF';'ZWOELF';'ANTWORT';'FREITEXT';'ANTWORT_FREITEXT';'FEEDBACK_GEWERTET';'FEEDBACK_VEROEFFENTLICHEN';'FEEDBACK_SICHTBAR';'NOTE_IN_PROZENT';'NOTE'


## Achte darauf, dass die Ordnerauswahl auch die csv files findet
