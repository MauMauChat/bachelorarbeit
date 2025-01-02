# CSV in Diagramm verwandeln

# Benötigte Bibliotheken laden
if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

# Funktion, um CSV-Datei zu laden und für jede Zeile ein Diagramm zu erstellen
plot_csv_per_row <- function(csv_file_path, output_dir="plots") {
  # CSV-Datei laden
  data <- read.csv(csv_file_path, stringsAsFactors = FALSE)

  # Überprüfen, ob die benötigten Spalten existieren
  required_columns <- c("Fragetext", "Antwort", "Sprache", "Sentiment", "Zahlenwert")
  if (!all(required_columns %in% names(data))) {
    stop("Die CSV-Datei muss die Spalten 'Fragetext', 'Antwort', 'Sprache', 'Sentiment' und 'Zahlenwert' enthalten.")
  }

  # Ordner für Diagramme erstellen, falls nicht vorhanden
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)
  }

  # Für jede Zeile ein Diagramm erstellen
  for (i in 1:nrow(data)) {
    row <- data[i, ]
    plot <- ggplot(data.frame(x=c("Zahlenwert"), y=c(row$Zahlenwert)), aes(x=x, y=y)) +
      geom_bar(stat="identity", fill=ifelse(row$Sentiment == "positive", "green", "red"), width=0.5) +
      labs(
        title=paste("Frage:", row$Fragetext),
        subtitle=paste("Antwort:", row$Antwort, "\nSprache:", row$Sprache, "\nSentiment:", row$Sentiment),
        x="Kategorie", y="Wert"
      ) +
      theme_minimal()

    # Dateiname aus den Spalten erstellen
    sanitized_question <- gsub("[\\/:*?\"<>|]", "_", substr(row$Fragetext, 1, 30))
    sanitized_sentiment <- gsub("[\\/:*?\"<>|]", "_", row$Sentiment)
    output_file <- file.path(output_dir, paste0(sanitized_question, "_", sanitized_sentiment, ".png"))

    # Diagramm speichern
    ggsave(output_file, plot=plot, width=8, height=6)
    cat("Diagramm für Zeile", i, "gespeichert unter:", output_file, "\n")
  }
}

# Beispiel: Funktion aufrufen
# plot_csv_per_row("meine_daten.csv", "plots")
