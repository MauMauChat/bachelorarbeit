import os
import pandas as pd
from afinn import Afinn
from analysis.language_detector import LanguageDetector
from utils.file_manager import FileManager

class SentimentAnalyzer:
    def __init__(self):
        self.afinn_de = Afinn(language='de')
        self.afinn_en = Afinn(language='en')
        self.language_detector = LanguageDetector()
        self.file_manager = FileManager()
        self.results = {}

    def process_directories(self, directories):
        for directory in directories:
            self.process_directory(directory)

    def process_directory(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.csv'):
                    filepath = os.path.join(root, file)
                    self.process_file(filepath)

    def process_file(self, filepath):
        df = self.file_manager.load_csv(filepath)
        if df is not None and 'FREITEXT' in df.columns:
            comments = df['FREITEXT'].dropna()
            for comment in comments:
                self.analyze_comment(comment)
        else:
            print(f"Keine gültigen Daten in {filepath}")

    def analyze_comment(self, comment):
        language = self.language_detector.detect_language(comment)
        if language in ['de', 'en']:
            afinn = self.afinn_de if language == 'de' else self.afinn_en
            score = afinn.score(comment)
            sentiment = self.get_sentiment_category(score)
            self.save_comment(comment, sentiment, language)
        else:
            self.save_unassigned_comment(comment)

    def get_sentiment_category(self, score):
        if score > 0:
            return 'positiv'
        elif score < 0:
            return 'negativ'
        else:
            return 'neutral'

    def save_comment(self, comment, sentiment, language):
        if language not in self.results:
            self.results[language] = {'positiv': [], 'neutral': [], 'negativ': []}
        self.results[language][sentiment].append(comment)

    def save_unassigned_comment(self, comment):
        if 'unassigned' not in self.results:
            self.results['unassigned'] = []
        self.results['unassigned'].append(comment)
