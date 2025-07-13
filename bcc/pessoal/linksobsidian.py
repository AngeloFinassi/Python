def formatar_salas_para_links(texto, nome_arquivo_saida="salas_formatadas.txt"):
    linhas = texto.strip().splitlines()
    salas_formatadas = []

    for linha in linhas:
        linha = linha.strip()
        if linha and not linha.lower().startswith("section"):
            nome = linha.replace("✔️", "").strip()
            salas_formatadas.append(f"link[[{nome}]]")

    resultado = ", ".join(salas_formatadas)

    #Salvar no arquivo txt
    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
        f.write(resultado)

    print(f"✅ Arquivo '{nome_arquivo_saida}' criado com sucesso!")


# Entrada de exemplo
entrada = """
Intro to Endpoint Security
Core Windows Processes
Sysinternals
Windows Event Logs
Sysmon
Osquery: The Basics
Wazuh
Monday Monitor
Retracted
Introduction to SIEM ✔️
Investigating with ELK 101
ItsyBitsy
Splunk: Basics
Incident handling with Splunk
Investigating with Splunk
Benign
DFIR: An Introduction
Windows Forensics 1
Windows Forensics 2
Linux Forensics
Autopsy
Redline
KAPE
Volatility
Velociraptor
TheHive Project
Intro to Malware Analysis
Unattended
Disgruntled
Critical
Secret Recipe
"""

# Executar
formatar_salas_para_links(entrada)
