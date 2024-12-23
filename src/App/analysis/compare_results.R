#!/usr/bin/env Rscript

# Funktion zum Installieren und Laden von Paketen
install_and_load <- function(packages){
  for(p in packages){
    if(!require(p, character.only = TRUE)){
      install.packages(p, dependencies = TRUE, repos = "http://cran.r-project.org")
      library(p, character.only = TRUE)
      message(paste("Paket", p, "installiert und geladen."))
    } else {
      message(paste("Paket", p, "geladen."))
    }
  }
}

# Liste der benötigten Pakete
required_packages <- c("ggplot2", "dplyr", "readr")

# Installiere und lade die Pakete
install_and_load(required_packages)

message("Alle erforderlichen Pakete sind geladen.")

# Verarbeiten von Argumenten
args <- commandArgs(trailingOnly = TRUE)

if(length(args) < 2){
  stop("Mindestens zwei Argumente werden benötigt: Pfade zu den Ergebnis-Ordnern und der Ausgabeordner.")
}

# Die letzten Argumente sind der Ausgabeordner
output_dir <- args[length(args)]
result_dirs <- args[1:(length(args)-1)]

message("Resultate-Verzeichnisse:")
print(result_dirs)
message("Ausgabe-Verzeichnis:")
print(output_dir)

# Funktion zum Einlesen der Analyseergebnisse
read_analysis <- function(dir){
  file_path <- file.path(dir, "Freitextantworten_Analyse.csv")
  if(file.exists(file_path)){
    message(paste("Lese Datei:", file_path))
    data <- read_csv(file_path, show_col_types = FALSE)
    data$Quelle <- basename(dir)  # 'Quelle' Spalte hinzufügen
    return(data)
  } else {
    warning(paste("Datei", file_path, "nicht gefunden."))
    return(NULL)
  }
}

# Alle Daten einlesen
all_data <- lapply(result_dirs, read_analysis)
all_data <- Filter(Negate(is.null), all_data)  # Entfernt NULL-Einträge

# Überprüfen, ob Daten vorhanden sind
if(length(all_data) == 0){
  stop("Keine Daten zum Vergleichen gefunden.")
}

all_data <- bind_rows(all_data)

if(nrow(all_data) == 0){
  stop("Keine Daten zum Vergleichen gefunden.")
}

message("Daten erfolgreich kombiniert.")

# Beispiel: Durchschnittliche Sentimentwerte pro Quelle
summary_data <- all_data %>%
  group_by(Quelle) %>%
  summarise(Durchschnitt_Sentiment = mean(Zahlenwert, na.rm = TRUE))

message("Zusammenfassung erstellt:")
print(summary_data)

# Diagramm erstellen
p <- ggplot(summary_data, aes(x = Quelle, y = Durchschnitt_Sentiment, fill = Quelle)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Durchschnittliches Sentiment pro Quelle",
       x = "Quelle",
       y = "Durchschnittlicher Sentimentwert") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Speichere das Diagramm
if(!dir.exists(output_dir)){
  dir.create(output_dir, recursive = TRUE)
  message(paste("Ausgabe-Verzeichnis erstellt:", output_dir))
}

output_file <- file.path(output_dir, "Durchschnitt_Sentiment.png")
ggsave(output_file, plot = p, width = 10, height = 6)
message(paste("Diagramm gespeichert als:", output_file))

# Weitere Diagramme können hier hinzugefügt werden
