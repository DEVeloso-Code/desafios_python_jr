# Solicita as coordenadas do ponto
x = float(input("Insira a coordenada x: "))
y = float(input("Insira a coordenada y: "))

# Verifica em qual quadrante o ponto se encontra
if x > 0 and y > 0:
    print("O ponto está no 1º quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no 2º quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no 3º quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no 4º quadrante.")
else:
    print("O ponto está localizado no eixo ou na origem.")
