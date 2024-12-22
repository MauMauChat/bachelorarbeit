#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Modul enthält die Klasse ComparisonManager, 
welche für das Vergleichen von Sentimentanalyse-Ergebnissen und die Erstellung von Diagrammen verantwortlich ist.
"""

import os  # noqa: E402
import subprocess  # noqa: E402
from tkinter import filedialog, messagebox  # noqa: E402

class ComparisonManager:
    """
    Klasse zur Verwaltung des Vergleichs von Sentimentanalyse-Ergebnissen.
    """
    def __init__(self, log_output):
        """
        Initialisiert den ComparisonManager mit einer Logging-Funktion.
        
        Args:
            log_output (callable): Funktion, um Log-Ausgaben zu erzeugen.
        """
        self.log_output = log_output

    def select_result_folders(self):
        """
        Öffnet einen Dialog zur Auswahl der Ergebnis-Ordner.
        
        Returns:
            list oder None: Eine Liste ausgewählter Ergebnis-Ordnerpfade oder None, wenn keine Auswahl getroffen wurde.
        """
        folders = filedialog.askdirectory(
            initialdir=os.path.expanduser('~/Documents/bachelorarbeit/src/App'),
            title="Ergebnis-Ordner für den Vergleich auswählen"
        )
        if folders:
            return [folders]
        else:
            messagebox.showwarning("Keine Auswahl", "Es wurden keine Ordner ausgewählt.")
            return None

    def compare_results(self, selected_folders):
        """
        Führt das R-Skript zur Erstellung der Vergleichsdiagramme aus.
        
        Args:
            selected_folders (list): Liste der ausgewählten Ergebnis-Ordnerpfade.
        """
        try:
            self.log_output("Starte den Vergleich der ausgewählten Ergebnisse...")
            # Pfad zum R-Skript annehmen: Liegt im aktuellen Arbeitsverzeichnis
            r_script_path = os.path.join(os.getcwd(), "compare_results.R")
            if not os.path.exists(r_script_path):
                self.log_output("R-Skript 'compare_results.R' nicht gefunden.")
                messagebox.showerror("Fehler", "R-Skript 'compare_results.R' nicht gefunden.")
                return

            # Erstelle den Ordner 'Vergleichsergebnisse' im Hauptverzeichnis
            main_dir = os.path.commonpath(selected_folders)
            comparison_dir = os.path.join(main_dir, "Vergleichsergebnisse")
            if not os.path.exists(comparison_dir):
                os.makedirs(comparison_dir)

            # Führe das R-Skript aus und übergebe die ausgewählten Ordner sowie den Ausgabeordner
            subprocess.run(
                ["Rscript", r_script_path, *selected_folders, comparison_dir],
                check=True
            )
            self.log_output("Vergleichsdiagramme wurden erfolgreich erstellt und in 'Vergleichsergebnisse' gespeichert.")
            messagebox.showinfo("Vergleich abgeschlossen", "Die Vergleichsdiagramme wurden erfolgreich erstellt.")
        except subprocess.CalledProcessError as e:
            self.log_output(f"Fehler beim Ausführen des R-Skripts: {e}")
            messagebox.showerror("Fehler", f"Fehler beim Ausführen des R-Skripts: {e}")
        except Exception as e:
            self.log_output(f"Unerwarteter Fehler: {e}")
            messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")
