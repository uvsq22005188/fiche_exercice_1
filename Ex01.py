############################
# Auteur : Kaan Doyurur
############################
# Import des librairies

import tkinter as tk

############################
# Constantes

HAUTEUR = 500
LARGEUR = 500
REC_LARGEUR = 400
REC_HAUTEUR = 250
BG_COLOR = "black"
############################
# Variables

############################
# Fonctions

def changer_couleur(event):
    """Change la couleur du rectangle dans le canvas si et seulement si le clique souris à lieu sur le rectangle."""
    if event.x >= 0 and event.x <= REC_LARGEUR and event.y >= 0 and event.y <= REC_HAUTEUR:
        if canvas.itemcget(rectangle, "fill") == "red":
            canvas.itemconfigure(rectangle, fill="blue")
        else:
            canvas.itemconfigure(rectangle, fill="red")
    else:
        canvas.unbind("<Button-1>")
        

def recommencer():
    """Applique la couleur rouge au rectangle et active le clique gauche de la souris"""
    canvas.itemconfigure(rectangle, fill="red")
    canvas.bind("<Button-1>", changer_couleur)

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 01")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg=BG_COLOR)
rectangle = canvas.create_rectangle(0, 0, REC_LARGEUR, REC_HAUTEUR, fill="red")

#Bouton
bouton_recommencer = tk.Button(content, text="Recommencer", command=recommencer)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_recommencer.grid(column=0, row=1)


#Evenement
canvas.bind("<Button-1>", changer_couleur)

#Boucle principale
root.mainloop()
