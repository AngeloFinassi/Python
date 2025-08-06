def salvar_links_em_linha(texto, nome_arquivo_saida="salas_links.txt"):
    linhas = texto.strip().splitlines()
    links_formatados = []

    for linha in linhas:
        linha = linha.strip()
        if linha and not linha.lower().startswith("section"):
            nome = linha.replace("✔️", "").strip()
            links_formatados.append(f"link[[{nome}]]")

    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
        for link in links_formatados:
            f.write(link + "\n")

    print(f"✅ Arquivo '{nome_arquivo_saida}' criado com sucesso!")


# Entrada de exemplo
entrada = """
Task 1
What is Penetration Testing?
Task 2
Penetration Testing Ethics
Task 3
Penetration Testing Methodologies
Task 4
Black box, White box, Grey box Penetration Testing
Task 5
Practical: ACME Penetration Test
"""

# Executar
salvar_links_em_linha(entrada)
