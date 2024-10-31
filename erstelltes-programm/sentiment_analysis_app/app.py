import sys
import tkinter as tk
from gui.main_window import MainWindow

def main():
    try:
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
