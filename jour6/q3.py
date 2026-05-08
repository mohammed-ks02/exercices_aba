def solution(a, k):
    n = len(a)
    # Initialisation : somme des pairs dans les k premiers éléments
    somme_pairs = 0
    for i in range(k):
        if a[i] % 2 == 0:
            somme_pairs += a[i]
    
    result = [somme_pairs]
    
    # Glissement de la fenêtre
    for i in range(k, n):
        # On sort l'élément a[i-k]
        if a[i - k] % 2 == 0:
            somme_pairs -= a[i - k]
        # On ajoute l'élément a[i]
        if a[i] % 2 == 0:
            somme_pairs += a[i]
        result.append(somme_pairs)
    
    return result