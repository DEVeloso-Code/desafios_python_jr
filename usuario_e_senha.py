# Definindo os valores esperados
usuario_esperado = "admin"
senha_esperada = "senha123"

# Solicita o nome de usuário e a senha
usuario = input("Insira o nome de usuário: ")
senha = input("Insira a senha: ")

# Verifica se o nome de usuário e a senha estão corretos
if usuario == usuario_esperado and senha == senha_esperada:
    print("Acesso concedido!")
else:
    print("Nome de usuário ou senha incorretos.")
