from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

class LanguageDetector:
    def detect_language(self, text):
        try:
            lang = detect(text)
            if lang in ['de', 'en']:
                return lang
            else:
                return 'unknown'
        except:
            return 'unknown'
