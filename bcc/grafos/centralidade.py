import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def carregar_dados_skyrim(caminho_arquivo):
    """
    Carrega os dados do arquivo CSV, tentando diferentes codificações e separadores.
    """
    tentativas = [
        {'encoding': 'utf-8', 'sep': ','},
        {'encoding': 'latin-1', 'sep': ','},
        {'encoding': 'utf-8', 'sep': ';'},
        {'encoding': 'latin-1', 'sep': ';'}
    ]
    
    for params in tentativas:
        try:
            print(f"Tentando ler com: encoding='{params['encoding']}', separador='{params['sep']}'...")
            df = pd.read_csv(caminho_arquivo, encoding=params['encoding'], sep=params['sep'])
            
            if 'Source' in df.columns and 'Target' in df.columns:
                print("\nArquivo lido com SUCESSO!\n")
                return df
            else:
                # Se leu o arquivo mas não achou as colunas, continua tentando
                print("Leitura bem-sucedida, mas colunas 'Source'/'Target' não encontradas. Tentando próximo separador.")
                continue

        except Exception as e:
            print(f"Falhou. Erro: {e}\n")

    print("ERRO FINAL: Não foi possível ler o arquivo ou encontrar as colunas 'Source' e 'Target'.")
    print("Verifique se o arquivo CSV tem essas colunas e se o separador é ',' ou ';'.")
    return None

def plotar_grafo_centralidade(G, centralidade, metrica_nome, ax, pos):
    """
    Função auxiliar para plotar um grafo com tamanho do nó por grau e cor por outra centralidade.
    """
    grau_centralidade = nx.degree_centrality(G)
    node_sizes = [v * 20000 for v in grau_centralidade.values()]
    node_colors = list(centralidade.values())
    cores = cm.viridis
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=cores, ax=ax, alpha=0.8)
    nx.draw_networkx_edges(G, pos, alpha=0.1, edge_color="gray", ax=ax)
    
    nos_importantes = sorted(grau_centralidade, key=grau_centralidade.get, reverse=True)[:15]
    labels_importantes = {node: node for node in nos_importantes}
    nx.draw_networkx_labels(G, pos, labels=labels_importantes, font_size=8, font_color="black", font_weight='bold', ax=ax)

    ax.set_title(f'Grafo de Centralidade de {metrica_nome}\n(Tamanho por Grau)', fontsize=15)
    ax.axis('off')
    
    sm = plt.cm.ScalarMappable(cmap=cores, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
    sm._A = [] 
    cbar = plt.colorbar(sm, ax=ax, shrink=0.8)
    cbar.set_label(f'Valor de Centralidade de {metrica_nome}', rotation=270, labelpad=15)


# --- BLOCO PRINCIPAL DE EXECUÇÃO ---
if __name__ == "__main__":
    # CORREÇÃO: Adicionado o 'r' antes das aspas para o caminho funcionar no Windows
    caminho_arquivo = r"D:\CC - Learning\Python\bcc\grafos\sky.csv"

    dataframe = carregar_dados_skyrim(caminho_arquivo)

    if dataframe is not None:
        # Tenta criar o grafo usando as colunas 'Source' e 'Target'
        # Adicionado um try-except para o caso de a coluna 'relationship' não existir
        try:
            G = nx.from_pandas_edgelist(dataframe, source='Source', target='Target', edge_attr='relationship')
        except KeyError:
            print("Aviso: Coluna 'relationship' não encontrada. Criando grafo sem atributos de aresta.")
            G = nx.from_pandas_edgelist(dataframe, source='Source', target='Target')

        print(f"Grafo de Skyrim criado com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")
        
        isolados = list(nx.isolates(G))
        if isolados:
            G.remove_nodes_from(isolados)
            print(f"Removidos {len(isolados)} nós isolados para melhorar a visualização.")
            print(f"Novo total: {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")

        print("\nCalculando centralidades... Isso pode levar alguns segundos.")
        betweenness_centrality = nx.betweenness_centrality(G)
        closeness_centrality = nx.closeness_centrality(G)

        print("Calculando o layout do grafo... Isso também pode demorar.")
        pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
        
        fig, axes = plt.subplots(1, 2, figsize=(22, 12))
        fig.suptitle('Análise de Rede dos Personagens de Skyrim', fontsize=20, y=0.98)
        
        print("Gerando os gráficos...")
        plotar_grafo_centralidade(G, betweenness_centrality, 'Intermediação (Betweenness)', axes[0], pos)
        plotar_grafo_centralidade(G, closeness_centrality, 'Proximidade (Closeness)', axes[1], pos)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig("grafos_skyrim.png")
        print("\nGráficos salvos com sucesso como 'grafos_skyrim.png'!")
        plt.show()