#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Modul enthält die Klasse FileSelector, 
welche für das Auswählen von Dateien oder Ordnern über eine GUI verantwortlich ist.
"""

import os  # noqa: E402  # für Pfad- und OS-Operationen
from tkinter import filedialog, messagebox  # noqa: E402  # für GUI-Dialogs

class FileSelector:
    """
    Eine Klasse, die eine grafische Oberfläche zum Auswählen von Verzeichnissen bereitstellt.
    """
    def select_directories(self):
        """
        Öffnet einen Dialog, um Verzeichnisse auszuwählen.

        Returns:
            list oder None: Eine Liste ausgewählter Verzeichnispfade. 
                            Wenn keine Verzeichnisse ausgewählt wurden, wird None zurückgegeben.
        """
        # Inline comments zur Erklärung:
        # directories wird eine Liste aller ausgewählten Ordner sein
        directories = []
        while True:
            # Öffnet einen Dialog zur Auswahl eines Ordners
            directory = filedialog.askdirectory(
                initialdir=os.path.expanduser('~/Documents/bachelorarbeit/src/App/test_data'),
                title="Ordner auswählen"
            )
            # Wenn ein Verzeichnis ausgewählt wurde, hänge es an die Liste an
            if directory:
                directories.append(directory)
                # Frage den Benutzer, ob noch ein weiterer Ordner ausgewählt werden soll
                cont = messagebox.askyesno("Weiteren Ordner auswählen", "Möchten Sie einen weiteren Ordner auswählen?")
                if not cont:
                    # Wenn nicht, beende die Schleife
                    break
            else:
                # Keine Auswahl getroffen, beende die Schleife
                break

        # Wenn keine Verzeichnisse ausgewählt wurden, zeige eine Warnung an
        if not directories:
            messagebox.showwarning("Keine Auswahl", "Es wurden keine Ordner ausgewählt.")
            return None
        return directories
