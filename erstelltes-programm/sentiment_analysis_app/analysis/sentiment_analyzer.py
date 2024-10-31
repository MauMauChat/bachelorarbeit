import os
import pandas as pd
from afinn import Afinn
from analysis.language_detector import LanguageDetector
from utils.file_manager import FileManager

class SentimentAnalyzer:
    """
    A class to analyze sentiment from CSV files containing free-text comments in various languages.
    """

    def __init__(self):
        """
        Initializes the SentimentAnalyzer with language-specific Afinn sentiment analyzers and other
        utility instances such as a language detector and file manager.
        """
        self.afinn_de = Afinn(language='de')
        self.afinn_en = Afinn(language='en')
        self.language_detector = LanguageDetector()
        self.file_manager = FileManager()
        self.results = {}

    def process_directories(self, directories):
        """
        Processes multiple directories, analyzing all CSV files within each.

        Args:
            directories (list): A list of directory paths to scan for CSV files.
        """
        for directory in directories:
            self.process_directory(directory)

    def process_directory(self, directory):
        """
        Processes a single directory, analyzing all CSV files within.

        Args:
            directory (str): The directory path to scan for CSV files.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.csv'):
                    filepath = os.path.join(root, file)
                    self.process_file(filepath)

    def process_file(self, filepath):
        """
        Loads a CSV file and analyzes each comment in the 'FREITEXT' column if present.

        Args:
            filepath (str): The file path of the CSV file to process.
        """
        df = self.file_manager.load_csv(filepath)
        if df is not None and 'FREITEXT' in df.columns:
            comments = df['FREITEXT'].dropna()
            for comment in comments:
                self.analyze_comment(comment)
        else:
            print(f"Keine gültigen Daten in {filepath}")

    def analyze_comment(self, comment):
        """
        Analyzes a single comment, determining its language, sentiment, and categorizing it.

        Args:
            comment (str): The text comment to be analyzed.
        """
        language = self.language_detector.detect_language(comment)
        if language in ['de', 'en']:
            afinn = self.afinn_de if language == 'de' else self.afinn_en
            score = afinn.score(comment)
            sentiment = self.get_sentiment_category(score)
            self.save_comment(comment, sentiment, language)
        else:
            self.save_unassigned_comment(comment)

    def get_sentiment_category(self, score):
        """
        Categorizes the sentiment score as 'positiv', 'neutral', or 'negativ'.

        Args:
            score (float): The sentiment score of the comment.

        Returns:
            str: The sentiment category based on the score.
        """
        if score > 0:
            return 'positiv'
        elif score < 0:
            return 'negativ'
        else:
            return 'neutral'

    def save_comment(self, comment, sentiment, language):
        """
        Saves a comment in the results dictionary under its language and sentiment category.

        Args:
            comment (str): The text comment to save.
            sentiment (str): The sentiment category ('positiv', 'neutral', or 'negativ').
            language (str): The language code of the comment ('de' or 'en').
        """
        if language not in self.results:
            self.results[language] = {'positiv': [], 'neutral': [], 'negativ': []}
        self.results[language][sentiment].append(comment)

    def save_unassigned_comment(self, comment):
        """
        Saves a comment that couldn't be categorized by language in an 'unassigned' category.

        Args:
            comment (str): The text comment to save.
        """
        if 'unassigned' not in self.results:
            self.results['unassigned'] = []
        self.results['unassigned'].append(comment)