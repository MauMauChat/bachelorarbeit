import tkinter as tk
from tkinter import filedialog, messagebox

class FileSelector:
    """
    A class to open a graphical interface for selecting one or more directories using tkinter.
    """

    def select_directories(self):
        """
        Opens a dialog for the user to select directories and confirm selections.

        Returns:
            list or None: A list of selected directory paths. If no directories are selected,
                          returns None and shows a warning message.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
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
