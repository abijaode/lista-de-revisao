# Peça ao usuário um número binário (por exemplo: 1101), e converta-o para decimal
# utilizando um while


numero_binario = int(input("Digite o número binario: "))

copia_binario = numero_binario
resultado_decimal = 0
potencia = 0

while numero_binario > 0:
    digito = numero_binario * 10
    resultado_decimal = resultado_decimal + (digito * (2 ** potencia))

    potencia = potencia + 1
    numero_binario = numero_binario // 10

print(f"O numero binario é {copia_binario} em decimal é {resultado_decimal}")