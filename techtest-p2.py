#!/usr/bin/env python3

# PART 2
import Levenshtein

# On ouvre le fichier
with open('input.txt', 'r') as f:
    # On lit le fichier
    lines = f.readlines()
    # On crée un tableau qui va contenir nos chaînes
    input_text = []

    # De quoi se débarasser des \n en fin de ligne et on rentre tout ça dans
    # input_text
    for line in lines:
        input_text.append("".join(line.strip()))

    # On vient bouler sur les chaînes
    for s1 in input_text:
        # Et on boucle chaque chaîne sur les autres chaînes
        for s2 in input_text:
            # On calcule la distance entre deux chaînes grâce au calcul de Levenshtein
            distance = Levenshtein.distance(s1, s2, score_cutoff=1)
            # Si la distance n'est que de un, on a nos deux boîtes gagnantes, on les affiche
            if distance == 1:
                print(s1)
                # lujnogabetp{u}msydyfcovzixaw & lujnogabetp{r}msydyfcovzixaw

# On ferme notre fichier
f.close()
