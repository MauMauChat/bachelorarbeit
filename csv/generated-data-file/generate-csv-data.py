import os
import csv
import random

# Spaltennamen aus deiner Beschreibung
columns = [
    'RLVKEY', 'SEMESTER', 'TYP', 'STUNDEN', 'CREDITS', 'LV_STATUS_NR',
    'LV_STATUS', 'KOMPONENTEN_TYP', 'FRAGE_TYP', 'FRAGETEXT', 'OPTIONEN',
    'ANTWORT', 'OPTIONNR', 'FREITEXT'
]

# Basisverzeichnis für die Ordner und CSV-Dateien
base_directory = '/home/lucy/Documents/Notes/bachelorarbeit/csv/generated-data-file'

# Beispielwerte für zufällige Einträge in die CSV
sample_data = {
    'RLVKEY': ['277f6a00a09fc6d', 'a53e6669754588d', '959353896063576', '757aeb0f3e66c44', 'ca76fca5fb653f5', '974e077c94dfc81'],
    'SEMESTER': ['16S', '17S', '18W', '19S', '20W'],
    'TYP': ['VO', 'UE', 'PS', 'VC'],
    'STUNDEN': [1.0, 2.0],
    'CREDITS': [1.0, 2.0, 3.0, 5.0],
    'LV_STATUS_NR': ['50'],
    'LV_STATUS': ['genehmigt'],
    'KOMPONENTEN_TYP': ['Uni'],
    'FRAGE_TYP': ['FREITEXT'],
    'OPTIONEN': ['n/a'],
    'OPTIONNR': ['-2', '-1'],
    'FREITEXT': ['', 'sehr interessante Themen', 'sympathischer LV-Leiter', 'auf Studierende eingegangen', 'gut strukturierte LV']
}

# Liste für zufällige Werte in der Spalte ANTWORT
answer_sentiments = ['positiv', 'neutral', 'negativ', '']

# Generiert zufällige Daten für die CSV-Dateien
def generate_random_row():
    row = {col: random.choice(values) if values else '' for col, values in sample_data.items()}
    return row

# Funktion zur Generierung und Speicherung der CSV-Dateien in Ordnern
def create_csv_files_with_data():
    for i in range(1, 4):
        # Erstelle Ordner
        folder_path = os.path.join(base_directory, f'Ordner_{i}')
        os.makedirs(folder_path, exist_ok=True)
        
        # CSV-Dateipfad
        csv_file_path = os.path.join(folder_path, f'FB Freitextantworten.csv')
        
        # CSV-Datei mit 100 Zeilen und zufälligen Daten erstellen
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
            writer.writeheader()
            
            for j in range(1, 1010):
                row = generate_random_row()
                
                # Fülle Fragetext und Antwort spezifisch
                row['FRAGETEXT'] = f'Das ist der Fragetext {j}'
                row['ANTWORT'] = random.choice(answer_sentiments)
                
                # Schreibe Zeile in CSV
                writer.writerow(row)
        
        print(f'CSV-Datei erstellt: {csv_file_path}')

if __name__ == "__main__":
    create_csv_files_with_data()

