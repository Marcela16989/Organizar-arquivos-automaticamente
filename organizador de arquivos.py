import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organizar_arquivos_por_extensao(pasta_alvo):
    if not os.path.isdir(pasta_alvo):
        print("A pasta fornecida não existe!")
        return
    for arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, arquivo)

        if os.path.isfile(caminho_completo):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao[1:].lower() or "sem_extensao"
            pasta_destino = os.path.join(pasta_alvo, extensao)

            os.makedirs(pasta_destino, exist_ok=True)
            novo_caminho = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_completo, novo_caminho)

            print(f"MOVIDO: {arquivo} para a pasta {pasta_destino}")

def seleciona_pasta():
    root = tk.Tk()
    root.withdraw()
    pasta_escolhida = filedialog.askdirectory(title="Selecione a pasta para organizar!")

    if pasta_escolhida:
        print(f"\nOrganizando arquivos na pasta: {pasta_escolhida}\n")
        organizar_arquivos_por_extensao(pasta_escolhida)
    else:
        print("Nenhuma pasta foi selecionada.")

seleciona_pasta()
