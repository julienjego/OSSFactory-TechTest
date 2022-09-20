#!/usr/bin/env python3

# PART 1
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()
    input_text = []
    group_text = []
    regex = re.compile(r'([a-z])\1{1,2}')

    for line in lines:
        input_text.append("".join(sorted(line.strip())))

    for el in input_text:
        group_text.append([match.group() for match in regex.finditer(el)])

    total_two_dupl = 0
    total_three_dupl = 0

    for node in group_text:
        two_dupl = 0
        three_dupl = 0
        for i in node:
            if len(i) == 2:
                two_dupl += 1
            elif len(i) == 3:
                three_dupl += 1
        if two_dupl > 0:
            total_two_dupl += 1
        if three_dupl > 0:
            total_three_dupl += 1

    print("La valeur du checksum est : " +
          str(total_two_dupl*total_three_dupl))

f.close()
