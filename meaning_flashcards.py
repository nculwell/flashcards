#!/usr/bin/env python3

import sys, os, os.path
import csv

CSV_PATH = "fred-jehle-spanish-verbs-master/jehle_verb_database.csv"

def main():
    # Encoding needs to remove Unicode BOM
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [ row for row in reader ]
    #print(rows[0]) ; return
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
        print(
                '"MEANING OF: ' + row["infinitive"] + '";"'
                + row["infinitive_english"]
                + '"'
                )

if __name__ == '__main__':
    main()

