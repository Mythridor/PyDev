#!/usr/bin/python3.6
# Auteurs: Benjamin ENOU, Sylvain RESSIER
# Société: GEKKO S.A.S.
# Description: script permettant de générer une fiche d'évaluation xls

####### Importation des scripts essentiels #######
import selection_fonctions
import type_domaine_categories
import get_colon
import get_ones
import re
#######

confirmation='' # Critère d'arrêt de boucle while
liste_fonctions = selection_fonctions.select_job() # Liste de fonctions
liste_competences = type_domaine_categories.get_skills()  # Liste des compétences

while True :
    if confirmation =="O" or confirmation =="Oui" or confirmation =='OUI' \
            or confirmation =='yes' or confirmation =='Y':
        break # condition d'arrêt de boucle
    if confirmation == "q" or confirmation == "exit" or confirmation == "quit":
        break
    sujet_fonction = str.capitalize(input("Quel est la fonction du sujet?\n"))
    pattern = re.compile(sujet_fonction)

    match = list(filter(pattern.match,liste_fonctions)) # noms de fonctions correspondant à la recherche

    if len(match) > 1:
        print("Plusieurs intitulés de fonctions correspondent à votre recherche. Voici la liste:")
        for i in match:
            print(i)
    else:
        print('Vous avez choisi la fonction suivante:',match[0])
        confirmation = str.capitalize(input("Confirmez-vous la sélection? [oui/non]\n"))
        if confirmation == "Oui" or confirmation =="O" or confirmation =='OUI' or confirmation =='yes' or confirmation =='Y':
            col_x = get_colon.select_colon(match[0])
            ones = get_ones.values(col_x[0])
            x = 0
            Skills4Job = list()
            for x in range(0,len(ones)-1):
                #print(ones[x], type(ones[x]))
                #print(len(liste_competences))
                #print(liste_competences[x])
                if ones[x][0] == '':
                    continue
                #elif ones[x] == "1.0":
                 #   print(liste_competences[x])
                elif ones[x][0] == 1.0:
                    Skills4Job.append(liste_competences[x])
            for i in Skills4Job:
                print(i)

