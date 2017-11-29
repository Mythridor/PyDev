#!/usr/bin/python3.6
import selection_fonctions
import type_domaine_categories
import get_colon
import re
confirmation=''
while confirmation != "oui":
    sujet_fonction = input("Quel est la fonction du sujet?")
    pattern = re.compile(sujet_fonction)
    liste_fonctions = selection_fonctions.select_job()
    match = list(filter(pattern.match,liste_fonctions))

    if len(match) >1:
        print("Plusieurs intitulés de fonctions correspondent à votre recherche. Voici la liste:")
        for i in match:
            print(i)
    else:
        print('Vous avez choisi la fonction suivante:',match[0])
        confirmation = input("Confirmez-vous la sélection? [oui/non]")
        if confirmation == 'oui':
            col_x = get_colon.select_colon(match[0])
            print(col_x)