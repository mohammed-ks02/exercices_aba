note = float(input("Entrez une note sur 20 : "))

if note >= 16:
    print("Résultat : Excellent")
elif note >= 14:
    print("Résultat : Bien")
elif note >= 12:
    print("Résultat : Assez bien")
elif note >= 10:
    print("Résultat : Passable")
else:
    print("Résultat : Non validé")
