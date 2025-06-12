import tkinter as tk
from tkinter import simpledialog

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class Pile:
    def __init__(self):
        self.sommet = None

    def empiler(self, valeur):
        nouveau_noeud = Noeud(valeur)
        nouveau_noeud.suivant = self.sommet
        self.sommet = nouveau_noeud

    def depiler(self):
        if self.sommet is None:
            return None
        valeur = self.sommet.valeur
        self.sommet = self.sommet.suivant
        return valeur

    def est_vide(self):
        return self.sommet is None

    def elements(self):
        elements = []
        courant = self.sommet
        while courant is not None:
            elements.append(courant.valeur)
            courant = courant.suivant
        elements.reverse()
        return elements

    def __repr__(self):
        chaine = ''
        courant = self.sommet
        while courant.suivant !=None:   #n'affichera pas la valeur du fond de la pile
            chaine += f"║{str(courant.valeur):^16}║\n"
            courant = courant.suivant
        chaine += f"║{str(courant.valeur):^16}║\n"
        chaine += "╚"+"═"*16+"╝"
        return chaine
    
    def affiche(self):
        '''affiche le contenu de la pile sans rien dépiler'''
        print(self)

class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def enfiler(self, valeur):
        nouveau_noeud = Noeud(valeur)
        if self.queue is None:
            self.tete = nouveau_noeud
            self.queue = nouveau_noeud
        else:
            self.queue.suivant = nouveau_noeud
            self.queue = nouveau_noeud

    def defiler(self):
        if self.tete is None:
            return None
        valeur = self.tete.valeur
        self.tete = self.tete.suivant
        if self.tete is None:
            self.queue = None
        return valeur

    def est_vide(self):
        return self.tete is None

    def elements(self):
        elements = []
        courant = self.tete
        while courant is not None:
            elements.append(courant.valeur)
            courant = courant.suivant
        return elements

    def __repr__(self):
        chaine = ''
        if not self.est_vide():
            courant = self.tete
            while courant.suivant !=None:
                chaine = ' > ' + str(courant.valeur) + chaine
                courant = courant.suivant
            chaine = str(courant.valeur) + chaine
        else:
            chaine="la file est vide"
        return chaine

    def affiche(self):
        '''affiche le contenu de la file sans rien défiler'''
        print(self)
        
def main():
    racine = tk.Tk()
    racine.withdraw()

    #choix = simpledialog.askstring("Choix de la structure", "Tapez 'pile' (LIFO) ou 'file' (FIFO) :")
    choix = 'file'

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
    racine.title(f"Cliquez pour tracer le parcours — {mode}")

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

    def fermer():
        racine.destroy()
        print(f"Parcours ({mode}) :")
        for point in structure.elements():
            print(point)
        print(structure.elements())
        structure.affiche()

    canevas.bind("<Button-1>", enregistrer_clic_gauche)
    canevas.bind("<Button-3>", enregistrer_clic_droit)
    canevas.bind("<Button-2>", changer_mode)  # Clic molette
    racine.protocol("WM_DELETE_WINDOW", fermer)
    dessiner_points()  # Afficher le mode dès le départ
    racine.mainloop()
    
    

if __name__ == "__main__":
    main()
