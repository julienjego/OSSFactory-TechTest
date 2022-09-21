#!/usr/bin/env python3

# PART 1
import re

# On ouvre le fichier
with open('input.txt', 'r') as f:
    # On lit le fichier
    lines = f.readlines()
    # On crée deux tableaux qui vont contenir nos chaînes
    input_text = []
    group_text = []
    # Une regex pour repérer les caractères répétés dans les chaînes
    regex = re.compile(r'([a-z])\1{1,2}')

    # De quoi se débarasser des \n en fin de ligne et trier par ordre
    # alphabétique les chaînes puis on rentre tout ça dans input_text
    for line in lines:
        input_text.append("".join(sorted(line.strip())))

    # On récupère seulement les caractères répétés deux ou trois fois et on les
    # intègre dans group_text
    for el in input_text:
        group_text.append([match.group() for match in regex.finditer(el)])

    # Les variables qui vont permettre de calculer le checksum
    total_two_dupl = 0
    total_three_dupl = 0

    # On récupère dans un premier temps combien de fois on trouve deux et trois
    # caractères répétés par ligne
    for node in group_text:
        two_dupl = 0
        three_dupl = 0
        for i in node:
            if len(i) == 2:
                two_dupl += 1
            elif len(i) == 3:
                three_dupl += 1

        # Et peu importe le nombre de duplicats, on regarde juste s'il y en a
        # au moins un pour les caractères répétés deux et trois fois et on
        # incrémente de 1 les totaux
        if two_dupl > 0:
            total_two_dupl += 1
        if three_dupl > 0:
            total_three_dupl += 1

    # Enfin on vient afficher le résultat
    print("La valeur du checksum est : " +
          str(total_two_dupl*total_three_dupl))  # La valeur du checksum est : 9633

# On ferme notre fichier
f.close()
