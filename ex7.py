from sympy import symbols, Rational

def taylor_sympy(x_val, p):

    #Calcula e^x utilizando a série de Taylor e computação simbólica com sympy.
    # x_val: valor numérico de x

    # Define a variável simbólica x
    x = symbols('x')

    # Inicia com o primeiro termo da série e soma total
    soma = Rational(1)  # Simbolicamente, 1 é tratado como fração
    termo_anterior = Rational(1)  # Primeiro termo: x^0 / 0!
    i = 1

    while True:
        # Calcula o próximo termo simbolicamente
        termo_atual = termo_anterior * (x / i)
        soma += termo_atual
        termo_anterior = termo_atual
        i += 1

        # Avalia a tolerância numericamente
        termo_num = termo_atual.subs(x, x_val)
        if abs(termo_num) < p:
            print(f"O número de termos necessários para atingir a tolerância foi: {i - 1}")
            return soma.subs(x, x_val)


def main():
    print("Cálculo de e^x usando a série de Taylor com SymPy")
    # Entrada de dados
    x = float(input("Digite o valor de x: "))
    p = float(input("Digite o limite de tolerância (p): "))

    # Cálculo para x diretamente
    print("\n--- Usando x diretamente na série ---")
    ex_direto_num = taylor_sympy(x, p)
    print(f"O valor de e^{x} (diretamente) com {p} de limite de tolerância é: {ex_direto_num:.8f}")


    if x < 0:  # Caso x seja negativo
        # Cálculo considerando y = -x e e^x = 1/e^-x
        print("\n--- Usando y = -x e calculando 1/e^-x ---")
        y = -x
        e_negativo_num, _ = taylor_sympy(y, p)
        ex_via_inverso = 1 / e_negativo_num
        print(f"O valor de e^{x} (via 1/e^{-x}) com {p} de limite de tolerância é: {ex_via_inverso:.8f}")


main()
