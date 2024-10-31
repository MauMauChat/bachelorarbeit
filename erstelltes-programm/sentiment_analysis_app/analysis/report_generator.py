from fpdf import FPDF
import os
from datetime import datetime

class ReportGenerator:
    """
    Diese Klasse erstellt einen PDF-Bericht für die Sentimentanalyse.

    Die Klasse fasst die Ergebnisse der Sentimentanalyse in einem PDF-Dokument zusammen und fügt
    optional erstellte Diagramme als zusätzliche Seiten hinzu. Der Bericht wird in einem festgelegten
    Verzeichnis gespeichert und automatisch geöffnet.
    """

    def __init__(self):
        """
        Initialisiert den ReportGenerator und erstellt das Ausgabe- sowie das Bildverzeichnis.

        Das Ausgabe-Verzeichnis wird standardmäßig als '/home/lucy/Documents/zulöschen' definiert.
        Im Unterverzeichnis 'bilder' werden alle Bilder gespeichert, die dem Bericht hinzugefügt werden.
        """
        self.output_dir = '/home/lucy/Documents/zulöschen'
        self.image_dir = os.path.join(self.output_dir, 'bilder')
        os.makedirs(self.image_dir, exist_ok=True)

    def generate_report(self, analysis_results):
        """
        Generiert den PDF-Bericht der Sentimentanalyse und speichert ihn im Ausgabe-Verzeichnis.

        Parameter:
        analysis_results (dict): Ein verschachteltes Dictionary, das die Analyseergebnisse enthält.
            Struktur: {Sprache: {Sentiment: [Kommentare]}}.

        Diese Methode erstellt eine PDF-Datei, in der die Analyseergebnisse pro Sprache und Sentiment
        zusammengefasst sind. Optional werden Diagramme von der Analyse als zusätzliche Seiten angehängt.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Berichtskopf erstellen
        pdf.cell(200, 10, txt="Sentimentanalyse Bericht", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Erstellt am {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True, align='C')

        # Ergebnisse der Sentimentanalyse hinzufügen
        for language, sentiments in analysis_results.items():
            pdf.ln(10)
            pdf.set_font("Arial", 'B', size=14)
            pdf.cell(200, 10, txt=f"Sprache: {language.upper()}", ln=True)
            for sentiment, comments in sentiments.items():
                pdf.set_font("Arial", 'B', size=12)
                pdf.cell(200, 10, txt=f"Sentiment: {sentiment.capitalize()} ({len(comments)} Kommentare)", ln=True)
                pdf.set_font("Arial", size=12)
                for comment in comments:
                    pdf.multi_cell(0, 10, txt=f"- {comment}")
                pdf.ln(5)

        # Diagramme (PNG-Dateien) dem Bericht hinzufügen
        image_files = [f for f in os.listdir(self.image_dir) if f.endswith('.png')]
        for image_file in image_files:
            pdf.add_page()
            pdf.image(os.path.join(self.image_dir, image_file), x=10, y=20, w=190)

        # PDF speichern und öffnen
        output_path = os.path.join(self.output_dir, 'Sentimentanalyse_Bericht.pdf')
        pdf.output(output_path)
        os.system(f'xdg-open "{output_path}"')
