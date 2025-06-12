🧠 Programmation orientée objet : Modélisation d’un parcours dans le plan

Objectifs pédagogiques

* Mettre en œuvre les principes de la programmation orientée objet en Python.
* Concevoir des classes simples représentant des objets mathématiques (point, vecteur, chemin).
* Appliquer la relation de Chasles pour modéliser un déplacement global à partir de déplacements élémentaires.

Contexte

On souhaite modéliser un parcours dans une grille de taille 1024×1024 pixels, comme si on suivait un chemin point par point. On utilisera la programmation orientée objet pour structurer ce parcours.

Travail demandé

Vous devez implémenter trois classes en Python :

1. La classe Point

Représente un point dans le plan.

Attributs :

* x : coordonnée entière horizontale
* y : coordonnée entière verticale

Méthodes attendues :

* **init**(self, x, y)
* **sub**(self, autre) → renvoie le vecteur allant de autre vers self.
* **add**(self, vecteur) → renvoie un nouveau point obtenu en appliquant le vecteur au point.
* **repr**(self) → représentation lisible du point.

2. La classe Vecteur

Représente un déplacement (dx, dy) dans le plan.

Attributs :

* dx : déplacement horizontal
* dy : déplacement vertical

Méthodes attendues :

* **init**(self, dx, dy)
* **add**(self, autre) → renvoie la somme de deux vecteurs.
* **repr**(self) → représentation lisible du vecteur.

3. La classe Chemin

Représente une suite ordonnée de points.

Attributs :

* points : liste de points

Méthodes attendues :

* ajouter(self, point) → ajoute un point à la suite du chemin.
* vecteurs(self) → renvoie la liste des vecteurs entre les points consécutifs.
* chasles(self, i, j) → applique la relation de Chasles : renvoie le vecteur allant du point i au point j (i < j), comme somme des vecteurs intermédiaires.

Relation de Chasles

Pour trois points A, B et C, la relation de Chasles s’écrit :

  AC = AB + BC

Elle permet de calculer le vecteur allant de A à C en sommant les vecteurs intermédiaires. Par extension, dans un chemin :

  Vecteur(Pi → Pj) = Vecteur(Pi → Pi+1) + Vecteur(Pi+1 → Pi+2) + … + Vecteur(Pj-1 → Pj)

Exemple d’utilisation

chemin = Chemin()
chemin.ajouter(Point(10, 20))
chemin.ajouter(Point(13, 22))
chemin.ajouter(Point(16, 25))
chemin.ajouter(Point(20, 30))

print("Vecteurs élémentaires :", chemin.vecteurs())
print("Vecteur de 0 à 3 :", chemin.chasles(0, 3))

Extensions possibles (facultatif)

* Ajouter une méthode distance(self) dans Vecteur, qui retourne la norme du vecteur (longueur du déplacement).
* Permettre d’enregistrer ou de lire un chemin à partir d’un fichier texte (exercice d’entrée/sortie).
* Afficher graphiquement le chemin à l’aide de Tkinter.

Critères d’évaluation

* Organisation et clarté du code
* Respect des signatures et du cahier des charges
* Usage correct des méthodes spéciales **add**, **sub**, etc.
* Qualité de la documentation et des exemples
* Bon usage de la relation de Chasles

