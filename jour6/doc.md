Voici la documentation demandée, structurée par question, avec objectif, logique générale, puis explication détaillée ligne par ligne du code.

---

## Question 1 – Manipulation de tableau

### Objectif
Produire un tableau `b` de même longueur que `a` où chaque élément `b[i]` est la somme de `a[i-1] + a[i] + a[i+1]`, en considérant `0` pour les indices manquants (début ou fin de tableau).

### Logique du code
- On détermine la longueur `n` du tableau d’entrée.
- On initialise un tableau `b` rempli de zéros.
- Pour chaque position `i` :
  - On récupère l’élément de gauche : `a[i-1]` si `i > 0`, sinon `0`.
  - On récupère l’élément central : `a[i]`.
  - On récupère l’élément de droite : `a[i+1]` si `i < n-1`, sinon `0`.
  - On calcule la somme et on la place dans `b[i]`.
- On retourne `b`.

### Code – explication ligne par ligne

```python
def solution(a):
    # Récupère la longueur du tableau d'entrée
    n = len(a)
    
    # Crée un tableau de sortie b de même taille, rempli de 0
    b = [0] * n
    
    # Parcourt chaque indice du tableau a
    for i in range(n):
        # Élément de gauche : s'il n'existe pas (i == 0), on prend 0
        gauche = a[i-1] if i > 0 else 0
        
        # Élément central
        centre = a[i]
        
        # Élément de droite : s'il n'existe pas (i == n-1), on prend 0
        droite = a[i+1] if i < n-1 else 0
        
        # Somme des trois et affectation dans b
        b[i] = gauche + centre + droite
    
    # Retourne le tableau résultat
    return b
```

---

## Question 2 – Correspondance de motif dans une chaîne

### Objectif
Compter combien de sous‑chaînes de `source` (de même longueur que `pattern`) vérifient que :
- `'0'` dans `pattern` correspond à une voyelle (`a, e, i, o, u, y`) dans la sous‑chaîne,
- `'1'` correspond à une consonne (toute lettre qui n’est pas une voyelle).

### Logique du code
- On définit un ensemble des voyelles.
- Si `pattern` est plus long que `source`, il n’y a aucune sous‑chaîne possible → retourne 0.
- On parcourt toutes les positions de départ possibles dans `source` (de 0 à `len(source)-len(pattern)`).
- Pour chaque position, on compare caractère par caractère avec le motif.
- Si toutes les positions correspondent, on incrémente un compteur.
- On retourne le compteur.

### Code – explication ligne par ligne

```python
def solution(pattern, source):
    # Ensemble des voyelles (minuscules, avec 'y' inclus)
    voyelles = set('aeiouy')
    
    # Longueurs respectives
    len_p = len(pattern)
    len_s = len(source)
    
    # Si le motif est plus long que la source, aucune sous-chaîne possible
    if len_p > len_s:
        return 0
    
    # Compteur de sous-chaînes valides
    count = 0
    
    # Parcourt tous les indices de début possibles dans source
    for i in range(len_s - len_p + 1):
        # Drapeau indiquant si la sous-chaîne courante correspond
        ok = True
        
        # Compare chaque caractère de la sous-chaîne avec le motif
        for j in range(len_p):
            c = source[i + j]           # caractère de la source
            if pattern[j] == '0':
                # Doit être une voyelle
                if c not in voyelles:
                    ok = False
                    break
            else:  # pattern[j] == '1'
                # Doit être une consonne
                if c in voyelles:
                    ok = False
                    break
        
        # Si la sous-chaîne entière correspond, on incrémente le compteur
        if ok:
            count += 1
    
    return count
```

---

## Question 3 – Somme des nombres pairs dans des sous‑tableaux de taille k

### Objectif
Retourner un tableau où chaque élément est la somme des entiers pairs de chaque sous‑tableau consécutif de longueur `k` du tableau `a`.

### Logique du code (fenêtre glissante)
1. Calculer la somme des pairs de la première fenêtre (indices 0 à k-1).
2. Stocker cette somme dans le résultat.
3. Glisser la fenêtre d’un pas vers la droite :
   - Si l’élément qui sort de la fenêtre est pair, on le soustrait de la somme courante.
   - Si le nouvel élément qui entre est pair, on l’ajoute à la somme courante.
   - On ajoute la nouvelle somme au résultat.
4. Retourner le tableau des sommes.

### Code – explication ligne par ligne

```python
def solution(a, k):
    # Longueur du tableau
    n = len(a)
    
    # --- Première fenêtre (indices 0 à k-1) ---
    somme_pairs = 0
    for i in range(k):          # parcourt les k premiers éléments
        if a[i] % 2 == 0:       # si l'élément est pair
            somme_pairs += a[i] # on l'ajoute à la somme
    
    # Initialise le tableau résultat avec la somme de la première fenêtre
    result = [somme_pairs]
    
    # --- Fenêtres suivantes (de i = k à n-1) ---
    for i in range(k, n):
        # Élément qui quitte la fenêtre : a[i-k]
        if a[i - k] % 2 == 0:
            somme_pairs -= a[i - k]   # on le retire s'il était pair
        
        # Élément qui entre dans la fenêtre : a[i]
        if a[i] % 2 == 0:
            somme_pairs += a[i]       # on l'ajoute s'il est pair
        
        # Ajoute la nouvelle somme au tableau résultat
        result.append(somme_pairs)
    
    return result
```