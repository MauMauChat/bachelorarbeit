#!/bin/bash

# Ziel-Datei für die Ausgabe
output_file="/home/lucy/Documents/Notes/bachelorarbeit/csv/output.txt"

# Hauptverzeichnis mit den CSV-Dateien
input_folder="/home/lucy/Documents/Notes/bachelorarbeit/csv"

# Leere Ausgabe-Datei
> "$output_file"

# Suche rekursiv nach allen CSV-Dateien in Unterverzeichnissen
find "$input_folder" -type f -name "*.csv" | while read -r file; do
    # Schreibe den Dateinamen und Pfad in die Ausgabe-Datei
    echo "Filename: $(basename "$file")" >> "$output_file"
    
    # Füge die ersten drei Zeilen der CSV-Datei hinzu
    head -n 3 "$file" >> "$output_file"
    
    # Trenne die Dateien für bessere Lesbarkeit
    echo -e "\n---\n" >> "$output_file"
done

