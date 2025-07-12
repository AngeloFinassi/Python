import networkx as nx
import matplotlib.pyplot as plt

def create_dune_graph():
    G = nx.Graph()

    #Vértices
    characters = [
        "Paul Atreides", "Lady Jessica", "Chani", "Stilgar",
        "Barão Harkonnen", "Feyd-Rautha Harkonnen", "Princesa Irulan",
        "Imperador Shaddam IV", "Gurney Halleck", "Rabban Harkonnen",
        "Liet-Kynes", "Reverenda Madre Mohiam", "Thufir Hawat",
        "Duncan Idaho", "Alia Atreides", "Sacerdotisa Fremen",
        "Jamis", "Farok", "Shishakli", "Gondola",
        "Esbirro Harkonnen I", "Esbirro Harkonnen II",
        "Guerreiro Fremen I", "Guerreiro Fremen II"
    ]
    G.add_nodes_from(characters)

    # Arestas
    edges = [
        ("Paul Atreides", "Lady Jessica"),
        ("Paul Atreides", "Chani"),
        ("Paul Atreides", "Stilgar"),
        ("Paul Atreides", "Barão Harkonnen"),
        ("Paul Atreides", "Feyd-Rautha Harkonnen"),
        ("Paul Atreides", "Imperador Shaddam IV"),
        ("Paul Atreides", "Princesa Irulan"),
        ("Paul Atreides", "Gurney Halleck"),
        ("Paul Atreides", "Alia Atreides"),
        ("Paul Atreides", "Jamis"),
        ("Lady Jessica", "Stilgar"),
        ("Lady Jessica", "Reverenda Madre Mohiam"),
        ("Lady Jessica", "Barão Harkonnen"),
        ("Lady Jessica", "Alia Atreides"),
        ("Lady Jessica", "Sacerdotisa Fremen"),
        ("Chani", "Stilgar"),
        ("Stilgar", "Jamis"),
        ("Stilgar", "Farok"),
        ("Stilgar", "Shishakli"),
        ("Stilgar", "Gondola"),
        ("Barão Harkonnen", "Feyd-Rautha Harkonnen"),
        ("Barão Harkonnen", "Rabban Harkonnen"),
        ("Imperador Shaddam IV", "Princesa Irulan"),
        ("Imperador Shaddam IV", "Reverenda Madre Mohiam"),
        ("Gurney Halleck", "Rabban Harkonnen"),
        ("Gurney Halleck", "Paul Atreides"),
        ("Feyd-Rautha Harkonnen", "Esbirro Harkonnen I"),
        ("Feyd-Rautha Harkonnen", "Esbirro Harkonnen II"),
        ("Barão Harkonnen", "Esbirro Harkonnen I"),
        ("Barão Harkonnen", "Esbirro Harkonnen II"),
        ("Guerreiro Fremen I", "Stilgar"),
        ("Guerreiro Fremen II", "Stilgar"),
        ("Guerreiro Fremen I", "Chani"),
        ("Guerreiro Fremen II", "Chani"),
        ("Guerreiro Fremen I", "Paul Atreides"),
        ("Liet-Kynes", "Paul Atreides"),
        ("Thufir Hawat", "Paul Atreides"),
        ("Duncan Idaho", "Paul Atreides"),
        ("Sacerdotisa Fremen", "Chani"),
        ("Sacerdotisa Fremen", "Gondola"),
        ("Jamis", "Farok"),
        ("Farok", "Shishakli"),
        ("Shishakli", "Gondola"),
        ("Gurney Halleck", "Lady Jessica")
    ]
    G.add_edges_from(edges)

    return G

def calculate_graph_metrics(G):
    """
    Calcula e exibe as métricas do grafo.
    """
    print("--- Métricas Globais do Grafo ---")
    print(f"Número de Vértices: {G.number_of_nodes()}")
    print(f"Número de Arestas: {G.number_of_edges()}")

    # Verificar se o grafo é conectado antes de calcular algumas métricas
    if nx.is_connected(G):
        print("Número de Componentes Conectados: 1")
        print(f"Diâmetro: {nx.diameter(G)}")
        print(f"Comprimento Médio do Caminho Mais Curto: {nx.average_shortest_path_length(G):.2f}")
    else:
        print(f"Número de Componentes Conectados: {nx.number_connected_components(G)}")
        print("Diâmetro e Comprimento Médio do Caminho Mais Curto não aplicáveis para grafo desconectado.")

    print(f"Densidade do Grafo: {nx.density(G):.3f}")
    print(f"Coeficiente de Aglomeração Médio (Average Clustering): {nx.average_clustering(G):.3f}")

    print("Modularidade: Necessita de algoritmo de detecção de comunidades (ex: Louvain) para cálculo preciso.")
    print("No Gephi, este valor seria gerado automaticamente após a execução do algoritmo de modularidade.")

    print("\n--- Métricas por Vértice (Top 5) ---")

    # Centralidade de Grau
    degree_centrality = nx.degree_centrality(G)
    print("\nCentralidade de Grau:")
    sorted_degree = sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)
    for node, value in sorted_degree[:5]:
        print(f"  {node}: {value:.3f}")

    # Centralidade de Intermediação
    betweenness_centrality = nx.betweenness_centrality(G)
    print("\nCentralidade de Intermediação:")
    sorted_betweenness = sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True)
    for node, value in sorted_betweenness[:5]:
        print(f"  {node}: {value:.3f}")

    # Centralidade de Proximidade
    closeness_centrality = nx.closeness_centrality(G)
    print("\nCentralidade de Proximidade:")
    sorted_closeness = sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True)
    for node, value in sorted_closeness[:5]:
        print(f"  {node}: {value:.3f}")

    # Coeficiente de Aglomeração (local)
    clustering = nx.clustering(G)
    print("\nCoeficiente de Aglomeração (Top 5):")
    sorted_clustering = sorted(clustering.items(), key=lambda item: item[1], reverse=True)
    for node, value in sorted_clustering[:5]:
        print(f"  {node}: {value:.3f}")

def visualize_graph(G):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.8, iterations=50) # Layout para 
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    plt.title("Grafo de Personagens de Duna: Parte Dois")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    dune_graph = create_dune_graph()
    calculate_graph_metrics(dune_graph)