#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dieses Modul enthält die Klasse SentimentAnalyzer, 
welche für die Sentimentanalyse der gefundenen CSV-Dateien verantwortlich ist.
"""

import os   # noqa: E402 # für Pfad- und OS-Operationen
import csv  # noqa: E402 # zum Lesen und Schreiben von CSV-Dateien
from langdetect import detect  # noqa: E402  # Spracherkennung
from transformers import pipeline  # noqa: E402  # für die Sentimentanalyse-Modelle

class SentimentAnalyzer:
    """
    Klasse zur Durchführung der Sentimentanalyse.
    """
    def __init__(self, progress_callback):
        """
        Initialisiert die Modelle und speichert den Callback für Fortschrittsmeldungen.

        Args:
            progress_callback (callable): Eine Funktion, um Fortschrittsmeldungen auszugeben.
        """
        # Inline comments zur Erklärung:
        self.progress_callback = progress_callback
        # Lade deutsche Sentimentanalyse
        self.progress_callback("Lade Sentimentanalyse-Modelle...", 0)
        self.sentiment_pipeline_de = pipeline(
            "sentiment-analysis",
            model="oliverguhr/german-sentiment-bert",
            tokenizer="oliverguhr/german-sentiment-bert",
            return_all_scores=True
        )
        # Lade englische Sentimentanalyse
        self.sentiment_pipeline_en = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            return_all_scores=True
        )
        self.progress_callback("Modelle geladen.", 0)

    def count_csv_files(self, base_dir):
        """
        Zählt die Anzahl der zu verarbeitenden CSV-Dateien im Verzeichnis.

        Args:
            base_dir (str): Basisverzeichnis.

        Returns:
            int: Anzahl der relevanten CSV-Dateien.
        """
        # Inline comments zur Erklärung:
        # Wir suchen nach 'FB Freitextantworten.csv'
        csv_files = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file == 'FB Freitextantworten.csv':
                    csv_files.append(os.path.join(root, file))
        return len(csv_files)

    def process_fb_freitextantworten(self, csv_path):
        """
        Verarbeitet eine einzelne CSV-Datei mit Freitextantworten.

        Args:
            csv_path (str): Pfad zur CSV-Datei.
        """
        # Inline comments zur Erklärung:
        try:
            self.progress_callback(f"Verarbeite Datei: {csv_path}", 0)
            with open(csv_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if not lines:
                self.progress_callback(f"Datei {csv_path} ist leer. Datei wird übersprungen.", 0)
                return

            # Kopfzeile einlesen
            header = lines[0].strip()
            header_cols = header.split(';')
            header_cols = [col.strip('"').strip("'") for col in header_cols]

            # Indizes ermitteln
            try:
                frage_index = header_cols.index('FRAGETEXT')
                antwort_index = header_cols.index('FREITEXT')
            except ValueError as e:
                self.progress_callback(f"Erforderliche Spalten fehlen in {csv_path}: {e}. Datei wird übersprungen.", 0)
                return

            data_lines = lines[1:]
            results = []

            for line_num, line in enumerate(data_lines, start=2):
                line = line.strip()
                cols = line.split(';')
                # Falls Spalten fehlen, ergänzen wir leere Strings
                while len(cols) < len(header_cols):
                    cols.append('')

                question = cols[frage_index].strip('"').strip("'")
                answer = cols[antwort_index].strip('"').strip("'")

                # Sprache erkennen
                language = 'unknown'
                if answer.strip():
                    try:
                        language = detect(answer)
                    except:
                        pass

                # Defaultwerte für Sentiment
                sentiment_label = 'not analyzed'
                sentiment_score = ''

                if language == 'de':
                    # Deutsche Sentimentanalyse
                    results_de = self.sentiment_pipeline_de(answer[:512])
                    if results_de:
                        scores = {res['label']: res['score'] for res in results_de[0]}
                        sentiment_score = (scores.get('positive', 0) * 1) + (scores.get('negative', 0) * -1)
                        sentiment_label = max(scores, key=scores.get)
                elif language == 'en':
                    # Englische Sentimentanalyse
                    results_en = self.sentiment_pipeline_en(answer[:512])
                    if results_en:
                        scores = {res['label'].lower(): res['score'] for res in results_en[0]}
                        sentiment_score = (scores.get('positive', 0) * 1) + (scores.get('negative', 0) * -1)
                        sentiment_label = max(scores, key=scores.get)

                results.append([question, answer, language, sentiment_label, sentiment_score])

            # Ergebnisse schreiben
            output_dir = os.path.dirname(csv_path)
            output_csv_path = os.path.join(output_dir, 'Freitextantworten_Analyse.csv')
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
        """
        Durchsucht das Basisverzeichnis nach relevanten CSV-Dateien und verarbeitet diese.

        Args:
            base_dir (str): Basisverzeichnis.
        """
        # Inline comments zur Erklärung:
        # Suche nach allen relevanten CSV-Dateien
        csv_files = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file == 'FB Freitextantworten.csv':
                    csv_files.append(os.path.join(root, file))

        # Verarbeite jede gefundene CSV-Datei
        for csv_path in csv_files:
            self.process_fb_freitextantworten(csv_path)
