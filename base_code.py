
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado

def taylor(x, n):
    #DERIVADAS DE e^x são e^x
    #f=f'=f''=f'''...
    #calcula com n termos
    soma = 0
    for i in range(n+1):
        soma += (x ** i) / fatorial(i)
    return soma

def main():
    print("Cálculo de e^x usando a série de Taylor")
    # Entrada de dados
    x = float(input("Digite o valor de x: "))
    n = int(input("Digite o número de termos da série (n): "))

    # Cálculo para x direto
    print("\n--- Usando x diretamente na série ---")
    ex_direto = taylor(x, n)
    print(f"O valor de e^{x} (diretamente) com {n} termos é: {ex_direto:.4f}")

    if x < 0: #se x for negativo
        # Cálculo considerando y = -x e e^x = 1/e^-x
        print("\n--- Usando y = -x e calculando 1/e^-x ---")
        y = -x
        e_negativo_x = taylor(y, n)
        ex_via_inverso = 1 / e_negativo_x
        print(f"O valor de e^{x} (via 1/e^{-x}) com {n} termos é: {ex_via_inverso:.4f}")

main()
