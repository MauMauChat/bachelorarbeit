import pandas as pd

class FileManager:
    def load_csv(self, filepath):
        try:
            df = pd.read_csv(filepath, sep=';', encoding='utf-8', error_bad_lines=False, warn_bad_lines=False)
            return df
        except Exception as e:
            print(f"Fehler beim Laden der Datei {filepath}: {e}")
            return None
