Dans une classe, si on code la  méthode `__repr__` mais pas la méthode `__str__`, on obtient le même affichage dans la console avec `print(p)`, `p`, `str(p)` ou `repr(p)`.  
On peut donc éviter de définir une méthode `__str__` et le code en est plus court.  

``` python
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __eq__(self, autre):
        return self.nom == autre.nom and self.prenom == autre.prenom
    def __repr__(self):
        return f"nom: {self.nom}, prenom: {self.prenom}"

p = Personne("Turing", "Alan")
```

Cependant, `repr` et `str` n’ont pas le même objectif.  
`str` permet d’obtenir une chaîne de caractères lisible et compréhensible pour l’affichage.  
`repr` doit renvoyer, (d’après la doc Python), à partir d’une
instance `p` une chaîne de caractères `ch = repr(p)` affichable, avec si possible la condition que `eval(ch)` produit une instance `q` de même valeur que `p` (donc égale à p si on a défini une méthode `__eq__ `convenable).  
Dans l’exemple, `q = eval(repr(p))` produit une `SyntaxError`  
Donc soit on ne définit que `__str__`, soit on définit` __str__` et `__repr__`, par exemple:

``` python
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __eq__(self, autre):
        return self.nom == autre.nom and self.prenom == autre.prenom
    def __repr__(self):
        return f"Personne('{self.nom}', '{self.prenom}')"
    def __str__(self):
        return f"nom: {self.nom}, prenom: {self.prenom}"

p = Personne("Turing", "Alan")
q = eval(repr(p)
print(q == p) # affiche True, puisque p et q ont les mêmes valeurs d'attributs (méthode __eq__)
print(q is p) # affiche False, puisque p et q sont deux objets différents


```
