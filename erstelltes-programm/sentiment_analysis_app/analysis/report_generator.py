from fpdf import FPDF
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.output_dir = '/home/lucy/Documents/zulöschen'
        self.image_dir = os.path.join(self.output_dir, 'bilder')
        os.makedirs(self.image_dir, exist_ok=True)

    def generate_report(self, analysis_results):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Sentimentanalyse Bericht", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Erstellt am {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True, align='C')

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

        # Diagramme hinzufügen
        image_files = [f for f in os.listdir(self.image_dir) if f.endswith('.png')]
        for image_file in image_files:
            pdf.add_page()
            pdf.image(os.path.join(self.image_dir, image_file), x=10, y=20, w=190)

        output_path = os.path.join(self.output_dir, 'Sentimentanalyse_Bericht.pdf')
        pdf.output(output_path)
        os.system(f'xdg-open "{output_path}"')
