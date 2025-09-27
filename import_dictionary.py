filename = "words_alpha.txt"

with open(filename) as f:
    all_lines = f.readlines()

lex = []
for line in all_lines:
    lex.append(line.rstrip())

