class Point:
    def __init__(self,abscisse,ordonnee):
        self.x = abscisse
        self.y = ordonnee

    def get_coord(self):
        return (self.x,self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Vecteur:
    def __init__(self,a,b):
        if (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)):
            # vecteur défini par ses composantes
            self.x = a
            self.y = b
        if isinstance(a,tuple) and isinstance(b,tuple) :
            # vecteur défini par deux points donnés par un tuple
            self.x = b[0]-a[0]
            self.y = b[1]-a[1]
        if isinstance(a,Point) and isinstance(b,Point) :
            # vecteur défini par deux points
            self.x = b.x-a.x
            self.y = b.y-a.y

        # Norme en tant qu'attribut de classe
        self.norme = (self.x*self.x+self.y*self.y)**0.5     # variable accessible en dehors de la classe
        self._norme = (self.x*self.x+self.y*self.y)**0.5    # variable accessible en dehors de la classe
        self.__norme = (self.x*self.x+self.y*self.y)**0.5   # variable non-accessible en dehors de la classe par self.__norme
                                                            # mais accessible en dehors de la classe par self._Vecteur__norme
                                                            # variable accessible à l'intérieur de la classe par self.__norme

    def __repr__(self):
        return f'Vecteur({self.x},{self.y})'

    def __str__(self):
        return f'Vecteur({self.x},{self.y})'

    def __add__(self,other):
        return Vecteur(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vecteur(self.x - other.x, self.y - other.y)

    def __mul__(self,other):
        # produit scalaire
        return self.x*other.x + self.y*other.y

    def get_norme(self):
        # Norme en tant que méthode de classe
        # norme(v) = sqrt(v.v)
        return  (self*self)**0.5

    def normaliser(self):
        n = self.get_norme()
        if n != 0:
            return Vecteur(self.x/n,self.y/n)

    def get_coord(self):
        return (self.x,self.y)

    def is_orth(self,other):
        return self*other == 0

    def is_colin(self,other):
        return self.x*other.y == self.y*other.x



A = Point(3,2)
B = Point(9,8)

v1 = Vecteur(5,6)
v2 = Vecteur((1,1),(6,-9))
v3 = Vecteur(A,B)