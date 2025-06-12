from module_pile_file import Noeud, Pile, File
from module_saisir_points_vers_pile_file_Tkinter import saisir_points_graphiquement

''' Lors de l'exécution de la fonction saisir_points_graphiquement :
* clic molette pour changer de structure de données File / Pile
* clic gauche pour ajouter un point
* clic droit pour supprimer un point
    - dans une file, on supprime la tête de file (le premier élément entré)
    - dans une pile, on supprime le sommet de la pile (le dernier élément entré)
'''

# créer une structure de données de type file ou pile (au choix)
points = saisir_points_graphiquement('pile')
points.affiche()

# on peut convertir une pile en file et réciproquement
if isinstance(points,Pile):
    points_file = points.vers_file()
    points_file.affiche()

if isinstance(points,File):
    points_pile = points.vers_pile()
    points_pile.affiche()


