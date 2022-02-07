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

############################
# Variables

nombre_croix = 0
nombre_carre = 0
nombre_cercle = 0

############################
# Fonctions

def placer_figures(event):
    """fonction qui créer les figures si les conditions sont respectés."""
    global nombre_croix, nombre_carre, nombre_cercle
    if nombre_croix < 2 and nombre_carre < 3 and event.x < LARGEUR/3:
        x0_rec = event.x - COTE_CARRE / 2
        y0_rec = event.y - COTE_CARRE / 2
        x1_rec = x0_rec + COTE_CARRE
        y1_rec = y0_rec + COTE_CARRE
        canvas.create_rectangle(x0_rec, y0_rec, x1_rec, y1_rec, outline="blue")
        nombre_carre += 1
        canvas.create_line(x0_rec, y0_rec, x1_rec, y1_rec, fill="blue")
        canvas.create_line(x1_rec, y0_rec, x0_rec, y1_rec, fill="blue")
        nombre_croix += 1
        canvas.addtag_all("figures")
    elif nombre_carre < 3 and event.x > LARGEUR / 3 and event.x < LARGEUR * 2 / 3:
        x0_rec = event.x - COTE_CARRE / 2
        y0_rec = event.y - COTE_CARRE / 2
        x1_rec = x0_rec + COTE_CARRE
        y1_rec = y0_rec + COTE_CARRE
        canvas.create_rectangle(x0_rec, y0_rec, x1_rec, y1_rec, outline="green")
        nombre_carre += 1
        canvas.addtag_all("figures")
    elif nombre_cercle < 3 and event.x > LARGEUR * 2 / 3:
        x0_rec = event.x - COTE_CARRE / 2
        y0_rec = event.y - COTE_CARRE / 2
        x1_rec = x0_rec + COTE_CARRE
        y1_rec = y0_rec + COTE_CARRE
        canvas.create_oval(x0_rec, y0_rec, x1_rec, y1_rec, outline="red")
        nombre_cercle += 1
        canvas.addtag_all("figures")


def redemarrer():
    """fonction qui supprime les figures."""
    global nombre_carre, nombre_cercle, nombre_croix
    canvas.delete("figures")
    canvas.dtag("figures")
    canvas.create_line(LARGEUR/3, HAUTEUR, LARGEUR/3, 0, fill="white")
    canvas.create_line(LARGEUR*2/3, HAUTEUR, LARGEUR*2/3, 0, fill="white")
    nombre_carre = 0
    nombre_cercle = 0
    nombre_croix = 0

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 03")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg="black")
canvas.create_line(LARGEUR/3, HAUTEUR, LARGEUR/3, 0, fill="white")
canvas.create_line(LARGEUR*2/3, HAUTEUR, LARGEUR*2/3, 0, fill="white")

#Bouton
bouton_redemarrer = tk.Button(content, text="Redémarrer", command=redemarrer)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_redemarrer.grid(column=0, row=1)

#Evenement
canvas.bind("<Button-1>", placer_figures)

#Boucle principale
root.mainloop()
