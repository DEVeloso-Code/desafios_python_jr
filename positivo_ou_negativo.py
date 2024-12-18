# Solicite ao usuário um número e verifique se é positivo, negativo ou zero
try:
    numero = int(input("Insira um número: "))

    # Verifica se o número é positivo ou negativo
    if numero > 0:
        print("Esse número é positivo")
    elif numero < 0:
        print("Esse número é negativo")
    else:
        print("Esse número é zero")

except ValueError:
    print("Por favor, insira um número válido.")