#!/usr/bin/python3.6
# Auteurs: Benjamin ENOU, Sylvain RESSIER
# Société: GEKKO S.A.S.
# Description: script permettant de générer une fiche d'évaluation xls

####### Importation des scripts essentiels #######
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy
from xlutils.styles import Styles
from xlwt import easyxf
import re

def get_skills():
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste=list()
    for row_x in range(3,matrix.nrows):
        intermediaire = list()
        for col_x in range(0,4):
            intermediaire.append(matrix.cell(row_x, col_x).value)
        liste.append(intermediaire)
    liste.pop(-1)  # suppression d'une liste vide
    return liste

def select_job():
    matrice = open_workbook("matrix.xls", formatting_info=True)
    jobs = matrice.sheet_by_index(1)
    liste=[]
    for col_x in range(0,jobs.ncols):
        cell = jobs.cell(0,col_x)
        if cell.value == '':
            continue
        else:
            liste.append(cell.value)
    liste.pop(0) # Suppression de "Fonction"
    liste.pop(-1) # Suppression du dernier élément
    return liste

def values(col_x):
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste = list()
    for row_x in range(3, matrix.nrows):
        intermediaire = list()
        intermediaire.append(matrix.cell(row_x, col_x).value)
        liste.append(intermediaire)
    liste.pop(-1)  # suppression d'un élément vide
    return liste

def select_colon(fonction):
    matrice = open_workbook("matrix.xls", formatting_info=True)
    jobs = matrice.sheet_by_index(1)
    colonne =list()
    for col_x in range(0,jobs.ncols):
        cell = jobs.cell(0,col_x)
        if cell.value == fonction:
            colonne.append(col_x)
    return colonne

def writeout(lista):
    source = open_workbook("test.xls", formatting_info=True).sheet_by_index(1)  # Ouverture du fichier test.xls avec xlrd
    #s = Styles(source)
    buffer = 19
    longueur=len(lista) # longueur de la liste
    w2 = Workbook()
    wb2 = w2.add_sheet(sheetname="Evalutation",cell_overwrite_ok=True)
    plain = easyxf('font: name Calibri, height 220')
    for rowsx in range(0, source.nrows):
        for colsx in range(0,source.ncols):
            if rowsx < 19:
                wb2.write(rowsx, colsx, source.cell(rowsx,colsx).value, plain)
                #print(source.cell(rowsx,colsx).value)
            if rowsx == 19:
                for count, data in enumerate(lista):
                            # count est le compteur de lignes (c'est un chiffre entier)
                            # data (qui est une liste) correspond à l'item numéro "count" de Skill4Job (data = Skill4Job[count])
                    for element in range(0, 4):
                                # element est l'index entre 0 et 4 pour chaque élément de la liste data
                        offset = count + buffer  # chaque count est décalée de 20 lignes.
                        wb2.write(offset, element, data[element], plain)  # ici element correspond également à la colonne de chaque liste
                        #print(data[element], offset)
                        continue
            elif rowsx >=19:
                wb2.write(rowsx+longueur, colsx, source.cell(rowsx, colsx).value, plain)
    w2.save('output_write.xls')
#######

confirmation = ''  # Critère d'arrêt de boucle while
liste_fonctions = select_job()  # Liste de fonctions
liste_competences = get_skills()  # Liste des compétences

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
            col_x = select_colon(match[0])
            ones = values(col_x[0])
            x = 0
            Skills4Job = list()
            for x in range(0, len(ones)-1):
                if ones[x][0] == '':
                    continue
                elif ones[x][0] == 1.0:
                    Skills4Job.append(liste_competences[x])
            longueur = len(Skills4Job)
            # Passage à l'écriture
            writeout(Skills4Job)

