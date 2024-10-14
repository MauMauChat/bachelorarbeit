# Bachelorarbeit

Dies ist deine Bachelorarbeit.

## Projektstruktur

- `src/`: Quellcode der Python Anwendung
- `tex/`: LaTeX-Dateien für das schriftliche Dokument
- `build/`: Erzeugte LaTeX-PDFs
- `docs/`: Dokumentation erstellt mit pdoc

## Installation

1. Abhängigkeiten installieren:
```bash
poetry install
```

2. Kompiliere das LaTeX-Dokument:
```bash
./compile.sh
```

3. Erstelle die Python-Dokumentation:
```bash
poetry run pdoc --html --output-dir docs src/bachelorarbeit
```

## Anforderungen
- Poetry
- LaTeX
- latexmk
- pdoc
