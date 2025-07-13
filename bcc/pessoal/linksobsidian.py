def format_salas_para_obsidian(texto):
    linhas = texto.strip().splitlines()
    saida_formatada = []

    for linha in linhas:
        linha = linha.strip()
        if linha and not linha.lower().startswith("section"):
            #Remove qualquer emoji e pontuação
            nome = linha.replace("✔️", "").strip()
            saida_formatada.append(f"- [[{nome}]]")

    return "\n".join(saida_formatada)

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
Introduction to SIEM
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

# Exibir resultado
print(format_salas_para_obsidian(entrada))
