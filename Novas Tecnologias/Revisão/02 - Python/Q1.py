number = int(input("Entre com um número inteiro de cinco digitos: "))

x = []
i = 0
while (number > 0):
    x.append(number % 10)
    number //= 10
    i += 1

if (i == 5):
    x.reverse()
    print(x)
else:
    print("O número deve ter cinco digitos")