operadores = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

def avaliar(expressao):
    expressao = expressao.strip()
    
    n = 0
    for i in range(len(expressao) - 1, -1, -1):
        if expressao[i] == ')': n += 1
        if expressao[i] == '(': n -= 1
        if n == 0 and expressao[i] in ('+', '-') and i > 0:
            return operadores[expressao[i]] (
                avaliar(expressao[:i]),
                avaliar(expressao[i+1:])
            )
            
    n = 0
    for i in range(len(expressao) - 1, -1, -1):
        if expressao[i] == ')': n += 1
        if expressao[i] == '(': n -= 1
        if n == 0 and expressao[i] in ('*', '/'):
            return operadores[expressao[i]] (
                avaliar(expressao[:i]),
                avaliar(expressao[i+1:])
            )
            
    if expressao.startswith('(') and expressao.endswith(')'):
        return avaliar(expressao[1:-1])
    
    return float(expressao)

uEntry = input("Digite uma expressão numérica: ")
print(avaliar(uEntry))