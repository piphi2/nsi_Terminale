''' Module permettant de saisir une suite de points en cliquant dans une fenêtre 1024*1024
    Les points sont renvoyés dans une structure de données pile ou file, au choix.
    Le choix entre pile ou file se passe en paramètre lors de l'appel de la
    fonction saisir_points_graphiquement (file par défaut)
    Le choix entre pile ou file peut être modifié à tout moment par un clic sur la molette de la souris

    * clic molette pour changer de structure de données File / Pile
    * clic gauche pour ajouter un point
    * clic droit pour supprimer un point
        - dans une file, on supprime la tête de file (le premier élément entré)
        - dans une pile, on supprime le sommet de la pile (le dernier élément entré)
'''

import tkinter as tk
from tkinter import simpledialog
from module_pile_file import Noeud, Pile, File


def saisir_points_graphiquement(choix = 'file'):
    racine = tk.Tk()
    racine.withdraw()

    #choix = simpledialog.askstring("Choix de la structure", "Tapez 'pile' (LIFO) ou 'file' (FIFO) :")

    if choix is None:
        return

    choix = choix.strip().lower()
    if choix == "pile":
        structure = Pile()
        mode = "PILE (LIFO)"
    else:
        structure = File()
        mode = "FILE (FIFO)"

    racine.deiconify()
    racine.title("Cliquez pour tracer le parcours")

    canevas = tk.Canvas(racine, width=1024, height=1024, bg="white")
    canevas.pack()

    def set_mode(nouveau_mode):
        nonlocal choix, structure, mode
        # Récupérer la liste des éléments dans l'ordre
        elements = structure.elements()
        if nouveau_mode == "pile":
            structure = Pile()
            for elem in elements:
                structure.empiler(elem)
            mode = "PILE (LIFO)"
            choix = "pile"
        else:
            structure = File()
            for elem in elements:
                structure.enfiler(elem)
            mode = "FILE (FIFO)"
            choix = "file"

    def enregistrer_clic_gauche(event):
        x, y = event.x, event.y
        if choix == "pile":
            structure.empiler((x, y))
        else:
            structure.enfiler((x, y))
        dessiner_points()

    def enregistrer_clic_droit(event):
        if choix == "pile":
            structure.depiler()
        else:
            structure.defiler()
        dessiner_points()

    def changer_mode(event):
        # Bascule entre pile et file
        if choix == "pile":
            set_mode("file")
        else:
            set_mode("pile")
        dessiner_points()

    def dessiner_fleche(x0, y0, x1, y1, taille=32, couleur="green"):
        import math
        """Dessine une flèche centrée sur le segment [x0,y0]-[x1,y1], dans le sens du déplacement."""
        mx = (x0 + x1) / 2
        my = (y0 + y1) / 2
        dx = x1 - x0
        dy = y1 - y0
        if dx == 0 and dy == 0:
            return
        angle = math.atan2(dy, dx)  # y vers le haut
        #calcul de la pointe de la flèche
        px = mx + (taille / 2) * math.cos(angle)
        py = my + (taille / 2) * math.sin(angle)
        # calcul des deux ailes
        angle_aile = math.radians(25)
        l_aile = taille / 2.5
        aile1 = (
            px - l_aile * math.cos(angle - angle_aile),
            py - l_aile * math.sin(angle - angle_aile)
        )
        aile2 = (
            px - l_aile * math.cos(angle + angle_aile),
            py - l_aile * math.sin(angle + angle_aile)
        )
        # Dessiner le corps et les ailes de la flèche
        canevas.create_line([ (mx, my), (px, py) ], fill=couleur, width=2)
        canevas.create_line([ (px, py), aile1 ], fill=couleur, width=2)
        canevas.create_line([ (px, py), aile2 ], fill=couleur, width=2)


    def dessiner_points():
        canevas.delete("all")
        canevas.create_text(
            10, 10, anchor='nw', text=mode, font=("Arial", 20, "bold"), fill="black"
        )
        rayon = 3
        points = structure.elements()
        for point in points:
            x, y = point
            canevas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill="red")
        for i in range(1, len(points)):
            x0, y0 = points[i-1]
            x1, y1 = points[i]
            canevas.create_line(x0, y0, x1, y1, fill="blue")
            dessiner_fleche(x0, y0, x1, y1, taille=32, couleur="green")

    def fermer():
        racine.destroy()
        #print(f"Structure de données : {mode}")
        #structure.affiche()

    canevas.bind("<Button-1>", enregistrer_clic_gauche)
    canevas.bind("<Button-3>", enregistrer_clic_droit)
    canevas.bind("<Button-2>", changer_mode)  # Clic molette
    racine.protocol("WM_DELETE_WINDOW", fermer)
    dessiner_points()  # Afficher le mode dès le départ
    racine.mainloop()

    return structure


if __name__ == "__main__":
    points = saisir_points_graphiquement('pile')