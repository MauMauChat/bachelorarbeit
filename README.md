Ja, das ist möglich! Du kannst den absoluten Pfad zu deinem Projekt dynamisch mit `pwd` in **Linux/macOS** und mit `(Get-Location).Path` in **Windows PowerShell** einfügen. Dadurch müssen Nutzer den Pfad nicht manuell eingeben. Das macht die Einrichtung noch einfacher.

Hier ist eine überarbeitete Version der **README.md**, die `pwd` und `(Get-Location).Path` verwendet.

---

## README.md

```markdown
# Bachelorarbeit-Projekt: Automatische Installation und Einrichtung

Diese Anleitung beschreibt, wie du das Projekt auf **macOS**, **Windows (PowerShell)** und **Linux** einrichtest. Kopiere einfach die Befehle aus den Codeblöcken in dein Terminal, und das Skript erledigt den Rest!

---

## Voraussetzungen

1. **Python 3.10 oder höher** muss installiert sein.
2. **Pip** (Python-Paketmanager) ist erforderlich.
3. Für Linux/macOS: Ein Terminal mit Bash.
4. Für Windows: PowerShell.

---

## Automatische Einrichtung

### 1. Virtuelle Umgebung erstellen

#### Linux/macOS

```bash
# Setze den aktuellen Pfad (Projektverzeichnis) dynamisch
cd "$(pwd)"

# Erstelle eine virtuelle Umgebung (.venv)
python3 -m venv .venv

# Aktiviere die virtuelle Umgebung
source .venv/bin/activate

# Prüfe, ob die Umgebung aktiv ist
echo "Virtuelle Umgebung aktiv: $(which python)"
```

#### Windows (PowerShell)

```powershell
# Setze den aktuellen Pfad (Projektverzeichnis) dynamisch
cd (Get-Location).Path

# Erstelle eine virtuelle Umgebung (.venv)
python -m venv .venv

# Aktiviere die virtuelle Umgebung
.\.venv\Scripts\Activate

# Prüfe, ob die Umgebung aktiv ist
Write-Output "Virtuelle Umgebung aktiv: $((Get-Command python).Source)"
```

---

### 2. Abhängigkeiten installieren

#### Linux/macOS

```bash
# Stelle sicher, dass die virtuelle Umgebung aktiv ist
source .venv/bin/activate

# Installiere alle Abhängigkeiten aus requirements.txt
pip install -r requirements.txt

# Optional: Aktualisiere pip auf die neueste Version
pip install --upgrade pip
```

#### Windows (PowerShell)

```powershell
# Stelle sicher, dass die virtuelle Umgebung aktiv ist
.\.venv\Scripts\Activate

# Installiere alle Abhängigkeiten aus requirements.txt
pip install -r requirements.txt

# Optional: Aktualisiere pip auf die neueste Version
pip install --upgrade pip
```

---

### 3. Einrichtung abschließen

#### Linux/macOS

```bash
# Führe erste Tests aus, um sicherzustellen, dass alles korrekt installiert ist
python main.py

# Zeige die installierten Pakete an (optional)
pip list
```

#### Windows (PowerShell)

```powershell
# Führe erste Tests aus, um sicherzustellen, dass alles korrekt installiert ist
python main.py

# Zeige die installierten Pakete an (optional)
pip list
```

---

## Projektstruktur

Das Projekt hat die folgende Struktur:

```
.
├── docs/                       # Dokumentation des Projekts
├── LV-Feedback-Daten/          # Rohdaten für die Sentiment-Analyse
├── src/                        # Hauptverzeichnis des Codes
│   ├── App/                    # Enthält die Kernmodule der Anwendung
│   ├── test_data/              # Beispiel- und Testdatensätze
│   └── utils/                  # Hilfsmodule (Logger, Fortschritt)
├── requirements.txt            # Abhängigkeiten des Projekts
├── pyproject.toml              # Build-Informationen
├── main.py                     # Einstiegspunkt des Projekts
└── README.md                   # Diese Anleitung
```

---

## Fehlerbehebung

### 1. Fehler: "Befehl nicht gefunden"
- **Linux/macOS:** Stelle sicher, dass Python 3 installiert ist und verwende `python3` anstelle von `python`.
- **Windows:** Stelle sicher, dass Python korrekt in den Umgebungsvariablen (`PATH`) konfiguriert ist.

### 2. Fehler: `pip` ist nicht installiert
- **Linux/macOS:** Installiere `pip` mit:
  ```bash
  sudo apt-get install python3-pip  # Für Debian-basierte Systeme
  brew install python               # Für macOS mit Homebrew
  ```
- **Windows:** Lade den Python-Installer von [python.org](https://www.python.org/downloads/) herunter und installiere Python erneut. Achte darauf, die Option "Add Python to PATH" auszuwählen.

---

## Optional: Pakete dokumentieren

Falls du später alle verwendeten Pakete dokumentieren möchtest, kannst du eine neue `requirements.txt` erstellen:

#### Linux/macOS/Windows

```bash
# Erstelle oder aktualisiere requirements.txt
pip freeze > requirements.txt
```

---

## Support

Bei Fragen oder Problemen kontaktiere mich über [GitHub Issues](https://github.com/MauMauChat). Viel Erfolg mit deinem Projekt! 🚀
```

---

### Vorteile der Anpassung mit `pwd` und `(Get-Location).Path`:

1. **Dynamischer Pfad:** Der aktuelle Pfad wird automatisch gesetzt, ohne dass Nutzer ihn manuell anpassen müssen.
2. **Kompaktere Anleitung:** Keine Platzhalter wie `/path/to/project` notwendig.
3. **Einheitliche Befehle für alle Plattformen:** Macht die README universeller.

Wenn noch etwas fehlt oder angepasst werden soll, lass es mich wissen! 😊