
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def carregar_dados(caminho_csv):
    """Lê os dados do arquivo CSV e retorna o DataFrame."""
    return pd.read_csv(caminho_csv)

def criar_grafo(df):
    """Cria e retorna um grafo direcionado a partir dos dados."""
    G = nx.DiGraph()
    for _, row in df.iterrows():
        npc1 = row["NPC1_Name"]
        npc2 = row["NPC2_Name"]
        rel_type = row["Relationship_Type"]
        G.add_edge(npc1, npc2, label=rel_type)
    return G

def calcular_metricas(G):
    """Calcula e retorna várias métricas de centralidade."""
    metrics = {
        "degree_centrality": nx.degree_centrality(G),
        "betweenness_centrality": nx.betweenness_centrality(G),
        "closeness_centrality": nx.closeness_centrality(G),
        "eigenvector_centrality": nx.eigenvector_centrality(G, max_iter=1000),
    }
    return metrics

def obter_top_conectados(metric, top_n=10):
    """Retorna os top_n NPCs mais conectados pela métrica fornecida."""
    return sorted(metric.items(), key=lambda x: x[1], reverse=True)[:top_n]

def analisar_componentes(G):
    """Retorna o número de componentes fracas e o tamanho da maior componente."""
    componentes = list(nx.weakly_connected_components(G))
    return len(componentes), max(len(c) for c in componentes)

def salvar_metricas_csv(metrics, caminho_arquivo):
    """Salva as métricas combinadas em um arquivo CSV."""
    df = pd.DataFrame({
        "NPC": list(metrics["degree_centrality"].keys()),
        "Degree Centrality": list(metrics["degree_centrality"].values()),
        "Betweenness Centrality": list(metrics["betweenness_centrality"].values()),
        "Closeness Centrality": list(metrics["closeness_centrality"].values()),
        "Eigenvector Centrality": list(metrics["eigenvector_centrality"].values())
    })
    df.sort_values(by="Degree Centrality", ascending=False, inplace=True)
    df.to_csv(caminho_arquivo, index=False)
    return df

def densidade_rede(G):
    """Calcula a densidade da rede."""
    return nx.density(G)

# Exemplo de execução principal
if __name__ == "__main__":
    caminho = "processed_relationships.csv"
    df = carregar_dados(caminho)
    G = criar_grafo(df)
    metrics = calcular_metricas(G)
    densidade = densidade_rede(G)
    num_componentes, maior_componente = analisar_componentes(G)
    top_npcs = obter_top_conectados(metrics["degree_centrality"])
    salvar_metricas_csv(metrics, "metrics_npc_skyrim.csv")

    print("Resumo da Rede:")
    print(f"Número de NPCs: {G.number_of_nodes()}")
    print(f"Número de relações: {G.number_of_edges()}")
    print(f"Densidade: {densidade:.5f}")
    print(f"Componentes conexas: {num_componentes}")
    print(f"Tamanho da maior componente: {maior_componente}")
    print("Top 10 NPCs mais conectados:")
    for npc, val in top_npcs:
        print(f"{npc}: {val:.4f}")
