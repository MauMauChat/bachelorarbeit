import os
import csv
from transformers import pipeline
from langdetect import detect

# Definiere das Basisverzeichnis zum Durchsuchen
base_directory = '/home/lucy/Documents/Notes/bachelorarbeit/csv'

print("Lade Sentimentanalyse-Modelle...")
sentiment_pipeline_de = pipeline(
    "sentiment-analysis",
    model="oliverguhr/german-sentiment-bert",
    tokenizer="oliverguhr/german-sentiment-bert",
    return_all_scores=True
)
sentiment_pipeline_en = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    return_all_scores=True
)
print("Modelle geladen.")

def process_fb_freitextantworten(csv_path):
    try:
        print(f"Verarbeite Datei: {csv_path}")
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print(f"Datei {csv_path} ist leer. Datei wird übersprungen.")
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
            print(f"Erforderliche Spalten fehlen in {csv_path}: {e}. Datei wird übersprungen.")
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
                results_de = sentiment_pipeline_de(answer[:512])
                if results_de:
                    scores = {res['label']: res['score'] for res in results_de[0]}
                    sentiment_score = (scores.get('positive', 0) * 1) + (scores.get('negative', 0) * -1)
                    sentiment_label = max(scores, key=scores.get)
            elif language == 'en':
                # Sentimentanalyse auf Englisch
                results_en = sentiment_pipeline_en(answer[:512])
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

        print(f"Verarbeitung von {csv_path} abgeschlossen.")

    except Exception as e:
        print(f"Fehler beim Verarbeiten von {csv_path}: {e}")

def search_and_process(base_dir):
    # Suche nach allen relevanten CSV-Dateien
    csv_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'FB Freitextantworten.csv':
                csv_files.append(os.path.join(root, file))

    # Verarbeite jede CSV-Datei einzeln
    for csv_path in csv_files:
        process_fb_freitextantworten(csv_path)

    print("Alle Dateien wurden verarbeitet.")

if __name__ == "__main__":
    search_and_process(base_directory)

