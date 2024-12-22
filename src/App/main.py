#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Skript ist der Einstiegspunkt für die Anwendung.
Es initialisiert die GUI, lädt die entsprechenden Klassen und startet den Tkinter-Eventloop.
"""

import sys  # noqa: E402  # import systemmodule um sys.exit() zu verwenden
import os   # noqa: E402  # import os für Pfad- und OS-Operationen
import tkinter as tk  # noqa: E402  # import tkinter für GUI
from tkinter import messagebox  # noqa: E402  # zusätzliche GUI-Komponente
from gui.main_window import MainWindow  # noqa: E402  # import der Hauptfenster-Klasse
# Keine direkte Nutzung von file_selector hier, da main_window sie intern lädt
from analysis.sentiment_analyzer import SentimentAnalyzer  # noqa: E402  # Import der Sentimentanalyse-Klasse
from analysis.report_generator import run_r_script  # noqa: E402  # Import der R-Skript-Funktion

def main():
    """
    Hauptfunktion, die die GUI initialisiert und ausführt.
    
    Returns:
        None
    """
    # Inline comments zur Erklärung:
    # Erstelle das Hauptfenster-Objekt
    root = tk.Tk()  # Erzeugt das Tk-Hauptfenster
    # Erzeuge eine MainWindow-Instanz und übergebe root
    #app
    MainWindow(root)  # Initialisiert die Haupt-GUI-Klasse
    # Starte den Tkinter-Ereignisschleife, um auf Benutzerinteraktionen zu warten
    root.mainloop()  # Wartet auf GUI-Events

if __name__ == '__main__':
    try:
        main()  # Starte die Hauptfunktion
    except Exception as e:
        # Fehlerbehandlung
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        print("Das ist alles gut")
        sys.exit(1)
