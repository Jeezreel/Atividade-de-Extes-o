#para exibir uma mensagem dizendo ''olá''
print("Olá, mundo!")

#calculadora simples
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("A soma é:", a + b)

#verificador de par ou impar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("É par!")
else:
    print("É ímpar!")

#contador até 10
for i in range(1, 11):
    print(i)
    
#jogo simples de adivinhação
import random

numero_secreto = random.randint(1, 10)
tentativa = int(input("Adivinhe o número de 1 a 10: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou.")
else:
    print(f"Errou! O número era {numero_secreto}.")

