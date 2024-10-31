import tkinter as tk
from tkinter import filedialog, messagebox

class FileSelector:
    def select_directories(self):
        root = tk.Tk()
        root.withdraw()
        directories = []

        while True:
            directory = filedialog.askdirectory(title="Ordner auswählen")
            if directory:
                directories.append(directory)
                cont = messagebox.askyesno("Weiteren Ordner auswählen", "Möchten Sie einen weiteren Ordner auswählen?")
                if not cont:
                    break
            else:
                break

        if not directories:
            messagebox.showwarning("Keine Auswahl", "Es wurden keine Ordner ausgewählt.")
            return None
        return directories
