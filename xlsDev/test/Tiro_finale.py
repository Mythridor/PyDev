#!/usr/bin/python3.6
# Auteurs: Benjamin ENOU, Sylvain RESSIER
# Société: GEKKO S.A.S.
# Description: script permettant de générer une fiche d'évaluation xls

####### Importation des scripts essentiels #######
from xlrd import open_workbook
import type_domaine_categories
from xlutils.copy import copy
import selection_fonctions
from xlwt import easyxf
import get_colon
#import tabTest2
import get_ones
import re
#######

confirmation = ''  # Critère d'arrêt de boucle while
liste_fonctions = selection_fonctions.select_job()  # Liste de fonctions
liste_competences = type_domaine_categories.get_skills()  # Liste des compétences

while True:
    if confirmation == "O" or confirmation == "Oui" or confirmation == 'OUI' \
            or confirmation == 'yes' or confirmation == 'Y':
        break  # condition d'arrêt de boucle
    if confirmation == "q" or confirmation == "exit" or confirmation == "quit":
        break
    sujet_fonction = str.capitalize(input("Quel est la fonction du sujet? (q pour quitter)\n"))
    pattern = re.compile(sujet_fonction)

    match = list(filter(pattern.match, liste_fonctions))  # noms de fonctions correspondant à la recherche

    if len(match) > 1:
        print("Plusieurs intitulés de fonctions correspondent à votre recherche. Voici la liste:")
        for i in match:
            print(i)
    else:
        print('Vous avez choisi la fonction suivante:', match[0])
        confirmation = str.capitalize(input("Confirmez-vous la sélection? [oui/non]\n"))
        if confirmation == "Oui" or confirmation == "O" or confirmation == 'OUI' or confirmation == 'YES' \
                or confirmation == 'Y':
            col_x = get_colon.select_colon(match[0])
            ones = get_ones.values(col_x[0])
            x = 0
            Skills4Job = list()
            for x in range(0, len(ones)-1):
                if ones[x][0] == '':
                    continue
                # elif ones[x] == "1.0":
                #   print(liste_competences[x])
                elif ones[x][0] == 1.0:
                    Skills4Job.append(liste_competences[x])
            longueur = len(Skills4Job)
            buffer = 20
            for count, data in enumerate(Skills4Job):
                # count est le compteur de lignes (c'est un chiffre integer)
                # data correspond à l'item numéro "count" de Skill4Job (data = Skill4Job[count])
                for element in range(0, 4):
                    # element est l'index entre 0 et 4 pour chaque élément de la liste data
                    offset = count+buffer
                    print(data[element], offset) # chaque count est décalée de 20 lignes.
