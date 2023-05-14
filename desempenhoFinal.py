import PySimpleGUI as sg
import matplotlib.pyplot as plt

# Definir layout
layout = [
    [sg.Text("Quantidade de alunos:"), sg.InputText()],
    [sg.Text("Série/Ano:"), sg.InputText()],
    [sg.Text("Letra da classe:"), sg.InputText()],
    [sg.Text("Quantidade de questões:"), sg.InputText()],
    [sg.Button("Adicionar acertos"), sg.Button("Calcular desempenho")],
]

# Criar janela
window = sg.Window("Desempenho dos Alunos", layout)

# Variáveis de entrada
quantidade_alunos = 0
serie = ""
ano = ""
quantidade_questoes = 0
acertos_por_questao = []
total_acertos = 0

# Função para adicionar acertos
def adicionar_acertos():
    global total_acertos, acertos_por_questao  # declarar como global antes de usá-las
    acertos_por_questao = []
    total_acertos = 0
    # Perguntar quantidade de acertos por questão
    for i in range(quantidade_questoes):
        acerto = sg.popup_get_text(f"Acertos na questão {i+1}:")
        acertos_por_questao.append(int(acerto))
        total_acertos += int(acerto)

# Função para calcular desempenho e mostrar gráfico
def calcular_desempenho():
    # Calcular desempenho
    desempenho = (total_acertos / (quantidade_alunos * quantidade_questoes * 1.0)) * 100
    # Mostrar desempenho na tela
    sg.popup(f"O desempenho é: {desempenho:.2f}%")
    # Gerar gráfico
    plt.bar(range(1, quantidade_questoes + 1), acertos_por_questao)
    plt.xlabel("Questões")
    plt.ylabel("Número de alunos")
    plt.title("Desempenho dos Alunos")
    plt.show()

# Loop principal
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Adicionar acertos":
        quantidade_alunos = int(values[0])
        serie = values[1]
        ano = values[2]
        quantidade_questoes = int(values[3])
        adicionar_acertos()
    if event == "Calcular desempenho":
        calcular_desempenho()

# Fechar janela
window.close()
