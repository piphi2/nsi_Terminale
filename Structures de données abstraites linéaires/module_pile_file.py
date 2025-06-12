
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class Pile:
    ''' créé une structure de données de type pile (LIFO)
        les primitives sont : .empiler(valeur), .depiler(), .est_vide()
        méthodes additionnelles : .affiche() et .elements()'''
    def __init__(self):
        self.sommet = None

    def empiler(self, valeur):
        '''Ajoute valeur au sommet de la pile'''
        nouveau_noeud = Noeud(valeur)
        nouveau_noeud.suivant = self.sommet
        self.sommet = nouveau_noeud

    def depiler(self):
        '''Renvoie le sommet de la pile et le supprime de la pile'''
        if self.sommet is None:
            return None
        valeur = self.sommet.valeur
        self.sommet = self.sommet.suivant
        return valeur

    def est_vide(self):
        ''' Renvoie True si la pile est vide, False sinon'''
        return self.sommet is None

    def elements(self):
        ''' Renvoie une liste (type list) des éléments de la pile
        Le premier élément de la liste est le fond de la pile
        Le dernier élément de la liste est le sommet de la pile'''
        elements = []
        courant = self.sommet
        while courant is not None:
            elements.append(courant.valeur)
            courant = courant.suivant
        elements.reverse()
        return elements


    def affiche(self):
        '''affiche le contenu de la pile sans rien dépiler'''
        if self.est_vide:
            print('')
        chaine = ''
        courant = self.sommet
        while courant.suivant !=None:   #n'affichera pas la valeur du fond de la pile
            chaine += f"║{str(courant.valeur):^16}║\n"
            courant = courant.suivant
        chaine += f"║{str(courant.valeur):^16}║\n"
        chaine += "╚"+"═"*16+"╝"
        print(chaine)


    def vers_file(self):
        p = Pile()
        # on vide la pile dans une autre pile pour la retourner
        while not self.est_vide():
            v = self.depiler()
            p.empiler(v)
        p2 = Pile()
        f = File()
        # on remet la pile à l'endroit et on remplit la file
        while not p.est_vide():
            v = p.depiler()
            f.enfiler(v)
            self.empiler(v)
        return f



class File:
    ''' créé une structure de données de type file (FIFO)    '''
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
        ''' Renvoie True si la file est vide, False sinon'''
        return self.tete is None

    def elements(self):
        ''' Renvoie une liste (type list) des éléments de la file
        Le premier élément de la liste est la tête de la file
        Le dernier élément de la liste est la queue de la file'''
        elements = []
        courant = self.tete
        while courant is not None:
            elements.append(courant.valeur)
            courant = courant.suivant
        return elements

    def affiche(self):
        '''affiche le contenu de la file sans rien défiler'''
        chaine = ''
        if not self.est_vide():
            courant = self.tete
            while courant.suivant !=None:
                chaine = ' >> ' + str(courant.valeur) + chaine
                courant = courant.suivant
            chaine = str(courant.valeur) + chaine
        else:
            chaine="la file est vide"
        print(chaine)

    def vers_pile(self):
        p = Pile()
        f = File()
        # on vide la file dans une autre file et on remplit la pile
        while not self.est_vide():
            v = self.defiler()
            p.empiler(v)
            f.enfiler(v)
        self = f
        return p


####################  TEST  ######################
if __name__ == "__main__":
    ma_pile = Pile()
    ma_pile.empiler(26)
    ma_pile.empiler(45)
    ma_pile.empiler(64)
    ma_pile.empiler(99)

    print("Contenu de la pile :")
    ma_pile.affiche()

    f = ma_pile.vers_file()
    f.affiche()
    p = f.vers_pile()
    p.affiche()



