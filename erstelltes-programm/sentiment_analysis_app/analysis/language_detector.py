from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

class LanguageDetector:
    """
    A class to detect the language of a given text, with support for German and English.
    """

    def detect_language(self, text):
        """
        Detects the language of the provided text.

        Args:
            text (str): The text for which to detect the language.

        Returns:
            str: The detected language code ('de' for German, 'en' for English), or 'unknown'
                 if the language is not supported or if detection fails.
        """
        try:
            lang = detect(text)
            if lang in ['de', 'en']:
                return lang
            else:
                return 'unknown'
        except:
            return 'unknown'
