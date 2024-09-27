import matplotlib.pyplot as plt
from matplotlib_venn import venn2


conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}


plt.figure(figsize=(8, 6))
venn = venn2([conjunto_A, conjunto_B], ('Conjunto A', 'Conjunto B'))


plt.title("Diagrama de Venn")


venn.get_label_by_id('10').set_text('1, 2, 3')   # Apenas A
venn.get_label_by_id('01').set_text('6, 7, 8')   # Apenas B
venn.get_label_by_id('11').set_text('4, 5')      # A ∩ B

plt.show()
