import sys
import tkinter as tk
from gui.main_window import MainWindow

def main():
    """
    Hauptfunktion zur Initialisierung und Ausführung der GUI-Anwendung.

    Diese Funktion erstellt eine Instanz des Tkinter-Hauptfensters und
    initialisiert die Hauptfenster-Klasse der Anwendung. Die Funktion startet
    die Ereignisschleife der GUI und fängt unerwartete Fehler ab, die während
    der Laufzeit auftreten könnten.

    Bei Auftreten eines Fehlers wird eine Fehlermeldung ausgegeben und das
    Programm mit Statuscode 1 beendet.
    """
    try:
        # Erstellen des Hauptfensters der Anwendung
        root = tk.Tk()

        # Initialisieren der Hauptfenster-Klasse der Anwendung
        app = MainWindow(root)

        # Starten der Tkinter-Ereignisschleife
        root.mainloop()

    except Exception as e:
        # Fehlerbehandlung: Ausgabe einer Fehlermeldung und Beendigung des Programms
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Einstiegspunkt: Startet die main()-Funktion, wenn das Skript direkt ausgeführt wird
    main()
