import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

# Criar janela
root = tk.Tk()
root.title("Desempenho dos Alunos")

# Variáveis de entrada
quantidade_alunos = tk.IntVar()
serie = tk.StringVar()
ano = tk.StringVar()
quantidade_questoes = tk.IntVar()
acertos_por_questao = []
total_acertos = 0

# Função para adicionar acertos
def adicionar_acertos():
    global total_acertos  # declarar como global antes de usá-la
    # Verificar se existem 5 questões
    if quantidade_questoes.get() == 5:
        # Perguntar acerto por questão
        for i in range(quantidade_questoes.get()):
            acerto = simpledialog.askinteger("Acertos", f"Acertos na questão {i+1}:")
            acertos_por_questao.append(acerto)
            total_acertos += acerto
    else:
        # Perguntar total de acertos
        total_acertos = simpledialog.askinteger("Acertos", "Total de acertos:")

# Função para calcular desempenho e mostrar gráfico
def calcular_desempenho():
    # Calcular desempenho
    desempenho = (total_acertos / (quantidade_alunos.get() * quantidade_questoes.get() * 1.0)) * 100
    # Mostrar desempenho na tela
    messagebox.showinfo("Desempenho", f"O desempenho é: {desempenho:.2f}%")
    # Gerar gráfico
    if quantidade_questoes.get() == 5:
        plt.bar(range(1, 6), acertos_por_questao)
        plt.xlabel("Questões")
    else:
        plt.bar(["Total"], [total_acertos])
        plt.xlabel("Acertos")
    plt.ylabel("Número de alunos")
    plt.title("Desempenho dos Alunos")
    plt.show()

# Criar widgets
tk.Label(root, text="Quantidade de alunos:").grid(row=0, column=0)
tk.Entry(root, textvariable=quantidade_alunos).grid(row=0, column=1)

tk.Label(root, text="Série/Ano:").grid(row=1, column=0)
tk.Entry(root, textvariable=serie).grid(row=1, column=1)

tk.Label(root, text="Letra da classe:").grid(row=2, column=0)
tk.Entry(root, textvariable=ano).grid(row=2, column=1)

tk.Label(root, text="Quantidade de questões:").grid(row=3, column=0)
tk.Entry(root, textvariable=quantidade_questoes).grid(row=3, column=1)

tk.Button(root, text="Adicionar acertos", command=adicionar_acertos).grid(row=4, column=0)
tk.Button(root, text="Calcular desempenho", command=calcular_desempenho).grid(row=4, column=1)

# Iniciar janela
root.mainloop()
