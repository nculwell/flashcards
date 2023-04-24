#!/usr/bin/env python3

import sys, os, os.path
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
    args = sys.argv[1:]
    if len(args) == 2:
        mood, tense = args
    elif len(args) == 3:
        mood, tense, ending = args
    else:
        print("Invalid arguments. USAGE: make_flashcards.py <mood> <tense> [<ending>]")
    # Encoding needs to remove Unicode BOM
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = [ row for row in reader ]
    #print(rows[0])
    (endings,) = validate_args(rows, mood, tense, ending)
    selected_verbs = select_verbs(rows, mood, tense, endings)
    write_output(selected_verbs)

def select_verbs(rows, mood, tense, endings):
    selected_verbs = rows
    if endings:
        selected_verbs = [
                row for row in selected_verbs
                if any(( row["infinitive"].endswith(e) for e in endings ))
                ]
    selected_verbs = [
            row for row in selected_verbs
            if row["mood"] == mood
            and row["tense"] == tense
            ]
    return selected_verbs

def write_output(selected_verbs):
    print("#separator:Semicolon")
    print("#html:false")
    for row in selected_verbs:
        for form, pronoun in FORMS:
            print(
                    '"' + row["mood"] + "\n" + row["tense"]
                    + "\n\n"
                    + pronoun + " [" + row["infinitive"] + "]"
                    + '";"'
                    + pronoun + " " + row["form_"+form]
                    + '"'
                    )

def validate_args(rows, mood, tense, ending):
    err = sys.stderr
    all_moods = set(( row["mood"] for row in rows ))
    all_tenses = set(( row["tense"] for row in rows ))
    if mood not in all_moods:
        print("Invalid mood: " + mood, file=err)
        print("Available moods: " + (', '.join(all_moods)), file=err)
        sys.exit(1)
    if tense not in all_tenses:
        print("Invalid tense: " + tense, file=err)
        print("Available tenses: " + (', '.join(all_tenses)), file=err)
        sys.exit(1)
    endings = None
    if ending:
        endings = ending.split(',')
        invalid = []
        for e in endings:
            if e not in ['ar', 'er', 'ir']:
                invalid.append(e)
        if len(invalid) > 0:
            print("Invalid endings: " + (','.join(invalid)), file=err)
            sys.exit(1)
    return ( endings, )

if __name__ == '__main__':
    main()

