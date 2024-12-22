#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Modul kümmert sich um die Integration des R-Skripts.
Es führt das R-Skript aus, um auf Basis der Analyse-Ergebnisse einen Bericht zu erstellen.
"""

import os  # noqa: E402
import subprocess  # noqa: E402

def run_r_script(directory, log_output):
    """
    Führt das R-Skript im ausgewählten Arbeitsverzeichnis aus.
    
    Args:
        directory (str): Das Basisverzeichnis, in dem das R-Skript die Resultate sammelt.
        log_output (callable): Funktion, um Log-Ausgaben zu erzeugen.
    """
    # Inline comments zur Erklärung:
    # Pfad zum R-Skript annehmen: Liegt im aktuellen Arbeitsverzeichnis
    r_script_path = os.path.join(os.getcwd(), "report_generator.R")
    if not os.path.exists(r_script_path):
        log_output("R-Skript 'report_generator.R' nicht gefunden.")
        return

    # Erstelle den Ordner 'Resultate_der_Analyse' im ausgewählten Verzeichnis
    result_dir = os.path.join(directory, "Resultate_der_Analyse")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # Führe das R-Skript aus
    try:
        subprocess.run(
            ["Rscript", r_script_path, directory, result_dir],
            check=True
        )
    except subprocess.CalledProcessError as e:
        log_output(f"Fehler beim Ausführen des R-Skripts: {e}")
