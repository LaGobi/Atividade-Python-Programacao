def calcular_expressao():
    # Solicitar ao usuario que insita uma expressão matemática
    expressao = input ("Digite uma expressão matemática")

    try:
        # Avaliar a expressão usando eval
        resultado = eval(expressao)
        print("O resultado da expressão é:", resultado)
    except Exception as e:
        print ("Erros ao avaliar a expressão", e)

        # Chamar a funcao
        calcular_expressao()
        # Exemplo da chamada do programa:
        # Digite uma expressão matemática: 2 + 3 * (4 - 1)
        # O resultado da espressão é : 11