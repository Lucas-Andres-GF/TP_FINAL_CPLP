original = [[1, 2, 3], [4, 5, 6]]
copia = original[:]

original[0][0] = 'a'

print(original)  # [['a', 2, 3], [4, 5, 6]]
print(copia) 