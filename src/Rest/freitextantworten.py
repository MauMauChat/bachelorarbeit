import sys
import os
import csv
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from langdetect import detect
from transformers import pipeline

class FileSelector:
    """
    Eine Klasse, die eine grafische Oberfläche zum Auswählen von Verzeichnissen bereitstellt.
    """
    def select_directories(self):
        """
        Öffnet einen Dialog, um Verzeichnisse auszuwählen.

        Rückgabe:
            list oder None: Eine Liste ausgewählter Verzeichnispfade. Wenn keine Verzeichnisse ausgewählt wurden,
                            wird None zurückgegeben und eine Warnmeldung angezeigt.
        """
        directories = []
        while True:
            directory = filedialog.askdirectory(initialdir=os.path.expanduser('~/Documents/bachelorarbeit'), title="Ordner auswählen")
            if directory:
                directories.append(directory)
                cont = messagebox.askyesno("Weiteren Ordner auswählen", "Möchten Sie einen weiteren Ordner auswählen?")
                if not cont:
                    break
            else:
                break

        if not directories:
            messagebox.showwarning("Keine Auswahl", "Es wurden keine Ordner ausgewählt.")
            return None
        return directories

class MainWindow:
    """
    Hauptklasse für die GUI der Sentiment-Analyse-Anwendung.
    """
    def __init__(self, root):
        """
        Initialisiert das Hauptfenster der Anwendung.
        """
        self.root = root
        self.root.title("Sentiment Analyse Anwendung")
        self.root.geometry("800x600")
        self.root.configure(bg="#E8EAF6")
        self.selected_directories = []  # Liste der vom Benutzer ausgewählten Verzeichnisse
        self.setup_gui()

    def setup_gui(self):
        """
        Erstellt die grafische Benutzeroberfläche für die Anwendung.
        """
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#E8EAF6")
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), foreground="#3F51B5", background="#E8EAF6")
        style.configure("Subtitle.TLabel", font=("Arial", 12), foreground="#5C6BC0", background="#E8EAF6")
        style.configure("TButton", font=("Arial", 12), foreground="#FFFFFF", background="#3F51B5")
        style.map("TButton", background=[("active", "#3949AB")])

        frame = ttk.Frame(self.root, padding=20, style="TFrame")
        frame.pack(expand=True, fill=tk.BOTH)

        title_label = ttk.Label(frame, text="Willkommen zur Sentiment Analyse", style="Title.TLabel")
        title_label.pack(pady=(0, 10))

        description_label = ttk.Label(
            frame,
            text="Bitte wählen Sie die Ordner mit den CSV-Dateien aus und starten Sie die Analyse.",
            style="Subtitle.TLabel",
            wraplength=600,
            justify="center"
        )
        description_label.pack(pady=(0, 20))

        select_button = ttk.Button(frame, text="Ordner auswählen", command=self.select_folders)
        select_button.pack(pady=10)

        analyze_button = ttk.Button(frame, text="Analyse starten", command=self.start_analysis)
        analyze_button.pack(pady=10)

        # Fortschrittsbalken hinzufügen
        self.progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='determinate')
        self.progress_bar.pack(pady=20, fill=tk.X)

        # Textfeld für Ausgaben hinzufügen
        self.output_text = tk.Text(frame, height=10, wrap='word')
        self.output_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def select_folders(self):
        """
        Öffnet einen Dialog zur Auswahl der Verzeichnisse und speichert die Auswahl.
        """
        selector = FileSelector()
        directories = selector.select_directories()
        if directories:
            self.selected_directories = directories
            messagebox.showinfo("Ordner ausgewählt", f"Sie haben {len(directories)} Ordner ausgewählt.")
        else:
            messagebox.showwarning("Keine Ordner ausgewählt", "Bitte wählen Sie mindestens einen Ordner aus.")

    def start_analysis(self):
        """
        Startet die Sentimentanalyse für die ausgewählten Verzeichnisse.
        """
        if not self.selected_directories:
            messagebox.showwarning("Fehler", "Keine Ordner ausgewählt.")
            return

        # Analyse in separatem Thread starten
        threading.Thread(target=self.run_analysis).start()

    def run_analysis(self):
        """
        Führt die Analyse aus und aktualisiert die GUI entsprechend.
        """
        try:
            # Fortschrittsbalken zurücksetzen
            self.update_progress(0)
            self.log_output("Lade Sentimentanalyse-Modelle...")
            analyzer = SentimentAnalyzer(self.progress_callback)

            total_files = 0
            for directory in self.selected_directories:
                total_files += analyzer.count_csv_files(directory)

            if total_files == 0:
                self.log_output("Keine zu verarbeitenden Dateien gefunden.")
                return

            self.progress_bar['maximum'] = total_files

            for directory in self.selected_directories:
                analyzer.search_and_process(directory)

            self.log_output("Alle Dateien wurden verarbeitet.")
            messagebox.showinfo("Analyse abgeschlossen", "Die Sentimentanalyse wurde erfolgreich abgeschlossen.")
        except Exception as e:
            self.log_output(f"Fehler: {e}")
            messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")

    def progress_callback(self, message, increment=1):
        """
        Callback-Funktion, um den Fortschritt zu aktualisieren.
        """
        self.root.after(0, self.update_progress, increment)
        self.root.after(0, self.log_output, message)

    def update_progress(self, increment):
        """
        Aktualisiert den Fortschrittsbalken.
        """
        self.progress_bar['value'] += increment

    def log_output(self, message):
        """
        Gibt eine Nachricht im Textfeld aus.
        """
        self.output_text.insert(tk.END, message + '\n')
        self.output_text.see(tk.END)

class SentimentAnalyzer:
    """
    Klasse zur Durchführung der Sentimentanalyse.
    """
    def __init__(self, progress_callback):
        self.progress_callback = progress_callback
        self.progress_callback("Lade Sentimentanalyse-Modelle...", 0)
        self.sentiment_pipeline_de = pipeline(
            "sentiment-analysis",
            model="oliverguhr/german-sentiment-bert",
            tokenizer="oliverguhr/german-sentiment-bert",
            return_all_scores=True
        )
        self.sentiment_pipeline_en = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            return_all_scores=True
        )
        self.progress_callback("Modelle geladen.", 0)

    def count_csv_files(self, base_dir):
        """
        Zählt die Anzahl der zu verarbeitenden CSV-Dateien.
        """
        csv_files = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file == 'FB Freitextantworten.csv':
                    csv_files.append(os.path.join(root, file))
        return len(csv_files)

    def process_fb_freitextantworten(self, csv_path):
        try:
            self.progress_callback(f"Verarbeite Datei: {csv_path}", 0)
            with open(csv_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if not lines:
                self.progress_callback(f"Datei {csv_path} ist leer. Datei wird übersprungen.", 0)
                return

            # Kopfzeile einlesen und Spalten bestimmen
            header = lines[0].strip()
            header_cols = header.split(';')
            header_cols = [col.strip('"').strip("'") for col in header_cols]

            # Bestimme die Indizes der gewünschten Spalten
            try:
                frage_index = header_cols.index('FRAGETEXT')
                antwort_index = header_cols.index('FREITEXT')
            except ValueError as e:
                self.progress_callback(f"Erforderliche Spalten fehlen in {csv_path}: {e}. Datei wird übersprungen.", 0)
                return

            # Entferne die Kopfzeile aus den Daten
            data_lines = lines[1:]

            results = []

            for line_num, line in enumerate(data_lines, start=2):
                line = line.strip()
                cols = line.split(';')

                # Korrigiere die Anzahl der Spalten, falls notwendig
                while len(cols) < len(header_cols):
                    cols.append('')

                # Extrahiere die gewünschten Werte
                question = cols[frage_index].strip('"').strip("'")
                answer = cols[antwort_index].strip('"').strip("'")

                # Sprache der Antwort erkennen, nur wenn Antwort vorhanden ist
                language = 'unknown'
                if answer.strip():
                    try:
                        language = detect(answer)
                    except:
                        pass

                sentiment_label = 'not analyzed'
                sentiment_score = ''

                if language == 'de':
                    # Sentimentanalyse auf Deutsch
                    results_de = self.sentiment_pipeline_de(answer[:512])
                    if results_de:
                        scores = {res['label']: res['score'] for res in results_de[0]}
                        sentiment_score = (scores.get('positive', 0) * 1) + (scores.get('negative', 0) * -1)
                        sentiment_label = max(scores, key=scores.get)
                elif language == 'en':
                    # Sentimentanalyse auf Englisch
                    results_en = self.sentiment_pipeline_en(answer[:512])
                    if results_en:
                        scores = {res['label'].lower(): res['score'] for res in results_en[0]}
                        sentiment_score = (scores.get('positive', 0) * 1) + (scores.get('negative', 0) * -1)
                        sentiment_label = max(scores, key=scores.get)

                results.append([question, answer, language, sentiment_label, sentiment_score])

            # Ergebnisse in eine CSV-Datei schreiben
            output_dir = os.path.dirname(csv_path)
            output_csv_path = os.path.join(output_dir, 'Freitextantworten_Analyse.csv')

            # Wenn die Ausgabedatei bereits existiert, löschen, um zu überschreiben
            if os.path.exists(output_csv_path):
                os.remove(output_csv_path)

            with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Fragetext', 'Antwort', 'Sprache', 'Sentiment', 'Zahlenwert'])
                writer.writerows(results)

            self.progress_callback(f"Verarbeitung von {csv_path} abgeschlossen.", 1)

        except Exception as e:
            self.progress_callback(f"Fehler beim Verarbeiten von {csv_path}: {e}", 0)

    def search_and_process(self, base_dir):
        # Suche nach allen relevanten CSV-Dateien
        csv_files = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file == 'FB Freitextantworten.csv':
                    csv_files.append(os.path.join(root, file))

        # Verarbeite jede CSV-Datei einzeln
        for csv_path in csv_files:
            self.process_fb_freitextantworten(csv_path)

def main():
    """
    Hauptfunktion zur Initialisierung und Ausführung der GUI-Anwendung.
    """
    try:
        # Erstellen des Hauptfensters der Anwendung
        root = tk.Tk()

        # Initialisieren der Hauptfenster-Klasse der Anwendung
        app = MainWindow(root)

        # Starten der Tkinter-Ereignisschleife
        root.mainloop()

    except Exception as e:
        # Fehlerbehandlung: Ausgabe einer Fehlermeldung und Beendigung des Programms
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        print("Das ist alles gut")
        sys.exit(1)

if __name__ == '__main__':
    main()
