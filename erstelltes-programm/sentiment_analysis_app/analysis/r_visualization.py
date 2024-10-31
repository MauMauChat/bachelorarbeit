import os
import pandas as pd
from rpy2 import robjects
from rpy2.robjects.packages import importr
from utils.constants import OUTPUT_DIR

class RVisualization:
    """
    Diese Klasse generiert Visualisierungen für die Sentimentanalyse.

    Die Klasse verwendet R und ggplot2, um eine grafische Darstellung der
    Verteilung von Sentiments pro Sprache zu erstellen und diese als Bilddatei zu speichern.
    """

    def __init__(self):
        """
        Initialisiert die Klasse und erstellt das Ausgabe-Verzeichnis für die Bilder.

        Das Verzeichnis wird in einem Unterordner namens 'bilder' unterhalb des
        standardmäßig definierten OUTPUT_DIR erstellt, falls es noch nicht existiert.
        """
        self.output_dir = os.path.join(OUTPUT_DIR, 'bilder')
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_visualizations(self, analysis_results):
        """
        Generiert die Visualisierung der Sentimentanalyse-Ergebnisse.

        Parameter:
        analysis_results (dict): Ein verschachteltes Dictionary mit Sprach- und Sentiment-Daten.
            Der Aufbau ist {Sprache: {Sentiment: [Kommentare]}}.

        Diese Methode wandelt die Ergebnisse der Analyse in ein DataFrame-Format um,
        welches ggplot2 in R für die Visualisierung verwenden kann. Sie erstellt ein
        Balkendiagramm zur Verteilung der Sentiments pro Sprache und speichert es als PNG-Bild.
        """
        data = []

        # Wandelt die Analyseergebnisse in eine flache Liste von Dictionaries für das DataFrame um
        for lang, sentiments in analysis_results.items():
            for sentiment, comments in sentiments.items():
                for _ in comments:
                    data.append({'Sprache': lang, 'Sentiment': sentiment})
        df = pd.DataFrame(data)

        # Übergibt das DataFrame an die R-Umgebung
        robjects.globalenv['df'] = df

        # Importiert R-Bibliotheken für das Plotten und Dateihandling
        grdevices = importr('grDevices')
        base = importr('base')
        ggplot2 = importr('ggplot2')

        # R-Skript zur Erstellung und Speicherung des Plots
        r_script = f'''
        library(ggplot2)
        p <- ggplot(df, aes(x=Sprache, fill=Sentiment)) +
            geom_bar(position="dodge") +
            ggtitle("Sentiment Verteilung nach Sprache") +
            xlab("Sprache") +
            ylab("Anzahl der Kommentare")
        ggsave("{self.output_dir}/sentiment_verteilung.png", plot=p)
        '''

        # Führt das R-Skript aus
        robjects.r(r_script)