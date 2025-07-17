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
Phishing Analysis Fundamentals

Phishing Emails in Action

Phishing Analysis Tools

Phishing Prevention

The Greenholt Phish

Snapped Phish-ing Line

Tempest

Boogeyman 1

Boogeyman 2

Boogeyman 3
"""

# Executar
salvar_links_em_linha(entrada)
