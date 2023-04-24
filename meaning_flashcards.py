#!/usr/bin/env python3

import sys, os, os.path
import csv

import spanish_verbs_db

CSV_PATH = "fred-jehle-spanish-verbs-master/jehle_verb_database.csv"

def main():
    rows = spanish_verbs_db.read_word_list()
    selected_verbs = [
            row for row in rows
            if row["mood"] == "Indicativo"
            and row["tense"] == "Presente"
            ]
    write_output(selected_verbs)

def write_output(selected_verbs):
    print("#separator:Semicolon")
    print("#html:false")
    for row in selected_verbs:
        spanish_verbs_db.write_output_line(
                [ row["infinitive"], row["infinitive_english"] ]
                )

if __name__ == '__main__':
    main()

