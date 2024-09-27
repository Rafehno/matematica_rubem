#conjuntos A e B
A = {1, 2, 3}
B = {2, 3, 4}

# União
uniao = A.union(B)
print("União (A ∪ B):", uniao)

# Interseção
interseccao = A.intersection(B)
print("Interseção (A ∩ B):", interseccao)

# Diferença
diferenca = A.difference(B)
print("Diferença (A - B):", diferenca)

# Complemento (A')
U = {1, 2, 3, 4, 5}
complemento = U.difference(A)
print("Complemento (A'):", complemento)

