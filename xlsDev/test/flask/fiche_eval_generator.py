#!/usr/bin/python3.6
# Auteurs: Benjamin ENOU, Sylvain RESSIER
# Société: GEKKO S.A.S.
# Description: script permettant de générer une fiche d'évaluation xls

####### Importation des scripts essentiels #######
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf


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


def writeout(lista, job, prenom, nom):
    source = open_workbook("test.xls", formatting_info=True).sheet_by_index(1)# Ouverture du fichier test.xls avec xlrd
    source2 = open_workbook("base.xls",formatting_info=True).sheet_by_index(0)
    input_wb = open_workbook("base.xls",formatting_info=True)
    copy_wb = copy(input_wb)
    sheet = copy_wb.get_sheet(1)
    sheet2 = copy_wb.get_sheet(0)
    buffer = 19
    longueur=len(lista) # longueur de la liste
    plain = easyxf('font: name Calibri, height 220; border: left thin, right thin, top thin, bottom thin;\
     pattern: fore_color white, back_color white, pattern none; alignment: wrap True, shrink_to_fit True,\
      horizontal center, vertical center')
    full_name = prenom.strip()+' '+nom.strip()
    for rowsx in range(0, source.nrows):
        for colsx in range(0,source.ncols):
            if rowsx < 19:
                if rowsx == 2 and colsx in range(0,2):
                    #for colsx in range(0,2):
                    sheet.write(rowsx, colsx, source.cell(rowsx,colsx).value, plain)
                else:
                    sheet.write(2, 2, full_name ,plain)
                sheet.write(rowsx, colsx, source.cell(rowsx, colsx).value, plain)
                if rowsx == 5 :
                    for colsx in range(0,1):
                        sheet.write(rowsx, colsx, source.cell(rowsx,colsx).value, plain)
                    sheet.write(rowsx, 2, job,plain)
                sheet.write(rowsx, colsx, source.cell(rowsx, colsx).value, plain)

            elif rowsx == 19:
                for row, data in enumerate(lista):
                             # row est le compteur de lignes (c'est un chiffre entier)
                             # data (qui est une liste) correspond à l'item numéro "row" de Skill4Job (data = Skill4Job[count])
                    for col,element in enumerate(data):
#                                  element est la valeur pour chaque élément de la liste data à l'index "col"
                        offset = row + buffer
                        for i in range(4, source.ncols):
                            sheet.write(offset, i, None, plain)
                        offset = row + buffer  # chaque count est décalée de 20 lignes.
                        sheet.write(offset, col, element, plain)

    # Pour la feuille 0, copie intégrale et rectification de la couleur:
    for rowsx in range(0, source2.nrows):
        for colsx in range(0,source2.ncols):
            if rowsx == 2:
                for colsx in range(0,2):
                    sheet2.write(rowsx, colsx, source2.cell(rowsx, colsx).value, plain)
                sheet2.write(rowsx, 3, full_name, plain)
            sheet2.write(rowsx, colsx, source2.cell(rowsx, colsx).value, plain)
            if rowsx == 5:
                for colsx in range(0, 2):
                    sheet2.write(rowsx, colsx, source2.cell(rowsx, colsx).value, plain)
                sheet2.write(rowsx, 3, job, plain)
            sheet2.write(rowsx, colsx, source2.cell(rowsx, colsx).value, plain)
    copy_wb.save('static/output/{0}_{1}.xls'.format(prenom.strip(), nom.strip()))


def get_names():
    list_names = open_workbook("liste_noms.xls", formatting_info=True).sheet_by_index(0)
    liste2=list()
    for row_x in range(2,list_names.nrows):
        full_row= list()
        for col_x in range(1,4):
            full_row.append(list_names.cell(row_x, col_x).value)
        if full_row[2] != "":
            liste2.append(full_row)
    return liste2


#######

liste_fonctions = select_job()  # Liste de fonctions
liste_competences = get_skills()  # Liste des compétences
liste_nom = get_names()
for people in liste_nom:
    #print(people)
    prenom = people[0]
    nom = people[1]
    job = people[2]
#for job in liste_fonctions:  # pour chaque élément de la liste de fonctions.
    col_x = select_colon(job)  # Selection de la colonne avec l'intitulé du poste
    #print(col_x, prenom,nom)
    ones = values(col_x[0])  # Récupération des compétences à partir du numéro de colonne
    Skills4Job = list()  # Création d'une liste de concaténation
    for x in range(0, len(ones)-1):
        if ones[x][0] == '':
            continue
        elif ones[x][0] == 1.0:
            Skills4Job.append(liste_competences[x])
    longueur = len(Skills4Job)
            # Passage à l'écriture
    writeout(Skills4Job, job, prenom, nom)