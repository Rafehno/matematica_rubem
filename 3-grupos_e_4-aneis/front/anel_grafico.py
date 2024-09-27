# front/anel_grafico.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matplotlib.pyplot as plt
import networkx as nx

from back.anel import tabela_adicao_anel, tabela_multiplicacao_anel

def visualizar_anel(n):
    """
    Visualiza o anel Z/nZ usando um gráfico onde cada elemento é um nó.
    :param n: Módulo para o anel
    """
    G = nx.Graph()
    
    # Adicionando nós para cada elemento do anel
    for i in range(n):
        G.add_node(i)

    # Adicionando arestas com base na tabela de adição
    add_table = tabela_adicao_anel(n)
    for i in range(n):
        for j in range(n):
            result = add_table[i][j]
            G.add_edge(i, result, label='+' + str(j))

    # Plotando o gráfico de adição
    pos = nx.spring_layout(G)  # Layout para o gráfico
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
    
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f'Visualização do Anel Z/{n}Z (Adição)')
    plt.show()

    # Repetindo para a multiplicação
    G.clear()  # Limpa o gráfico anterior

    # Adicionando nós para cada elemento do anel
    for i in range(n):
        G.add_node(i)

    # Adicionando arestas com base na tabela de multiplicação
    mult_table = tabela_multiplicacao_anel(n)
    for i in range(n):
        for j in range(n):
            result = mult_table[i][j]
            G.add_edge(i, result, label='*' + str(j))

    # Plotando o gráfico de multiplicação
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=10)
    
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f'Visualização do Anel Z/{n}Z (Multiplicação)')
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    visualizar_anel(6)  # Visualiza o anel Z/6Z
