def calculer_moyenne(notes):
    return sum(notes) / len(notes)

notes_liste = [12, 15, 18, 10]
moyenne = calculer_moyenne(notes_liste)
print(moyenne)
