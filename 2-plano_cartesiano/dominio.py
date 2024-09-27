import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 400)  # 400 pontos entre -10 e 10


y = x ** 2  # f(x) = x^2

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x^2', color='blue')
plt.title('Gráfico da Função f(x) = x^2')
plt.xlabel('x (domínio)')
plt.ylabel('f(x) (imagem)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # Eixo x
plt.axvline(0, color='black', lw=0.5, ls='--')  # Eixo y
plt.grid()
plt.legend()
plt.xlim(-10, 10)
plt.ylim(0, 100)
plt.show()
