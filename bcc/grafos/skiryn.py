import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Ler o CSV
df = pd.read_csv("processed_relationships.csv")

# Criar grafo direcionado (pode ser não-direcionado se preferir)
G = nx.DiGraph()

# Adicionar as arestas com tipo de relacionamento como rótulo
for _, row in df.iterrows():
    npc1 = row["NPC1_Name"]
    npc2 = row["NPC2_Name"]
    rel_type = row["Relationship_Type"]
    
    G.add_edge(npc1, npc2, label=rel_type)

# Desenhar o grafo
plt.figure(figsize=(16, 12))
pos = nx.spring_layout(G, k=0.5)

# Nós e arestas
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", edge_color="gray", font_size=10)

# Adicionar rótulos às arestas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=8)

plt.title("Relacionamentos entre NPCs")
plt.axis('off')
plt.show()