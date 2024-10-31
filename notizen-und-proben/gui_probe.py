import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow importieren

# Hauptfenster erstellen
root = tk.Tk()
root.title("Willkommen")
root.geometry("700x450")
root.configure(bg="#E8EAF6")  # Sanfte Hintergrundfarbe für professionelles Aussehen

# Stil für Widgets definieren
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#E8EAF6")
style.configure("Title.TLabel", font=("Arial", 28, "bold"), foreground="#3F51B5", background="#E8EAF6")
style.configure("Subtitle.TLabel", font=("Arial", 12), foreground="#5C6BC0", background="#E8EAF6")
style.configure("TButton", font=("Arial", 14), foreground="#FFFFFF", background="#3F51B5", padding=10)
style.map("TButton", background=[("active", "#3949AB")])  # Leichter Hover-Effekt für Button

# Container-Frame für zentrierte Ausrichtung
frame = ttk.Frame(root, padding=40, style="TFrame")
frame.pack(expand=True)

# Logo-Bereich (optional)
logo_frame = ttk.Frame(frame, style="TFrame")
logo_frame.pack(pady=(0, 20))

# Bild mit Pillow öffnen und in tkinter-kompatibles Format konvertieren
logo_image = Image.open("./logo.jpg")
logo_image = logo_image.resize((100, 100), Image.LANCZOS)  # Größe anpassen

logo = ImageTk.PhotoImage(logo_image)

# Logo anzeigen
logo_label = tk.Label(logo_frame, image=logo, bg="#E8EAF6")
logo_label.image = logo  # Referenz halten
logo_label.pack()

# Titel
title_label = ttk.Label(frame, text="Willkommen bei [Deine App]", style="Title.TLabel")
title_label.pack(pady=(0, 10))

# Untertitel
subtitle_label = ttk.Label(frame, text="Ihr zentraler Zugang zu Wissen und Ressourcen.", style="Subtitle.TLabel")
subtitle_label.pack(pady=(0, 30))

# Beschreibungstext für weiteren Kontext
description_label = ttk.Label(
    frame,
    text="Organisieren, vernetzen und entwickeln Sie sich mit unserer modernen Plattform.\nErleben Sie effiziente Zusammenarbeit und Informationsaustausch.",
    style="Subtitle.TLabel",
    wraplength=500,
    justify="center"
)
description_label.pack(pady=(0, 20))

# Start-Button
start_button = ttk.Button(frame, text="Loslegen", style="TButton")
start_button.pack(pady=(20, 0))

# Funktion für Button-Interaktion
def start_app():
    print("App gestartet")

# Button-Aktion verbinden
start_button.config(command=start_app)

# Fenster starten
root.mainloop()

