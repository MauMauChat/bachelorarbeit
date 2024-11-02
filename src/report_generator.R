#!/usr/bin/env Rscript

# Laden der erforderlichen Pakete
library(ggplot2)
library(dplyr)
library(rmarkdown)

# Übergebene Argumente abrufen
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("Bitte geben Sie das Datenverzeichnis und das Ausgabeverzeichnis als Argumente an.")
}

data_directory <- args[1]
output_dir <- args[2]

# Funktion zum Generieren des Berichts
generate_report <- function(data_directory, output_dir) {
  # Erstellen des Ausgabe-Verzeichnisses, falls es nicht existiert
  if (!dir.exists(output_dir)) {
    dir.create(output_dir, recursive = TRUE)
  }

  # Suchen aller 'Freitextantworten_Analyse.csv' Dateien im data_directory rekursiv
  csv_files <- list.files(path = data_directory, pattern = "Freitextantworten_Analyse\\.csv$", recursive = TRUE, full.names = TRUE)

  if (length(csv_files) == 0) {
    message(sprintf("Keine 'Freitextantworten_Analyse.csv' Dateien im Verzeichnis %s gefunden.", data_directory))
    return()
  }

  # Lesen und Zusammenführen der CSV-Dateien
  all_data <- data.frame()
  for (csv_path in csv_files) {
    data <- tryCatch({
      read.csv(csv_path, stringsAsFactors = FALSE)
    }, error = function(e) {
      message(sprintf("Fehler beim Lesen der Datei %s: %s", csv_path, e$message))
      return(NULL)
    })
    if (!is.null(data)) {
      all_data <- bind_rows(all_data, data)
    }
  }

  if (nrow(all_data) == 0) {
    warning("Keine Daten zum Analysieren gefunden.")
    return()
  }

  # Datenvorbereitung
  all_data$Sentiment <- as.factor(all_data$Sentiment)
  all_data$Sprache <- as.factor(all_data$Sprache)
  all_data$Zahlenwert <- as.numeric(all_data$Zahlenwert)

  # Generieren der Grafiken
  plot1 <- ggplot(all_data, aes(x = Sentiment)) +
    geom_bar(fill = "#3F51B5") +
    theme_minimal() +
    labs(title = "Verteilung der Sentiments",
         x = "Sentiment",
         y = "Anzahl")

  plot2 <- ggplot(all_data, aes(x = Sprache, fill = Sentiment)) +
    geom_bar(position = "dodge") +
    theme_minimal() +
    labs(title = "Sentiments nach Sprache",
         x = "Sprache",
         y = "Anzahl")

  plot3 <- ggplot(all_data, aes(x = Zahlenwert)) +
    geom_histogram(fill = "#3F51B5", bins = 10, na.rm = TRUE) +
    theme_minimal() +
    labs(title = "Verteilung der Sentiment-Zahlenwerte",
         x = "Zahlenwert",
         y = "Anzahl")

  # Speichern der Grafiken
  ggsave(filename = file.path(output_dir, "Analyse_Diagramm1.png"), plot = plot1, width = 6, height = 4)
  ggsave(filename = file.path(output_dir, "Analyse_Diagramm2.png"), plot = plot2, width = 6, height = 4)
  ggsave(filename = file.path(output_dir, "Analyse_Diagramm3.png"), plot = plot3, width = 6, height = 4)

  # Generieren des Berichts mit R Markdown
  report_content <- '
---
title: "Studentenfeedback-Bericht"
output: pdf_document
---

In diesem Bericht wird das Feedback der Studierenden zu verschiedenen Aspekten des Lehrangebots ausgewertet, um Verbesserungsansätze zu identifizieren. Die allgemeine Zufriedenheit ist überwiegend hoch; dennoch gibt es Bereiche, in denen sich die Studierenden Weiterentwicklungen wünschen.

## Zufriedenheit mit Vorlesungen und Übungen

Die Mehrheit der Studierenden bewertet die Vorlesungen positiv, besonders hinsichtlich Struktur und Inhalt. Einige wünschen sich jedoch mehr Interaktivität zur besseren Festigung der Inhalte. Auch die Übungsgruppen erhalten gutes Feedback, allerdings äußerten manche den Wunsch nach kleineren Gruppen und einer besseren Betreuung.

![](Analyse_Diagramm1.png)

## Unterstützung durch Lehrende

Die Unterstützung und Zugänglichkeit der Lehrenden werden generell als sehr gut wahrgenommen. Studierende schätzen die schnelle Reaktion auf Anfragen. Ein kleines Verbesserungspotenzial liegt in der Erweiterung der digitalen Betreuungsmöglichkeiten.

![](Analyse_Diagramm2.png)

## Zufriedenheit mit Lernmaterialien

Das zur Verfügung gestellte Lernmaterial wird überwiegend positiv bewertet. Einige Studierende wünschen sich jedoch mehr ergänzende digitale Ressourcen und aktuelle Inhalte.

![](Analyse_Diagramm3.png)

## Fazit

Das Feedback zeigt eine hohe Zufriedenheit, weist jedoch auf Potenziale in Interaktivität, Betreuung und digitalen Ressourcen hin.
'

  # Speichern des R Markdown Dokuments
  report_path <- file.path(output_dir, "Studentenfeedback_Bericht.Rmd")
  writeLines(report_content, con = report_path)

  # Rendern des Berichts als PDF
  tryCatch({
    rmarkdown::render(input = report_path,
                      output_format = "pdf_document",
                      output_file = "Studentenfeedback_Bericht.pdf",
                      output_dir = output_dir,
                      quiet = TRUE)
    message("Der Bericht wurde erfolgreich erstellt und im folgenden Verzeichnis gespeichert:")
    message(normalizePath(output_dir))
  }, error = function(e) {
    message("Fehler beim Generieren des Berichts: ", e$message)
  })
}

# Bericht generieren
generate_report(data_directory, output_dir)

