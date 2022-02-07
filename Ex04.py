############################
# Auteur : Kaan Doyurur
############################
# Import des librairies

import tkinter as tk

############################
# Constantes

HAUTEUR = 500
LARGEUR = 500
COTE_CARRE = 50
TAILLE_MAX = 100
TAILLE_MIN = 20

############################
# Variables



############################
# Fonctions

def afficher_carré(event):
    """"""
    global carré, COTE_CARRE
    if COTE_CARRE >= 20 and event.x > LARGEUR / 2 - COTE_CARRE / 2 and event.x < LARGEUR / 2 + COTE_CARRE / 2 and event.y > HAUTEUR / 2 - COTE_CARRE / 2 and event.y < HAUTEUR / 2 + COTE_CARRE / 2:
        canvas.delete(carré)
        COTE_CARRE = COTE_CARRE - 10
        carré = canvas.create_rectangle(LARGEUR / 2 - COTE_CARRE / 2, HAUTEUR / 2 + COTE_CARRE / 2, LARGEUR / 2 + COTE_CARRE / 2, HAUTEUR / 2 - COTE_CARRE / 2, fill="red")
        print(COTE_CARRE)
    elif COTE_CARRE <= 100 and event.x < LARGEUR / 2 - COTE_CARRE / 2 or event.x > LARGEUR / 2 + COTE_CARRE / 2 or event.y < HAUTEUR / 2 - COTE_CARRE / 2 or event.y > HAUTEUR / 2 + COTE_CARRE / 2:
        canvas.delete(carré)
        COTE_CARRE = COTE_CARRE + 10
        carré = canvas.create_rectangle(LARGEUR / 2 - COTE_CARRE / 2, HAUTEUR / 2 + COTE_CARRE / 2, LARGEUR / 2 + COTE_CARRE / 2, HAUTEUR / 2 - COTE_CARRE / 2, fill="red")



def pause_programme():
    """fonction qui suspend le programme"""
    

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 04")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg="white")
carré = canvas.create_rectangle(LARGEUR / 2 - COTE_CARRE / 2, HAUTEUR / 2 + COTE_CARRE / 2, LARGEUR / 2 + COTE_CARRE / 2, HAUTEUR / 2 - COTE_CARRE / 2, fill="red")

#Bouton
bouton_pause = tk.Button(content, text="Pause", command=pause_programme)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_pause.grid(column=0, row=1)

#Evenement
canvas.bind("<Button-1>", afficher_carré)

#Boucle principale
root.mainloop()
