import PySimpleGUI as sg

def main():
    # Criando a janela
    layout = [
        [sg.Text("Número de entrada:")],
        [sg.InputText(key="numero_de_entrada")],
        [sg.Text("Total de itens:")],
        [sg.InputText(key="total_itens")],
        [sg.Text("Tipos de pesquisa:")],
        [sg.Checkbox("Original", key="Original"), sg.Checkbox("Re-creation", key="Re-creation"), sg.Checkbox("Inpersonation", key="Inpersonation")],
        [sg.Checkbox("High Vertical/Middle/Random", key="High Vertical/Middle/Random")],
        [sg.Button("Calcular")],
        [sg.Text("", size=(40, 2), key="resultado")],  # Aumentando a altura da caixa de texto para exibir o resultado
        [sg.Text("", size=(40, 1), key="classificacao")]  # Espaço para a classificação
    ]

    janela = sg.Window("Pesquisa de originalidade", layout)

    # Inicializando a variável para armazenar o primeiro resultado
    primeiro_resultado = None

    # Loop de eventos
    while True:
        evento, valores = janela.read()

        # Verificando se a janela foi fechada
        if evento == sg.WIN_CLOSED:
            break

        # Verificando se o botão "Calcular" foi pressionado
        if evento == "Calcular":
            # Verificando se o valor do número e do total são válidos
            try:
                numero_de_entrada = int(valores["numero_de_entrada"])
                total_itens = int(valores["total_itens"])
                if numero_de_entrada < 0 or total_itens <= 0:
                    raise ValueError("O número de entrada e o total de itens devem ser maiores que zero.")
            except ValueError:
                janela["resultado"].update("O valor do número de entrada e do total de itens devem ser números inteiros maiores que zero.")
                continue

            # Calculando a porcentagem em relação ao total inserido pelo usuário
            resultado = (1 - numero_de_entrada / total_itens) * 100

            # Exibindo a porcentagem para o usuário
            porcentagem = int(resultado)
            janela["resultado"].update(f"Para o número {numero_de_entrada} em um total de {total_itens}, o resultado da pesquisa é {porcentagem}%.")

            # Verificando se o usuário selecionou High Vertical/Middle/Random
            if valores["High Vertical/Middle/Random"]:
                # Comparando com o primeiro resultado e classificando
                classificacao = ""
                if primeiro_resultado is not None and resultado > 90:
                    classificacao = "High"
                elif primeiro_resultado is not None and 60 <= resultado <= 90:
                    classificacao = "Middle"
                elif primeiro_resultado is not None and resultado < 60:
                    classificacao = "Random"

                # Armazenando o primeiro resultado se ainda não foi armazenado
                if primeiro_resultado is None:
                    primeiro_resultado = resultado

                # Exibindo a classificação para o usuário
                janela["classificacao"].update(f"Classificação: {classificacao}")
            else:
                # Se não for selecionado High Vertical/Middle/Random, limpar a classificação
                janela["classificacao"].update("")

    # Fechando a janela
    janela.close()

if __name__ == "__main__":
    main()
