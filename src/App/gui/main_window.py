#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Modul enthält die Hauptfenster-Klasse der GUI-Anwendung.
Es bindet den FileSelector, startet die Analyse und steuert die GUI-Elemente.
"""

import os  # noqa: E402  # für Pfad-Operationen
import sys
from pathlib import Path
import threading  # noqa: E402  # für parallele Ausführung der Analyse
import tkinter as tk  # noqa: E402  # GUI-Bibliothek
from tkinter import ttk, messagebox  # noqa: E402
# Bestimme das Basisverzeichnis dynamisch
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

# Füge src dem Python-Pfad hinzu
sys.path.append(str(SRC_DIR))
from src.App.gui.file_selector import FileSelector  # noqa: E402  # Import der Dateiauswahl-Klasse
from src.App.analysis.sentiment_analyzer import SentimentAnalyzer  # noqa: E402  # Import der Analyseklasse
from src.App.analysis.report_generator import run_r_script  # noqa: E402  # Import der Funktion zum R-Skript-Run
from src.App.analysis.comparison import ComparisonManager  # noqa: E402  # Import der Vergleichsmanager-Klasse

class MainWindow:
    """
    Hauptklasse für die GUI der Sentiment-Analyse-Anwendung.
    """
    def __init__(self, root):
        """
        Initialisiert das Hauptfenster der Anwendung.

        Args:
            root (tk.Tk): Das Haupt-Tkinter-Fensterobjekt.
        """
        # Inline comments zur Erklärung:
        self.root = root  # Hauptfenster-Referenz
        self.root.title("Sentiment Analyse Anwendung")  # Setzt Fenstertitel
        self.root.geometry("800x600")  # Setzt Fenstergröße
        self.root.configure(bg="#E8EAF6")  # Hintergrundfarbe
        self.selected_directories = []  # Liste der ausgewählten Ordner
        self.setup_gui()  # Erzeugt die GUI-Elemente

    def setup_gui(self):
        """
        Erstellt die grafische Benutzeroberfläche für die Anwendung.
        """
        # Inline comments zur Erklärung:
        # Konfiguriere Styles für Widgets
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#E8EAF6")
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), foreground="#3F51B5", background="#E8EAF6")
        style.configure("Subtitle.TLabel", font=("Arial", 12), foreground="#5C6BC0", background="#E8EAF6")
        style.configure("TButton", font=("Arial", 12), foreground="#FFFFFF", background="#3F51B5")
        style.map("TButton", background=[("active", "#3949AB")])

        # Haupt-Frame erstellen
        frame = ttk.Frame(self.root, padding=20, style="TFrame")
        frame.pack(expand=True, fill=tk.BOTH)  # Frame anpassen

        # Titel-Label
        title_label = ttk.Label(frame, text="Willkommen zur Sentiment Analyse", style="Title.TLabel")
        title_label.pack(pady=(0, 10))

        # Beschreibungs-Label
        description_label = ttk.Label(
            frame,
            text="Bitte wählen Sie die Ordner mit den CSV-Dateien aus und starten Sie die Analyse.",
            style="Subtitle.TLabel",
            wraplength=600,
            justify="center"
        )
        description_label.pack(pady=(0, 20))

        # Button zum Ordner auswählen
        select_button = ttk.Button(frame, text="Ordner auswählen", command=self.select_folders)
        select_button.pack(pady=10)

        # Button zum Analyse starten
        analyze_button = ttk.Button(frame, text="Analyse starten", command=self.start_analysis)
        analyze_button.pack(pady=10)

        # Neuer Button zum Vergleich starten
        compare_button = ttk.Button(frame, text="Vergleich starten", command=self.start_comparison)
        compare_button.pack(pady=10)

        # **Neuer Button für den Entwicklungsmodus**
        dev_mode_button = ttk.Button(frame, text="Entwicklungsmodus: Testdaten verwenden", command=self.run_dev_mode)
        dev_mode_button.pack(pady=10)
        # **Ende des neuen Buttons**

        # Fortschrittsbalke iener freund in auf winfow gjet firse klasse niht weikes ptbleme mit dem dateooafbbsadfsdasdn
        self.progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='determinate')
        self.progress_bar.pack(pady=20, fill=tk.X)

        # Textfeld für Ausgaben
        self.output_text = tk.Text(frame, height=10, wrap='word')
        self.output_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def select_folders(self):
        """
        Öffnet einen Dialog zur Auswahl der Verzeichnisse und speichert die Auswahl.
        """
        # Inline comments zur Erklärung:
        # Erzeuge ein FileSelector-Objekt
        selector = FileSelector()
        # Starte den Auswahl-Dialog
        directories = selector.select_directories()
        if directories:
            # Wenn Verzeichnisse ausgewählt wurden, speichere sie
            self.selected_directories = directories
            messagebox.showinfo("Ordner ausgewählt", f"Sie haben {len(directories)} Ordner ausgewählt.")
        else:
            # Keine Verzeichnisse ausgewählt
            messagebox.showwarning("Keine Ordner ausgewählt", "Bitte wählen Sie mindestens einen Ordner aus.")

    def start_analysis(self):
        """
        Startet die Sentimentanalyse für die ausgewählten Verzeichnisse.
        """
        # Inline comments zur Erklärung:
        # Prüfe, ob Ordner ausgewählt wurden
        if not self.selected_directories:
            messagebox.showwarning("Fehler", "Keine Ordner ausgewählt.")
            return

        # Starte die Analyse in einem separaten Thread, um GUI nicht zu blockieren
        threading.Thread(target=self.run_analysis).start()

    def run_dev_mode(self):
        """
        Führt die Analyse automatisch mit vordefinierten Testdaten aus.
        Dieser Button ist nur für die Entwicklungsumgebung gedacht.
        """
        # **Neuer Code für den Entwicklungsmodus**
        test_directories = [
            "/home/lucy/Documents/bachelorarbeit/src/App/test_data/Jahr_4",
            "/home/lucy/Documents/bachelorarbeit/src/App/test_data/Jahr_5"
        ]
        self.selected_directories = test_directories
        self.log_output("Entwicklungsmodus aktiviert. Verwende Testdaten aus Jahr_4 und Jahr_5.")
        # Starte die Analyse in einem separaten Thread
        threading.Thread(target=self.run_analysis).start()
        ## **Ende des neuen Codes**



    def run_analysis(self):
        """
        Führt die Analyse aus und aktualisiert die GUI entsprechend.
        """
        # Inline comments zur Erklärung:
        try:
            # Setze Fortschrittsbalken zurück
            self.progress_bar['value'] = 0
            self.log_output("Lade Sentimentanalyse-Modelle...")

            # Erzeuge ein SentimentAnalyzer-Objekt
            analyzer = SentimentAnalyzer(self.progress_callback)

            # Zähle alle zu verarbeitenden Dateien
            total_files = 0
            for directory in self.selected_directories:
                total_files += analyzer.count_csv_files(directory)

            if total_files == 0:
                # Wenn keine Dateien vorhanden sind
                self.log_output("Keine zu verarbeitenden Dateien gefunden.")
                return

            self.progress_bar['maximum'] = total_files

            # Verarbeite alle ausgewählten Verzeichnisse
            for directory in self.selected_directories:
                analyzer.search_and_process(directory)

            # Nach der Analyse wird das R-Skript ausgeführt
            self.log_output("Generiere den Bericht mit R...")
            root_directory = os.path.commonpath(self.selected_directories)
            run_r_script(root_directory, self.log_output)
            self.log_output("Bericht wurde erstellt und in 'Resultate_der_Analyse' gespeichert.")

            self.log_output("Alle Dateien wurden verarbeitet.")
            messagebox.showinfo("Analyse abgeschlossen", "Die Sentimentanalyse wurde erfolgreich abgeschlossen.")
        except Exception as e:
            self.log_output(f"Fehler: {e}")
            messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")

    def start_comparison(self):
        """
        Startet den Vergleich der Sentimentanalyse-Ergebnisse.
        """
        # Inline comments zur Erklärung:
        try:
            # Erzeuge ein ComparisonManager-Objekt mit der Logging-Funktion
            comparator = ComparisonManager(self.log_output)
            # Öffne den Dialog zur Auswahl der Ergebnis-Ordner
            selected_folders = FileSelector().select_directories()
            if selected_folders:
                # Starte den Vergleich in einem separaten Thread, um GUI nicht zu blockieren
                threading.Thread(target=comparator.compare_results, args=(selected_folders,)).start()
        except Exception as e:
            self.log_output(f"Fehler beim Starten des Vergleichs: {e}")
            messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")

    def log_output(self, message):
        """
        Gibt eine Nachricht im Textfeld aus.

        Args:
            message (str): Nachricht, die im Ausgabe-Textfeld angezeigt wird.
        """
        # Inline comments zur Erklärung:
        self.output_text.insert(tk.END, message + '\n')
        self.output_text.see(tk.END)

    def progress_callback(self, message, increment=1):
        """
        Callback-Funktion, um den Fortschritt zu aktualisieren.

        Args:
            message (str): Auszugebende Nachricht
            increment (int): Fortschrittswert, um den der Balken erhöht wird
        """
        # Inline comments zur Erklärung:
        # Nutzung von after, um GUI-Updates thread-sicher durchzuführen
        self.root.after(0, self.update_progress, increment)
        self.root.after(0, self.log_output, message)

    def update_progress(self, increment):
        """
        Aktualisiert den Fortschrittsbalken.

        Args:
            increment (int): Wert, um den der Fortschritt erhöht wird.
        """
        # Inline comments zur Erklärung:
        self.progress_bar['value'] += increment
