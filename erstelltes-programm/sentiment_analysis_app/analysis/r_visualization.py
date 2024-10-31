import os
import pandas as pd
from rpy2 import robjects
from rpy2.robjects.packages import importr
from utils.constants import OUTPUT_DIR

class RVisualization:
    def __init__(self):
        self.output_dir = os.path.join(OUTPUT_DIR, 'bilder')
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_visualizations(self, analysis_results):
        data = []
        for lang, sentiments in analysis_results.items():
            for sentiment, comments in sentiments.items():
                for _ in comments:
                    data.append({'Sprache': lang, 'Sentiment': sentiment})
        df = pd.DataFrame(data)
        robjects.globalenv['df'] = df

        grdevices = importr('grDevices')
        base = importr('base')
        ggplot2 = importr('ggplot2')

        r_script = f'''
        library(ggplot2)
        p <- ggplot(df, aes(x=Sprache, fill=Sentiment)) +
            geom_bar(position="dodge") +
            ggtitle("Sentiment Verteilung nach Sprache") +
            xlab("Sprache") +
            ylab("Anzahl der Kommentare")
        ggsave("{self.output_dir}/sentiment_verteilung.png", plot=p)
        '''
        robjects.r(r_script)
