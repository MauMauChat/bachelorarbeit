# Dieses R-Skript vergleicht Sentimentanalyse-Ergebnisse aus mehreren Ordnern
# und erstellt Diagramme zur Visualisierung der Veränderungen.

args <- commandArgs(trailingOnly = TRUE)

if(length(args) < 2){
  stop("Mindestens zwei Argumente werden benötigt: Pfade zu den Ergebnis-Ordnern und der Ausgabeordner.")
}

# Die letzten Argumente sind die Ausgabeordner
output_dir <- args[length(args)]
result_dirs <- args[1:(length(args)-1)]

library(ggplot2)
library(dplyr)
library(readr)

# Funktion zum Einlesen der Analyseergebnisse
read_analysis <- function(dir){
  file_path <- file.path(dir, "Freitextantworten_Analyse.csv")
  if(file.exists(file_path)){
    data <- read_csv(file_path, show_col_types = FALSE)
    data <- basename(dir)  # Quelle hinzufügen
    return(data)
  } else {
    warning(paste("Datei", file_path, "nicht gefunden."))
    return(NULL)
  }
}

# Alle Daten einlesen
all_data <- lapply(result_dirs, read_analysis)
all_data <- bind_rows(all_data, .id = "Quelle")

# Überprüfen, ob Daten vorhanden sind
if(nrow(all_data) == 0){
  stop("Keine Daten zum Vergleichen gefunden.")
}

# Beispiel: Durchschnittliche Sentimentwerte pro Quelle
summary_data <- all_data %>%
  group_by(Quelle) %>%
  summarise(Durchschnitt_Sentiment = mean(Zahlenwert, na.rm = TRUE))

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
}

output_file <- file.path(output_dir, "Durchschnitt_Sentiment.png")
ggsave(output_file, plot = p, width = 10, height = 6)

# Weitere Diagramme können hier hinzugefügt werden
