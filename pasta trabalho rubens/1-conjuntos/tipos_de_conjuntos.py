#Conjunto finito.
A = {1, 2, 3, 4, 5}  
print(f'Conjunto Finito A: {A}')

#Conjunto innfinito.
import itertools

naturais = itertools.count(start=1, step=1)
print("Exemplo de um conjunto infinito de números naturais:", next(naturais), next(naturais), next(naturais))

#Conjunto vazio
vazio = ''
print("Conjunto Vazio:", vazio)

#Conjunto unitario
unitario = {42}  
print("Conjunto Unitario:", unitario)

#conjunto universo (Um conjunto que contém todos os elementos possíveis dentro de um contexto)
universo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Conjunto Universo:", universo)

#Conjuntos iguais
conjunto_a = {1, 2, 3, 4}
conjunto_b = {4, 3, 2, 1}

sao_iguais = conjunto_a == conjunto_b

if sao_iguais:
    print("Os conjuntos são iguais.")
else:
    print("Os conjuntos são diferentes.")
    
#Subconjuntos
B = {1, 2, 3}  
print("Subconjunto B de A:", B.issubset(universo))

#Reunião de conjuntos
conjunto_c = {1, 2, 3}
conjunto_d = {3, 4, 5}

uniao = conjunto_c.union(conjunto_d)
print("A união dos conjuntos é:", uniao)

#Interseção de conjuntos

conjunto_e = {1, 2, 3, 4}
conjunto_f = {3, 4, 5, 6}

intersecao = conjunto_e.intersection(conjunto_f)
print("A interseção dos conjuntos é:", intersecao)

# Conjunto disjunto
C = {11, 12, 13}  
print("Conjuntos A e C são disjuntos?", A.isdisjoint(C))

# Diferença de conjuntos
conjunto_g = {1, 2, 3, 4}
conjunto_h = {3, 4, 5, 6}

diferenca = conjunto_g.difference(conjunto_h)
print("A diferença do conjunto A em relação ao conjunto B é:", diferenca)









