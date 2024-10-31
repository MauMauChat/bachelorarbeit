import tkinter as tk
from tkinter import ttk, messagebox
import os

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professioneller Ordnerbrowser")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.history = []
        self.history_index = -1

        # Aktuelles Verzeichnis
        self.current_path = os.path.expanduser("~")

        # Erstelle die GUI-Elemente
        self.create_widgets()

        # Zeige den Inhalt des aktuellen Verzeichnisses
        self.show_directory(self.current_path)

    def create_widgets(self):
        # Frame für Navigation
        nav_frame = tk.Frame(self, bg="#f0f0f0")
        nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Back Button
        self.back_button = tk.Button(nav_frame, text="←", command=self.go_back, state=tk.DISABLED)
        self.back_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Forward Button
        self.forward_button = tk.Button(nav_frame, text="→", command=self.go_forward, state=tk.DISABLED)
        self.forward_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Address Bar
        self.path_entry = tk.Entry(nav_frame)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        self.path_entry.bind("<Return>", self.on_enter_path)

        # Refresh Button
        self.refresh_button = tk.Button(nav_frame, text="Aktualisieren", command=self.refresh)
        self.refresh_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Main area for displaying folders and files
        self.tree = ttk.Treeview(self, columns=("Name", "Type"), selectmode="extended")
        self.tree.heading('#0', text='Name', anchor='w')
        self.tree.heading('#1', text='Typ', anchor='w')
        self.tree.column('#0', stretch=True)
        self.tree.column('#1', width=100)
        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<Double-1>", self.on_double_click)

        # Scrollbars
        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=hsb.set)

        # Button to show selected paths
        show_button = tk.Button(self, text="Auswahl anzeigen", font=("Arial", 12), command=self.show_selection, bg="#4CAF50", fg="white")
        show_button.pack(pady=10)

        # Ergebnisanzeige
        self.ergebnis_label = tk.Label(self, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.ergebnis_label.pack(pady=10)

    def show_directory(self, path):
        # Aktualisiert die Adresseingabe
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

        # Leert die Treeview
        self.tree.delete(*self.tree.get_children())

        # Holt die Inhalte des Verzeichnisses
        try:
            items = os.listdir(path)
        except PermissionError:
            messagebox.showerror("Fehler", f"Zugriff auf {path} verweigert.")
            return
        except FileNotFoundError:
            messagebox.showerror("Fehler", f"Verzeichnis {path} nicht gefunden.")
            return

        # Sortiere die Inhalte: Ordner zuerst
        items.sort()
        folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]

        # Füge die Ordner zur Treeview hinzu
        for folder in folders:
            self.tree.insert('', 'end', text=folder, values=('Ordner',))

        # Füge die Dateien zur Treeview hinzu (optional)
        # for file in files:
        #     self.tree.insert('', 'end', text=file, values=('Datei',))

        # Update current path
        self.current_path = path

        # Update navigation history
        if self.history_index == -1 or self.history[self.history_index] != path:
            self.history = self.history[:self.history_index+1]
            self.history.append(path)
            self.history_index += 1

        self.update_nav_buttons()

    def on_double_click(self, event):
        item_id = self.tree.focus()
        if not item_id:
            return
        item_text = self.tree.item(item_id, "text")
        new_path = os.path.join(self.current_path, item_text)
        if os.path.isdir(new_path):
            self.show_directory(new_path)

    def on_enter_path(self, event):
        path = self.path_entry.get()
        if os.path.isdir(path):
            self.show_directory(path)
        else:
            messagebox.showerror("Fehler", f"{path} ist kein gültiges Verzeichnis.")

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            path = self.history[self.history_index]
            self.show_directory(path)
        self.update_nav_buttons()

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            path = self.history[self.history_index]
            self.show_directory(path)
        self.update_nav_buttons()

    def update_nav_buttons(self):
        self.back_button.config(state=tk.NORMAL if self.history_index > 0 else tk.DISABLED)
        self.forward_button.config(state=tk.NORMAL if self.history_index < len(self.history) - 1 else tk.DISABLED)

    def refresh(self):
        self.show_directory(self.current_path)

    def show_selection(self):
        selected_items = self.tree.selection()
        paths = []
        for item in selected_items:
            item_text = self.tree.item(item, "text")
            path = os.path.join(self.current_path, item_text)
            if os.path.isdir(path):
                paths.append(path)
        if paths:
            ergebnis = "Ausgewählte Ordnerpfade:\n" + "\n".join(paths)
            self.ergebnis_label.config(text=ergebnis)
        else:
            self.ergebnis_label.config(text="Keine Ordner ausgewählt.")

if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()

