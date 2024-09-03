### Exemplo de Código em Python:
# Variável de escopo global
mensagem_global = "Eu sou uma variável global"
def minha_funcao ():
    # Variável de escopo local
    mensagem_local = "Eu sou uma variável local"
    print(mensagem_local) #Acessivel dentro da função

    minha_funcao()

    # Se tentarmos acessar a variável local
    # fora da função (causará erro)
    # print (mensagem_local)

    #Variável global ainda é acessivel
    print(mensagem_global) # Exibe: Eu sou uma variável global