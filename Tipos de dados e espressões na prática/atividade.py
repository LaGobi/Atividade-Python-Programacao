
def soma_numeros (a, b) :
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Erro: Entrada inválida")
    except Exception as e:
        print(f"Eroo inesperado: {e}")
        return None
    # Testes da funcao com numeros validos
    print (soma_numeros (2,3))  # Saida: 5
    # Testes da funcao com numeros invalidos
    print(soma_numeros("a", 3))
    # Saida: Erro: entrada invalida
    # Testes da funcao com outros tipos de dados
    print(soma_numeros(True, 3))
    # Saida: 4 (pois True é considerado 1 em Python)
    # Testes da funcao com uma lista
    print(soma_numeros([1, 2],3))
    # Saida: Erro: entrada invalida