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

############################
# Variables

x0_blue = LARGEUR*2/3
y0_blue = HAUTEUR
x1_blue = x0_blue
y1_blue = 0
x0_red = LARGEUR/3
y0_red = HAUTEUR
x1_red = x0_red
y1_red = 0



############################
# Fonctions

def deplacement(event):
    """"""
    x0_blue = LARGEUR*2/3
    y0_blue = HAUTEUR
    x1_blue = LARGEUR*2/3
    y1_blue = 0
    x0_red = LARGEUR/3
    y0_red = HAUTEUR
    x1_red = LARGEUR/3
    y1_red = 0
    
    if event.x < x0_red and x0_blue:
        canvas.move("ligne_rouge", -10, 0)
        canvas.move("ligne_bleue", -10, 0)
        canvas.itemconfigure("ligne_rouge", fill="blue")
        canvas.itemconfigure("ligne_bleue", fill="red")
    elif event.x > x0_red and event.x > x0_blue:
        canvas.move("ligne_rouge", 10, 0)
        canvas.move("ligne_bleue", 10, 0)
        canvas.itemconfigure("ligne_rouge", fill="blue")
        canvas.itemconfigure("ligne_bleue", fill="red")
    else:
        canvas.move("ligne_rouge", 10, 0)
        canvas.move("ligne_bleue", -10, 0)
        canvas.itemconfigure("ligne_rouge", fill="blue")
        canvas.itemconfigure("ligne_bleue", fill="red")
        



        
        


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
canvas.create_line(x0_red, y0_red, x1_red, y1_red, tags="ligne_rouge", fill="red", width=5)
canvas.create_line(x0_blue, y0_blue, x1_blue, y1_blue, tags="ligne_bleue", fill="blue", width=5)

#Bouton
bouton_recommencer = tk.Button(content, text="Recommencer", command="")

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_recommencer.grid(column=0, row=1)

#Evenement
canvas.bind("<Button-1>", deplacement)

#Boucle principale
root.mainloop()
