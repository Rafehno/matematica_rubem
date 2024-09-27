def add_mod(a, b, n):
    return (a + b) % n

def mult_mod(a, b, n):
    return (a * b) % n

def tabela_adicao_anel(n):
    return [[add_mod(a, b, n) for b in range(n)] for a in range(n)]

def tabela_multiplicacao_anel(n):
    return [[mult_mod(a, b, n) for b in range(n)] for a in range(n)]