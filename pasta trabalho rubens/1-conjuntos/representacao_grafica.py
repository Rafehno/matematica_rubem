import matplotlib.pyplot as plt
import numpy as np


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


intersection = A.intersection(B)
union = A.union(B)


plt.figure(figsize=(8, 6))


venn_labels = [len(A), len(B), len(intersection)]
venn_circle1 = plt.Circle((-0.5, 0), 0.5, color='blue', alpha=0.5)
venn_circle2 = plt.Circle((0.5, 0), 0.5, color='red', alpha=0.5)


plt.gca().add_artist(venn_circle1)
plt.gca().add_artist(venn_circle2)


plt.xlim(-1.5, 1.5)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Representação de Conjuntos')
plt.text(-0.5, 0, 'A\n' + str(A), fontsize=12, ha='center')
plt.text(0.5, 0, 'B\n' + str(B), fontsize=12, ha='center')
plt.text(0, 0, 'A ∩ B\n' + str(intersection), fontsize=12, ha='center', color='black')


plt.show()

