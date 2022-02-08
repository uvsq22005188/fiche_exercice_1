############################
# Auteur : Kaan Doyurur
############################
# Import des librairies

import tkinter as tk

############################
# Constantes

HAUTEUR = 500
LARGEUR = 500


############################
# Variables

compteur1 = 0
compteur2 = 0

############################
# Fonctions

def ligne(event):
    """fonction qui place une ligne au niveau des cliques souris et les supprime ensuite au bout du 5eme clique."""
    global compteur1, x1, y1, x2, y2, x3, y3, x4, y4, ligne_bleue, ligne_rouge
    if compteur1 == 0:
        x1 = event.x
        y1 = event.y
        compteur1 += 1   
    elif compteur1 == 1:
        x2 = event.x
        y2 = event.y 
        ligne_bleue = canvas.create_line(x1,y1,x2,y2, fill="blue")
        compteur1 += 1
    elif compteur1 == 2:
        x3 = event.x
        y3 = event.y
        compteur1 += 1
    elif compteur1 == 3:
        x4 = event.x
        y4 = event.y
        ligne_rouge = canvas.create_line(x3,y3,x4,y4, fill="red")
        compteur1 += 1
    elif compteur1 == 4:
        canvas.delete(ligne_bleue, ligne_rouge)
        compteur1 = 0


def pause_restart():
    """fonction qui suspend le programme"""
    if bouton_pause.cget("text") == "Pause":
        canvas.unbind("<Button-1>")
        bouton_pause.configure(text="Restart")
    else:
        canvas.bind("<Button-1>", ligne)
        bouton_pause.configure(text="Pause")

########################################################
# Partie principale

############################
#Création des widgets

#Fenêtre
root = tk.Tk()
root.title("Exercice 02")
content = tk.Frame(root) 

#Canvas
canvas = tk.Canvas(content, height=HAUTEUR, width=LARGEUR, bg="white")

#Bouton
bouton_pause = tk.Button(content, text="Pause", command=pause_restart)

############################
#Placement des widgets
content.grid(column=0, row=0)
canvas.grid(column=0, row=0)
bouton_pause.grid(column=0, row=1)

#Evenement
canvas.bind("<Button-1>", ligne)

#Boucle principale
root.mainloop()
