import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from gui.file_selector import FileSelector
from analysis.sentiment_analyzer import SentimentAnalyzer
from analysis.report_generator import ReportGenerator
from analysis.r_visualization import RVisualization

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analyse Anwendung")
        self.root.geometry("800x600")
        self.root.configure(bg="#E8EAF6")
        self.selected_directories = []
        self.setup_gui()

    def setup_gui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#E8EAF6")
        style.configure("Title.TLabel", font=("Arial", 24, "bold"), foreground="#3F51B5", background="#E8EAF6")
        style.configure("Subtitle.TLabel", font=("Arial", 12), foreground="#5C6BC0", background="#E8EAF6")
        style.configure("TButton", font=("Arial", 12), foreground="#FFFFFF", background="#3F51B5")
        style.map("TButton", background=[("active", "#3949AB")])

        frame = ttk.Frame(self.root, padding=20, style="TFrame")
        frame.pack(expand=True)

        title_label = ttk.Label(frame, text="Willkommen zur Sentiment Analyse", style="Title.TLabel")
        title_label.pack(pady=(0, 10))

        description_label = ttk.Label(
            frame,
            text="Bitte wählen Sie die Ordner mit den CSV-Dateien aus und starten Sie die Analyse.",
            style="Subtitle.TLabel",
            wraplength=600,
            justify="center"
        )
        description_label.pack(pady=(0, 20))

        select_button = ttk.Button(frame, text="Ordner auswählen", command=self.select_folders)
        select_button.pack(pady=10)

        analyze_button = ttk.Button(frame, text="Analyse starten", command=self.start_analysis)
        analyze_button.pack(pady=10)

    def select_folders(self):
        selector = FileSelector()
        directories = selector.select_directories()
        if directories:
            self.selected_directories = directories
            messagebox.showinfo("Ordner ausgewählt", f"Sie haben {len(directories)} Ordner ausgewählt.")
        else:
            messagebox.showwarning("Keine Ordner ausgewählt", "Bitte wählen Sie mindestens einen Ordner aus.")

    def start_analysis(self):
        if not self.selected_directories:
            messagebox.showwarning("Fehler", "Keine Ordner ausgewählt.")
            return

        try:
            analyzer = SentimentAnalyzer()
            analyzer.process_directories(self.selected_directories)

            visualizer = RVisualization()
            visualizer.generate_visualizations(analyzer.results)

            report_generator = ReportGenerator()
            report_generator.generate_report(analyzer.results)

            messagebox.showinfo("Analyse abgeschlossen", "Die Sentimentanalyse wurde erfolgreich abgeschlossen.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")
