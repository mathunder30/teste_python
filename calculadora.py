num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
operador = str(input("digite o operador (+) para somar,  (-) para susbtrair, (*) para multiplicar e (/) para dividir: "))
resultado = 0 
if operador == "+":
    resultado = num1 + num2
    print("o resultado é", resultado)
elif operador == "-":
    resultado = num1 - num2
    print("o resultado: ", resultado)
elif operador == "*":
    resultado = num1 * num2
    print("resultado é ", resultado)
elif operador == "/":
    if num2 != 0:
        resultado = num1/num2
        print("o resultado é: ", resultado)
    elif num2 == 0:
        print("Erro!! não pode dividir por zero.")
else:
    print("Você não digitou um operador válido.")

