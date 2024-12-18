# Solicite ao usuário um número e verifique se é divisível por 2
try:
    numero = int(input("Insira um número: "))

    # Verifica se o número é divisível por 2
    if numero % 2 == 0:
        print("Esse número é divisível por 2")
    else:
        print("Esse número não é divisível por 2")

except ValueError:
    print("Por favor, insira um número válido.")