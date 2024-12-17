def taylor(x, n):
    # Inicia com o primeiro termo (x^0 / 0! = 1)
    soma = 1
    termo_anterior = 1  # O primeiro termo é 1

    for i in range(1, n+1):
        # Calcula o próximo termo aproveitando o termo anterior
        termo_atual = termo_anterior * (x / i)
        soma += termo_atual
        termo_anterior = termo_atual  # Atualiza o termo anterior para o próximo cálculo

    return soma


def main():
    print("Cálculo de e^x usando a série de Taylor")
    # Entrada de dados
    x = float(input("Digite o valor de x: "))
    n = int(input("Digite o número de termos da série (n): "))

    # Cálculo para x direto
    print("\n--- Usando x diretamente na série ---")
    ex_direto = taylor(x, n)
    print(f"O valor de e^{x} (diretamente) com {n} termos é: {ex_direto:.8f}")

    if x < 0: #se x for negativo
        # Cálculo considerando y = -x e e^x = 1/e^-x
        print("\n--- Usando y = -x e calculando 1/e^-x ---")
        y = -x
        e_negativo_x = taylor(y, n)
        ex_via_inverso = 1 / e_negativo_x
        print(f"O valor de e^{x} (via 1/e^{-x}) com {n} termos é: {ex_via_inverso:.8f}")

main()
