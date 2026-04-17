#!/usr/bin/env python3
"""
Gera um CSV com a lista de todos os arquivos da pasta atual.
"""

import csv
import os
from datetime import datetime

PASTA = os.path.dirname(os.path.abspath(__file__))
SAIDA_ARQUIVOS = os.path.join(PASTA, "lista_arquivos_completa.csv")


def listar_todos_arquivos():
    """Lista todos os arquivos do diretório com informações detalhadas."""
    arquivos_info = []

    for arquivo in sorted(os.listdir(PASTA)):
        caminho_completo = os.path.join(PASTA, arquivo)

        if os.path.isdir(caminho_completo):
            continue

        if arquivo == os.path.basename(__file__):
            continue

        try:
            stat_info = os.stat(caminho_completo)
            tamanho_mb = stat_info.st_size / (1024 * 1024)
            data_mod = datetime.fromtimestamp(stat_info.st_mtime).strftime("%d/%m/%Y %H:%M:%S")
            extensao = os.path.splitext(arquivo)[1].lower() or "sem extensao"

            info = {
                "arquivo": arquivo,
                "extensao": extensao,
                "tamanho_mb": f"{tamanho_mb:.2f}",
                "data_modificacao": data_mod,
                "caminho_completo": caminho_completo,
            }
            arquivos_info.append(info)
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    return arquivos_info


def main():
    arquivos = listar_todos_arquivos()

    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    campos = ["arquivo", "extensao", "tamanho_mb", "data_modificacao", "caminho_completo"]

    with open(SAIDA_ARQUIVOS, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        writer.writeheader()
        writer.writerows(arquivos)

    print(f"Lista de arquivos salva em: {SAIDA_ARQUIVOS}")
    print(f"Total de arquivos: {len(arquivos)}")


if __name__ == "__main__":
    main()
