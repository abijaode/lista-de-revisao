# Peça um número inteiro positivo ao usuário e determine se ele é primo utilizando
# while


numero = int(input("Digite o número: "))
contador = 2
primo = True

if numero < 2:
    primo = False
else:    
    while numero > contador: 
        if numero  % contador == 0:
            primo = False 
            break     
        else:
            primo = True
            break
        contador += 1

if primo:
    print("O numero é primo")
else:
    print("O numero nao é primo")
