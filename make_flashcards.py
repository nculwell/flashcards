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
    validate_args(rows, mood, tense, ending)
    selected_verbs = select_verbs(rows, mood, tense, ending)
    write_output(selected_verbs)

def select_verbs(rows, mood, tense, ending):
    selected_verbs = rows
    if ending:
        selected_verbs = [
                row for row in selected_verbs
                if row["infinitive"].endswith(ending)
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
    if ending and ending not in ['ar', 'er', 'ir']:
        print("Invalid ending: " + ending, file=err)
        sys.exit(1)

if __name__ == '__main__':
    main()

