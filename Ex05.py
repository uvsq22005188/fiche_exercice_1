############################
# Auteur : Kaan Doyurur
############################
# Import des librairies

import tkinter as tk

############################
# Constantes

HAUTEUR = 600
LARGEUR = 600
BG_COLOR = "white"
X0_BLUE = LARGEUR*2/3
Y0_BLUE = HAUTEUR
X1_BLUE = X0_BLUE
Y1_BLUE = 0
X0_RED = LARGEUR/3
Y0_RED = HAUTEUR
X1_RED = X0_RED
Y1_RED = 0

############################
# Variables

############################
# Fonctions

def deplacement(event):
    """déplace les lignes vers le clique"""
    
    x0_blue = canvas.coords(ligne_bleue)[0]
    x0_red = canvas.coords(ligne_rouge)[0]
    
    if event.x < x0_red and x0_blue:
        canvas.move("ligne_rouge", -10, 0)
        canvas.move("ligne_bleue", -10, 0)
        changer_couleurs()
    elif event.x > x0_red and event.x > x0_blue:
        canvas.move("ligne_rouge", 10, 0)
        canvas.move("ligne_bleue", 10, 0)
        changer_couleurs()
    elif event.x > x0_red and event.x < x0_blue:
        canvas.move("ligne_rouge", 10, 0)
        canvas.move("ligne_bleue", -10, 0)
        changer_couleurs()
        

def changer_couleurs():
    """change la couleur des lignes à chaque clique"""
    if canvas.itemcget(ligne_rouge, "fill") == "red" and canvas.itemcget(ligne_bleue, "fill") == "blue":
            canvas.itemconfigure("ligne_rouge", fill="blue")
            canvas.itemconfigure("ligne_bleue", fill="red")
    else:
        canvas.itemconfigure("ligne_rouge", fill="red")
        canvas.itemconfigure("ligne_bleue", fill="blue")
        
        
def recommencer():
    """retourne les lignes à leur position de départ initiale."""
    canvas.coords(ligne_rouge, X0_RED, Y0_RED, X1_RED, Y1_RED)
    canvas.coords(ligne_bleue, X0_BLUE, Y0_BLUE, X1_BLUE, Y1_BLUE)
    

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 05")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg=BG_COLOR)
ligne_rouge = canvas.create_line(X0_RED, Y0_RED, X1_RED, Y1_RED, tags="ligne_rouge", fill="red", width=5)
ligne_bleue = canvas.create_line(X0_BLUE, Y0_BLUE, X1_BLUE, Y1_BLUE, tags="ligne_bleue", fill="blue", width=5)

#Bouton
bouton_recommencer = tk.Button(content, text="Recommencer", command=recommencer)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_recommencer.grid(column=0, row=1)

#Evenement
canvas.bind("<Button-1>", deplacement)

#Boucle principale
root.mainloop()
