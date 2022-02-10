############################
# Auteur : Kaan Doyurur
############################
# Import des librairies

import tkinter as tk

############################
# Constantes

HAUTEUR = 500
LARGEUR = 500
BG_COLOR = "white"
COTE_CARRE = 50
RAYON_OVAL = 50

############################
# Listes
liste_couleurs = []

############################
# Fonctions

def changement_couleur(event):
    """Change la couleur du cercle avec la couleur du carré choisi"""
    
    if canvas.find_withtag("current") and canvas.itemcget("current", "fill") == "green":
        canvas.itemconfigure("cercle_noir", fill="green")
        liste_couleurs.append("green")
        print(liste_couleurs)
    elif canvas.find_withtag("current") and canvas.itemcget("current", "fill") == "yellow":
        canvas.itemconfigure("cercle_noir", fill="yellow")
        liste_couleurs.append("yellow")
        print(liste_couleurs)
    elif canvas.find_withtag("current") and canvas.itemcget("current", "fill") == "blue":
        canvas.itemconfigure("cercle_noir", fill="blue")
        liste_couleurs.append("blue")
        print(liste_couleurs)
    else:
        canvas.itemconfigure("cercle_noir", fill="black")
        print(liste_couleurs)

def annuler():
    """Le cercle reprends la couleur qu'il avait avant le dernier changement de couleur"""
    if len(liste_couleurs) == 1:
        print("Liste vide")
    else:
        liste_couleurs.pop(-1)
        canvas.itemconfigure("cercle_noir", fill=liste_couleurs[-1])

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 06")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg=BG_COLOR)
canvas.create_rectangle(0, 0, COTE_CARRE, COTE_CARRE, tags="carré_vert", fill="green")
canvas.create_rectangle(COTE_CARRE, 0, COTE_CARRE*2, COTE_CARRE, tags="carré_jaune", fill="yellow")
canvas.create_rectangle(COTE_CARRE*2, 0, COTE_CARRE*3, COTE_CARRE, tags="carré_bleue", fill="blue")
canvas.create_oval(LARGEUR/2-RAYON_OVAL, HAUTEUR/2+RAYON_OVAL, LARGEUR/2+RAYON_OVAL, HAUTEUR/2-RAYON_OVAL, tags="cercle_noir", fill="black")
#Bouton
bouton_annuler = tk.Button(content, text="Annuler", command=annuler)

############################
#Placement des widgets
content.grid(column=1, row=0)
canvas.grid(column=1, row=0)
bouton_annuler.grid(column=0, row=0)

#Evenement
canvas.bind("<Button-1>", changement_couleur)

#Boucle principale
root.mainloop()
