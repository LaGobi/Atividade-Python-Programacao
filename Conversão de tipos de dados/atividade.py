### Exemplo de Código em Python:
# Leitura de dados com string
idade_str = "25"
altura_str = "1.75"
# Conversão de tipos
idade = int (idade_str)                         #convertendo string para inteiro
altura = float (altura_str)                     #convertendo string para float
#Processamento usando os novos tipos de dados
mensagem = "idade: " + str(idade) + ", Altura: " + str(altura)
# Exibindo a mensagem
print(mensagem)  # Exibe: Idade 25, Altura: 1.75