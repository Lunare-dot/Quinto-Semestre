x = input("Insira um número: ")
y = input("Insira uma base (8, 10, 16): ")
print(type(x))

x = int(x)
y = int(y)
print(type(x))

if (y == 10): print("\nValor em decimal: ", x)
elif (y == 16): print("\nValor em hexadecimal: ", hex(x))
elif (y == 8): print("\nValor em octal: ", oct(x))
else: print("Base inválida!")