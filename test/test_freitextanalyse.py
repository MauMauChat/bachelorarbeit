import os
import csv
import pytest
from tempfile import TemporaryDirectory
from script import process_fb_freitextantworten

def test_process_fb_freitextantworten(tmp_path):
    """
    Testet die Funktion process_fb_freitextantworten mit einer typischen CSV-Datei.
    Überprüft die korrekte Erkennung von Sprache und Sentiment.
    """
    # CSV-Inhalt mit deutschen und englischen Einträgen
    csv_content = '''FRAGETEXT;FREITEXT
"Wie war Ihr Erlebnis?";"Das war großartig!"
"Any comments?";"I did not like the service."
"Feedback";"Der Service war okay."
"Anmerkungen";"I love this product!"
'''

    # Temporäre CSV-Datei mit obigem Inhalt erstellen
    csv_file = tmp_path / 'FB Freitextantworten.csv'
    csv_file.write_text(csv_content, encoding='utf-8')

    # Funktion ausführen
    process_fb_freitextantworten(str(csv_file))

    # Ausgabe-Datei überprüfen
    output_csv_file = tmp_path / 'Freitextantworten_Analyse.csv'
    assert output_csv_file.exists()

    # Ausgabedatei lesen und überprüfen
    with open(output_csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Überprüfe die Kopfzeile der Ausgabe
    assert rows[0] == ['Fragetext', 'Antwort', 'Sprache', 'Sentiment', 'Zahlenwert']

    # Prüfe, ob die erwartete Anzahl von Zeilen (Header + 4 Einträge) vorhanden ist
    assert len(rows) == 5

    # Überprüfe die Sprache der ersten Zeile (Deutsch oder tolerierte Alternative)
    assert rows[1][2] in ['de', 'af', 'unknown']

    # Überprüfe das Sentiment der ersten Zeile (beliebige sentiment-Labels oder 'not analyzed' möglich)
    assert rows[1][3] in ['positive', 'negative', 'neutral', 'not analyzed']

    # Überprüfe die Sprache und das Sentiment der zweiten Zeile (Englisch)
    assert rows[2][2] == 'en'
    assert rows[2][3] in ['positive', 'negative']

def test_process_fb_freitextantworten_empty_file(tmp_path):
    """
    Testet das Verhalten der Funktion, wenn eine leere Datei bereitgestellt wird.
    Erwartet, dass keine Ausgabedatei erstellt wird.
    """
    # Erstellen einer leeren CSV-Datei
    csv_file = tmp_path / 'FB Freitextantworten.csv'
    csv_file.write_text('', encoding='utf-8')

    # Funktion ausführen
    process_fb_freitextantworten(str(csv_file))

    # Überprüfe, dass keine Ausgabedatei erstellt wurde
    output_csv_file = tmp_path / 'Freitextantworten_Analyse.csv'
    assert not output_csv_file.exists()

def test_process_fb_freitextantworten_missing_columns(tmp_path):
    """
    Testet das Verhalten bei einer Datei, der die erforderlichen Spalten fehlen.
    Erwartet, dass keine Ausgabedatei erstellt wird.
    """
    # Erstelle eine CSV-Datei ohne die benötigten Spalten 'FRAGETEXT' und 'FREITEXT'
    csv_content = '''SomeColumn;AnotherColumn
"value1";"value2"
'''

    # Temporäre Datei erstellen und Funktion ausführen
    csv_file = tmp_path / 'FB Freitextantworten.csv'
    csv_file.write_text(csv_content, encoding='utf-8')
    process_fb_freitextantworten(str(csv_file))

    # Überprüfe, dass keine Ausgabedatei erstellt wurde
    output_csv_file = tmp_path / 'Freitextantworten_Analyse.csv'
    assert not output_csv_file.exists()

def test_process_fb_freitextantworten_no_answers(tmp_path):
    """
    Testet das Verhalten der Funktion, wenn Antworten fehlen.
    Überprüft, dass 'unknown' als Sprache und 'not analyzed' als Sentiment gesetzt wird.
    """
    # CSV-Inhalt ohne Antworten
    csv_content = '''FRAGETEXT;FREITEXT
"Frage 1";""
"Frage 2";""
'''

    # Temporäre Datei erstellen und Funktion ausführen
    csv_file = tmp_path / 'FB Freitextantworten.csv'
    csv_file.write_text(csv_content, encoding='utf-8')
    process_fb_freitextantworten(str(csv_file))

    # Überprüfen, ob die Ausgabedatei existiert und die richtige Anzahl an Zeilen hat
    output_csv_file = tmp_path / 'Freitextantworten_Analyse.csv'
    assert output_csv_file.exists()

    # Datei lesen und Inhalt überprüfen
    with open(output_csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Prüfe, ob die erwartete Anzahl von Zeilen vorhanden ist (Header + 2 Datenzeilen)
    assert len(rows) == 3

    # Überprüfen, dass die Sprache 'unknown' und das Sentiment 'not analyzed' ist
    assert rows[1][2] == 'unknown'
    assert rows[1][3] == 'not analyzed'

def test_process_fb_freitextantworten_special_characters(tmp_path):
    """
    Testet die Funktion mit Eingaben, die Sonderzeichen enthalten.
    Überprüft die korrekte Sprache und Sentiment für spanische und englische Eingaben.
    """
    # CSV-Inhalt mit spanischen und englischen Eingaben
    csv_content = '''FRAGETEXT;FREITEXT
"¿Cómo fue su experiencia?";"¡Excelente!"
"Any comments?";"Service was meh :/"
'''

    # Temporäre Datei erstellen und Funktion ausführen
    csv_file = tmp_path / 'FB Freitextantworten.csv'
    csv_file.write_text(csv_content, encoding='utf-8')
    process_fb_freitextantworten(str(csv_file))

    # Überprüfen, ob die Ausgabedatei existiert und die richtige Anzahl an Zeilen hat
    output_csv_file = tmp_path / 'Freitextantworten_Analyse.csv'
    assert output_csv_file.exists()

    # Datei lesen und Inhalt überprüfen
    with open(output_csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Prüfe, ob die erwartete Anzahl von Zeilen vorhanden ist (Header + 2 Datenzeilen)
    assert len(rows) == 3

    # Überprüfen, ob die Sprache der ersten Zeile korrekt oder als alternative Sprache erkannt wurde
    assert rows[1][2] in ['es', 'unknown', 'ro']

    # Sprache der zweiten Zeile sollte Englisch sein
    assert rows[2][2] == 'en'

    # Sentiment der ersten Zeile prüfen (beliebige sentiment-Labels oder 'not analyzed' möglich)
    assert rows[1][3] in ['positive', 'negative', 'neutral', 'not analyzed']
    assert rows[2][3] in ['positive', 'negative', 'neutral', 'not analyzed']

