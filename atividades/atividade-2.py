# Peça uma base e um expoente inteiro não negativo ao usuário e calcule a potência
# manualmente, sem usar operador de exponenciação, utilizando um for.


base = int(input("Digite a Base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(expoente):
    resultado = resultado * base

print("O resultado é: ", resultado)
print("O expoente é: ", expoente)
print("A base é: ", base)

