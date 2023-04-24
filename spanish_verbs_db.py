#!/usr/bin/env python3

import csv

CSV_PATH = "fred-jehle-spanish-verbs-master/jehle_verb_database.csv"

def read_word_list():
    # Read the cards into a list.
    # Encoding needs to remove Unicode BOM.
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [ row for row in reader ]
    # Remove extranous spaces.
    for row in rows:
        eng = row["infinitive_english"]
        has_extra_spaces = all(( eng[i] == ' ' for i in range(1, len(eng), 2) ))
        if has_extra_spaces:
            row["infinitive_english"] = ''.join((
                eng[i] for i in range(0, len(eng), 2)
                ))
    return rows

def write_output_header():
    print("#separator:Semicolon")
    print("#html:false")

def write_output_line(fields):
    print(';'.join(( f'"{f}"' for f in fields )))

def main():
    rows = read_word_list()
    # Get unique row for each verb.
    rows = [ row for row in rows if row["mood"] == "Indicativo" and row["tense"] == "Presente" ]
    # Print meanings.
    for row in rows:
        print(row["infinitive_english"])

if __name__ == '__main__':
    main()

