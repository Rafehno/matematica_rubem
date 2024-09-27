import matplotlib.pyplot as plt


plt.figure()

#linhas dos eixos X e Y
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)


plt.xlim(-7, 7)
plt.ylim(-7, 7)

#grade
plt.grid(True)


plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')


pontos_x = [2]
pontos_y = [3]


plt.scatter(pontos_x, pontos_y, color='red', label='Pontos', s=100)


#Cria a imagem do plano cartesiano
plt.savefig('plano_cartesiano.png', format='png')

plt.legend()

plt.show()
