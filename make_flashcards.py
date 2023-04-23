#!/usr/bin/env python3

import csv

CSV_PATH = "fred-jehle-spanish-verbs-master/jehle_verb_database.csv"

FORMS = [
        ( "1s", "yo" ),
        ( "2s", "tú" ),
        ( "3s", "él" ),
        ( "3s", "ella" ),
        ( "3s", "Usted" ),
        ( "1p", "nosotros" ),
        ( "1p", "nosotras" ),
        ( "2p", "vosotros" ),
        ( "2p", "vosotras" ),
        ( "3p", "ellos" ),
        ( "3p", "ellas" ),
        ( "3p", "Ustedes" ),
        ]

def main():
    # Encoding needs to remove Unicode BOM
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [ row for row in reader ]
    #print(rows[0])
    ar_verbs = [ row for row in rows if row["infinitive"].endswith("ar") ]
    selected_verbs = [
            row for row in rows
            if row["infinitive"].endswith("ar")
            and row["mood"] == "Indicativo"
            and row["tense"] == "Presente"
            ]
    for row in selected_verbs:
        for form, pronoun in FORMS:
            print(row["infinitive"], row["mood"], row["tense"], pronoun, row["form_"+form])

if __name__ == '__main__':
    main()

