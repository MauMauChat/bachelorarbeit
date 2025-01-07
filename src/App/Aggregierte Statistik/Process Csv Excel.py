import pandas as pd
import os
import re


# Funktion zum Anpassen der Zeilenumbrüche
def preprocess_csv_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Ersetze Zeilenumbrüche durch Leerzeichen, außer wenn sie nach ';' oder neben '\'' stehen
        pattern = re.compile(
            r"(?<!;[A-Za-z0-9\s\(\)\[\]\{\}])(?<!')\n(?!')"  # dein existierendes Muster
            r"|"
            r"((\.)\s*\n\s*)"
            r"|"
            r"(?<=')\s*\n\s*(?=[A-Za-z])"
            r"|"
            r"(?<=[A-Za-z\(\)])\s*\n\s*(?=')"
            r"|"
            r"((?<=[A-Za-z])\s*\n\s*)"
        )
        processed_content = pattern.sub(" ", content)

        # Schreibe den angepassten Inhalt zurück
        temp_file_path = file_path + '_processed.csv'
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write(processed_content)

        return temp_file_path
    except Exception as e:
        print(f"Fehler beim Verarbeiten der Datei {file_path}: {e}")
        return None


# Liste der CSV-Dateien
csv_files = [
    r'C:\Users\claud\Desktop\Bachelor_Arbeit\Test_datei3.csv'
]

# Ausgabe-Excel-Datei
output_excel_file = r'C:\Users\claud\Desktop\Bachelor_Arbeit\zusammengefuegte_daten.xlsx'

with pd.ExcelWriter(output_excel_file, engine='openpyxl') as writer:
    for csv_file in csv_files:
        try:
            sheet_name = os.path.splitext(os.path.basename(csv_file))[0]

            # Vorverarbeiten der Datei
            processed_file = preprocess_csv_content(csv_file)
            if not processed_file:
                print(f"Die Datei {csv_file} konnte nicht verarbeitet werden.")
                continue

            try:
                # CSV-Datei einlesen
                df = pd.read_csv(
                    processed_file,
                    sep=r'(?<![A-Za-z\s\.&]);(?![A-Za-z\s\(\)\[\]\{\}&])',  # Regex als Trenner
                    engine='python',
                    encoding='utf-8'
                )
            except pd.errors.ParserError as e:
                # ParserError abfangen und fehlerhafte Zeile ausgeben
                print(f"ParserError beim Einlesen der Datei {csv_file}:\n{e}")

                # Versuchen, die Zeilennummer aus der Fehlermeldung zu extrahieren
                match = re.search(r'line (\d+)', str(e))
                if match:
                    error_line_no = int(match.group(1))
                    print(f"Fehler in Zeile: {error_line_no}")

                    # Jetzt die entsprechende Zeile ausgeben
                    with open(processed_file, 'r', encoding='utf-8') as f_in:
                        for i, line in enumerate(f_in, start=1):
                            if i == error_line_no:
                                print("Fehlerhafte Zeile lautet:")
                                print(line.rstrip("\n"))
                                break

                # Falls du den Skriptlauf hier abbrechen willst, kannst du erneut raisen:
                # raise e
                # Oder du ignorierst den Fehler, dann geht es einfach weiter mit dem nächsten CSV.
                continue

            # Wenn kein ParserError, DataFrame in Excel schreiben
            if df.empty:
                print(f"Die Datei {csv_file} enthält keine gültigen Daten und wird übersprungen.")
            else:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Temporäre Datei entfernen
            os.remove(processed_file)

        except Exception as e:
            print(f"Allgemeiner Fehler beim Verarbeiten der Datei {csv_file}: {e}")

    # Überprüfen, ob mindestens ein Blatt vorhanden ist
    if len(writer.book.sheetnames) == 0:
        raise ValueError("Keine gültigen Daten gefunden. Die Excel-Datei enthält keine Tabellenblätter.")

print(f"Die Excel-Datei wurde erfolgreich erstellt: {output_excel_file}")
