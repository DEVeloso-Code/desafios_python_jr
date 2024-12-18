# Verificar se um número é múltiplo de 5
try:
    numero = int(input("Insira um número: "))

    # Verifica se o número é múltiplo de 5
    if numero % 5 == 0:
        print("Esse número é múltiplo de 5")
    else:
        print("Esse número não é múltiplo de 5")
    
except ValueError:
    print("Por favor, insira um número válido")