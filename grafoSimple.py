import networkx as nx
import random
import matplotlib.pyplot as plt


def rect(lis1, lis2, r1, r2):
    for i in range(len(lis1)):
        if (lis1[i] == r1 and lis2[i] == r2) or (lis1[i] == r2 and lis2[i] == r1):
            return True
    return False


def rando(tam, cont, k):
    random_1 = random.randrange(tam)
    conteoEmergencia = 0
    while cont[random_1] + 1 > k and conteoEmergencia < 200:
        conteoEmergencia += 1
        random_1 = random.randrange(tam)
    if conteoEmergencia == 200:
        return -1, -1
    random_i = random.randrange(tam)
    conteoEmergencia = 0
    while (random_1 == random_i or cont[random_i] + 1 > k) and conteoEmergencia < 200:
        conteoEmergencia += 1
        random_i = random.randrange(tam)
    if conteoEmergencia == 200:
        return -1, -1
    return random_1, random_i


def mainGrafo(v, a, k):
    G = nx.Graph()
    cont = [0] * v
    st = []
    fl = []
    tupla = ()
    conteoEmergencia = 0

    for i in range(a):
        tupla = rando(v, cont, k)
        conteoEmergencia = 0
        while tupla[0] != -1 and rect(st, fl, tupla[0], tupla[1]) and conteoEmergencia < 200:
            conteoEmergencia += 1
            tupla = rando(v, cont, k)
        if tupla[0] == -1 or conteoEmergencia == 200:
            break
        cont[tupla[0]] += 1
        cont[tupla[1]] += 1
        st.append(tupla[0])
        fl.append(tupla[1])

    if tupla[0] == -1 or conteoEmergencia == 200:
        cont = [0] * v
        st = []
        fl = []
        while len(st) != a:
            i = 0
            for i in range(v):
                con = (i + 1) % v
                while rect(st, fl, i, con):
                    con = (con + 1) % v
                st.append(i)
                fl.append(con)

    if len(st) != a:
        return False

    for j in range(len(st)):
        G.add_edge(st[j], fl[j])

    for h in range(v):
        if cont[h] == 0:
            G.add_node(h)

    nx.draw_circular(G, with_labels=True, node_color="lightblue", edge_color="chocolate", font_color="black")

    plt.savefig('grafo.png', facecolor="#00000F")
    plt.clf()
    plt.close()
    return True