"""Projet N°2 : Compression d'image en JPEG"""
import math
from math import cos, pi, sqrt
from copy import deepcopy
from typing import List
# Insertion des modules nécessaire au bon fonctionnement du programme.
print('\n', "Bienvenue ! Ce programme est un processus de compression d'image en JPEG.")
print(" Programme de THIERRY Louis")
print('\n', "Voici le tableau des valeurs initiales de notre image (c'est l'exemple du sujet) : ", '\n')

# Insertion des valeurs initiales de l'image d'exemple.
tableau_exempl = [[188, 225, 237, 237, 277, 205, 199, 222],
                  [157, 186, 205, 225, 237, 205, 218, 225],
                  [104, 125, 149, 143, 151, 123, 149, 191],
                  [132, 169, 128, 104, 81, 61, 81, 152],
                  [125, 169, 125, 104, 104, 107, 87, 158],
                  [107, 185, 201, 187, 185, 179, 161, 186],
                  [125, 180, 233, 223, 223, 205, 223, 223],
                  [104, 152, 186, 180, 196, 203, 203, 212]]
# Affiche le tableau de l'image d'origine
print("", tableau_exempl[0], '\n', tableau_exempl[1], '\n', tableau_exempl[2], '\n',
      tableau_exempl[3], '\n', tableau_exempl[4], '\n', tableau_exempl[5], '\n',
      tableau_exempl[6], '\n', tableau_exempl[7], '\n')
print('\n', "Après la conversion DCT, on obtient le nouveau tableau : ", '\n')
# Programme de DCT.
def encoder_dct(ancien_tableau: List[List[int]]) -> List[List[int]]:
    nouveau_tableau: List[List[int]] = deepcopy(ancien_tableau)
    # Copie complète des valeurs du tableau d'origine
    for nouveau_y in range(8):
        for nouveau_x in range(8):
    # Permet le balayage complet de toutes les valeurs du tableau
            nouvelle_valeur = 0
    # On insère une constante pour la boucle
            for ancien_y in range(8):
                for ancien_x in range(8):
                    nouvelle_valeur += (
                            ancien_tableau[ancien_y][ancien_x] *
                            cos(((2 * ancien_y + 1) * nouveau_y * pi) / 16) *
                            cos(((2 * ancien_x + 1) * nouveau_x * pi) / 16)
                    )
    # Utilisation de la formule de DCT
            if nouveau_y == 0:
                nouvelle_valeur /= sqrt(2)
            if nouveau_x == 0:
                nouvelle_valeur /= sqrt(2)
            nouvelle_valeur /= 4
            nouveau_tableau[nouveau_y][nouveau_x] = math.floor(nouvelle_valeur)
    return nouveau_tableau # On redonne les valeurs après la conversion DCT
# On affiche les valeurs du nouveau tableau après la DCT.
print("", encoder_dct(tableau_exempl)[0], '\n',
      encoder_dct(tableau_exempl)[1], '\n',
      encoder_dct(tableau_exempl)[2], '\n',
      encoder_dct(tableau_exempl)[3], '\n',
      encoder_dct(tableau_exempl)[4], '\n',
      encoder_dct(tableau_exempl)[5], '\n',
      encoder_dct(tableau_exempl)[6], '\n',
      encoder_dct(tableau_exempl)[7])

nouveau_tableau = []
nouveau_tableau.append(encoder_dct(tableau_exempl)[0])
nouveau_tableau.append(encoder_dct(tableau_exempl)[1])
nouveau_tableau.append(encoder_dct(tableau_exempl)[2])
nouveau_tableau.append(encoder_dct(tableau_exempl)[3])
nouveau_tableau.append(encoder_dct(tableau_exempl)[4])
nouveau_tableau.append(encoder_dct(tableau_exempl)[5])
nouveau_tableau.append(encoder_dct(tableau_exempl)[6])
nouveau_tableau.append(encoder_dct(tableau_exempl)[7])

print('\n', "Avec la DCT Inverse, on obtient le nouveau tableau : ")

def decoder_dct(ancien_tableau: List[List[int]]) -> List[List[int]]:
    nouveau_tableau: List[List[int]] = deepcopy(ancien_tableau)
    # On fait une copie de l'ancien tableau.
    for nouveau_y in range(8):
        for nouveau_x in range(8):
            nouvelle_valeur = 0
            for ancien_y in range(8):
                for ancien_x in range(8):
                    valeur_a_ajouter = (
                            ancien_tableau[ancien_y][ancien_x] *
                            cos(((2 * nouveau_y + 1) * ancien_y * pi) / 16) *
                            cos(((2 * nouveau_x + 1) * ancien_x * pi) / 16)
                    )
                    if ancien_y == 0:
                        valeur_a_ajouter /= sqrt(2)
                    if ancien_x == 0:
                        valeur_a_ajouter /= sqrt(2)
                    nouvelle_valeur += valeur_a_ajouter
            nouvelle_valeur /= 4
            nouveau_tableau[nouveau_y][nouveau_x] = math.floor(nouvelle_valeur)
    return nouveau_tableau # Même déroulement du programme sauf qu'on utilise une formule différente

print(" \n", decoder_dct(nouveau_tableau)[0], '\n',
      decoder_dct(nouveau_tableau)[1], '\n',
      decoder_dct(nouveau_tableau)[2], '\n',
      decoder_dct(nouveau_tableau)[3], '\n',
      decoder_dct(nouveau_tableau)[4], '\n',
      decoder_dct(nouveau_tableau)[5], '\n',
      decoder_dct(nouveau_tableau)[6], '\n',
      decoder_dct(nouveau_tableau)[7])

print('\n', "On applique la fonction de seuil (qui ne fonctionne pas pour l'instant), on obtient le nouveau tableau : ")

def encoder_seuil(ancien_tableau: List[List[int]]) -> List[List[int]]:
    nouveau_tableau: List[List[int]] = deepcopy(ancien_tableau)
    nouveau_tableau2: List[List[int]] = deepcopy(ancien_tableau)
    s = 4 # On applique un seuil, ici 4 de l'exemple
    for nouveau2_y in range(8):
        for nouveau2_x in range(8):
            for nouveau_y in range(8):
                for nouveau_x in range(8):
                    nouvelle_valeur = 0
                    for ancien_y in range(8):
                        for ancien_x in range(8):
                            nouvelle_valeur += (
                                nouveau_tableau2[nouveau2_y][nouveau2_x] // (1 + (nouveau_y + nouveau_x + 1) * s)
                            ) # On applique le calcul : N // F avec F = 1 + (u + v + 1) * s
                    nouveau_tableau[nouveau_y][nouveau_x] = math.floor(nouvelle_valeur)
    return nouveau_tableau

print(" \n", encoder_seuil(encoder_dct(tableau_exempl))[0], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[1], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[2], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[3], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[4], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[5], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[6], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[7])

print('\n', "Fonction de seuil Inverse, on obtient le nouveau tableau : ")

def decoder_seuil(ancien_tableau: List[List[int]]) -> List[List[int]]:
    nouveau_tableau: List[List[int]] = deepcopy(ancien_tableau)
    nouveau_tableau2: List[List[int]] = deepcopy(ancien_tableau)
    s = 4
    for nouveau2_y in range(8):
        for nouveau2_x in range(8):
            for nouveau_y in range(8):
                for nouveau_x in range(8):
                    nouvelle_valeur = 0
                    for ancien_y in range(8):
                        for ancien_x in range(8):
                            valeur_a_ajouter = (
                                    nouveau_tableau2[nouveau2_y][nouveau2_x] * (1 + (nouveau_y + nouveau_x + 1) * s)
                            )
                            nouvelle_valeur += valeur_a_ajouter
                    nouveau_tableau[nouveau_y][nouveau_x] = math.floor(nouvelle_valeur)
    return nouveau_tableau

print(" \n", decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[0], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[1], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[2], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[3], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[4], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[5], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[6], '\n',
      decoder_seuil(encoder_seuil(encoder_dct(tableau_exempl)))[7])

def encoder_zig_zag(ancien_tableau: List[List[int]]) -> List[List[int]]:
    # Je n'ai pas eu le temps de faire ce programme mais la réponse sera
    # quand même afficher.
    return nouveau_tableau

print('\n', "Pour la lecture en Zig-Zag, on obtient ce résultat :")
print(" La fonction n'a pas été faite mais le résultat est simple.")
print(" [64, 0, 0, 0, ...")

print('\n', "Pour la lecture en Zig-Zag Inverse, on obtient ce résultat :")
print(" La fonction n'a pas été faite mais le résultat est simple.")
print("", encoder_seuil(encoder_dct(tableau_exempl))[0], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[1], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[2], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[3], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[4], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[5], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[6], '\n',
      encoder_seuil(encoder_dct(tableau_exempl))[7])

liste_zz = [64, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0]

def encoder_RLE(input_list):
    # On définit les constantes pour évoluer dans le programme
    output = []
    precedent_value = None
    taille_sequence = 0
    # On démarre la boucle :
    for current_value in input_list:
        if current_value != precedent_value and precedent_value != None:
        # Si la valeur n'est pas égale à la valeur précédente et si la
        # précédente valeur n'est pas nul alors :
            # On fait apprendre à output la taille et la valeur.
            output.append(taille_sequence)
            output.append(precedent_value)
            # Définition de la taille de la séquence
            taille_sequence = 1
        else:
        # Sinon on ajoute 1 à la taille de la séquence à chaque fois.
            taille_sequence += 1
        precedent_value = current_value
    # Dans la boucle, on fait apprendre à output la taille
    # puis la valeur à chaque fois
    output.append(taille_sequence)
    output.append(precedent_value)
    return output # On redonne les valeurs

print('\n', "Fonction RLE, on obtient le nouveau tableau : ")
print('\n', encoder_RLE(liste_zz))

def decoder_RLE(input):
    # On définit les constantes pour évoluer dans le programme
    output = []
    input_size = len(input)
    x = 0
    # On démarre la boucle :
    while x < input_size:
        # Les tailles et les valeurs sont restituer
        taille_sequence = input[x]
        valeur_sequence = input[x + 1]
        # Calcul pour redonner les valeurs dans le bon ordre
        output = output + [valeur_sequence] * taille_sequence
        x = x + 2
    return output # On redonne les valeurs

print('\n', "Fonction RLE Inverse, on obtient le nouveau tableau : ")
print('\n', decoder_RLE(encoder_RLE(liste_zz)))
