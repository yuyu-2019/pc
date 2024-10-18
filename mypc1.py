# Importing the required libraries
import numpy as np
import pandas as pd
from itertools import combinations
import math
from scipy.stats import norm
import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# Constructing an undirected skeleton
def make_skeleton(V, corr_matrix, sample_num):
    node_num = len(V)
    C = np.ones((node_num, node_num))
    S = []
    for i in range(node_num):
        S.append([])
        for j in range(node_num):
            S[i].append([])

    pairs = []
    for i in range(node_num):
        for j in range(node_num - i):
            if (i != (node_num - j - 1)):
                pairs.append((i, (node_num - j - 1)))
            else:
                C[i, i] = 0

    l = -1
    while 1:
        l = l + 1
        flag = True
        for (i, j) in pairs:
            adj_set = get_adjSet(i, C, node_num)
            if (C[i][j] == 1) & (len(adj_set) >= l):
                flag = False
                adj_set.remove(j)
                combin_set = combinations(adj_set, l)
                for K in combin_set:
                    if indep_judge(i, j, list(K), corr_matrix, sample_num):
                        C[i][j] = 0
                        C[j][i] = 0
                        S[i][j] = list(K)
                        S[j][i] = list(K)
                        break
                    else:
                        continue
            else:
                continue

        if flag:
            break

    return C, S


# Determining whether i and j are mutually independent under the condition of set K
def indep_judge(i, j, K, corr_matrix, sample_num):
    indep = True
    if len(K) == 0:
        r = corr_matrix[i, j]
    else:
        corr = corr_matrix[np.ix_([i] + [j] + K, [i] + [j] + K)]
        partial_corr = np.linalg.pinv(corr)
        r = (-1 * partial_corr[0, 1]) / (math.sqrt(abs(partial_corr[0, 0] * partial_corr[1, 1])))

    r = min(0.99999, max(r, -0.99999))

    z = 0.5 * math.log1p((2 * r) / (1 - r))
    z_standard = z * math.sqrt(sample_num - len(K) - 3)

    alpha = 0.005
    if 2 * (1 - norm.cdf(abs(z_standard))) >= alpha:
        indep = True
    else:
        indep = False
    return indep


# Extending the undirected skeleton to a CPDAG
def extend_CPDAG(V, C, S):
    G = C
    node_num = len(V)

    pairs = []
    for i in range(node_num):
        for j in range(node_num):
            if (i != j):
                if (C[i][j] == 1):
                    pairs.append((i, j))

    triples = []
    for (i, j) in pairs:
        for k in range(node_num):
            if (C[j][k] == 1) & (k != i):
                triples.append([i, j, k])

    for [i, j, k] in triples:
        if (G[i][j] == 1) & (G[j][i] == 1) & (G[k][j] == 1) & (G[j][k] == 1) & (G[i][k] == 0) & (
                G[k][i] == 0):
            if j not in S[i][k]:
                G[j][i] = 0
                G[j][k] = 0

    for [i, j, k] in triples:
        if (G[i][j] == 1) & (G[j][i] == 0) & (G[k][j] == 1) & (G[j][k] == 1) & (G[i][k] == 0) & (
                G[k][i] == 0):
            G[k][j] = 0

    for [i, j, k] in triples:
        if (G[i][j] == 1) & (G[j][i] == 0) & (G[j][k] == 1) & (G[k][j] == 0) & (G[i][k] == 1) & (
                G[k][i] == 1):
            G[k][i] = 0

    for [i, j, k] in triples:
        for [l, m, n] in triples:
            if (i == l) & (k == n):
                if (G[i][j] == 1) & (G[j][i] == 1) & (G[i][m] == 1) & (G[m][i] == 1) & (G[j][k] == 1
                ) & (G[k][j] == 0) & (G[m][k] == 1) & (G[k][m] == 0) & (G[i][k] == 1) & (G[k][i] == 1):
                    G[k][i] = 0

    for [i, j, k] in triples:
        for [l, m, n] in triples:
            if (j == l) & (k == m):
                if (G[i][j] == 1) & (G[j][i] == 1) & (G[j][k] == 1) & (G[k][j] == 0) & (G[k][n] == 1
                ) & (G[n][k] == 0) & (G[i][n] == 1) & (G[n][i] == 1):
                    G[n][i] = 0

    return G


# Getting the adjacent set of node i in graph G
def get_adjSet(i, G, node_num):
    adj = []
    for j in range(node_num):
        if G[i][j] == 1:
            adj.append(j)
    return adj


# Drawing the graph using networkx
def Draw(DAG, nodes, pdf_pages):
    G = nx.DiGraph()
    nodes = nodes.tolist()
    G.add_nodes_from(nodes)
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if DAG[i][j] == 1:
                G.add_edge(nodes[i], nodes[j])
    nx.draw(G, with_labels=True)
    pdf_pages.savefig()
    plt.close()


def PC(data_path):
    df = pd.read_excel(data_path, index_col=False)

    corr = df.corr().values
    sample_num = df.values.shape[0]

    node = df.columns.values

    skeleton, separate = make_skeleton(node, corr, sample_num)
    CPDAG = extend_CPDAG(node, skeleton, separate)

    # Save CPDAG to PDF
    with PdfPages("CPDAG.pdf") as pdf_pages:
        Draw(CPDAG, node, pdf_pages)

    return CPDAG


if __name__ == '__main__':
    data_path = r"C:\Users\26318\Desktop\causal\Research Team\data.xlsx"
    PC(data_path)
