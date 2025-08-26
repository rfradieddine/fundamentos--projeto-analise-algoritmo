import time

def karatsuba(x, y):
    # Caso base: se um dos números tem apenas 1 dígito
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho do maior número
    n = max(len(str(x)), len(str(y)))

    # Divide n pela metade (arredondando para cima se ímpar)
    m = n // 2

    # Divide x em duas partes: x = a * 10^m + b
    a = x // (10 ** m)  # Parte alta de x
    b = x % (10 ** m)  # Parte baixa de x

    # Divide y em duas partes: y = c * 10^m + d
    c = y // (10 ** m)  # Parte alta de y
    d = y % (10 ** m)  # Parte baixa de y

    # Três multiplicações recursivas (ao invés de 4 no método tradicional)
    ac = karatsuba(a, c)  # Produto das partes altas
    bd = karatsuba(b, d)  # Produto das partes baixas
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd  # Produto cruzado

    # Combina os resultados usando a fórmula de Karatsuba
    # resultado = ac * 10^(2*m) + ad_plus_bc * 10^m + bd
    resultado = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd
    
    return resultado


def multiplicacao_tradicional(x, y):
    """
    Implementa a multiplicação tradicional para comparação.

    Args:
        x: Primeiro número inteiro
        y: Segundo número inteiro

    Returns:
        O produto de x e y
    """
    return x * y


def testar_karatsuba():
    """
    Função para testar o algoritmo de Karatsuba com diferentes casos.
    """
    casos_teste = [
        (12, 34),
        (123, 456),
        (1234, 5678),
        (12345, 67890),
        (123456789, 987654321),
        (999999999, 999999999),
        (1000000000000, 2000000000000),
        (5, 7),  # Números pequenos
        (0, 12345),  # Teste com zero
        (1, 98765)  # Teste com um
    ]

    print("=" * 60)
    print("TESTE DO ALGORITMO DE KARATSUBA")
    print("=" * 60)

    for x, y in casos_teste:
        resultado_karatsuba = karatsuba(x, y)
        resultado_esperado = x * y

        # Verifica se o resultado está correto
        status = "CORRETO" if resultado_karatsuba == resultado_esperado else "ERRO"

        print(f"\n{x} × {y}")
        print(f"Karatsuba: {resultado_karatsuba}")
        print(f"Esperado:  {resultado_esperado}")
        print(f"Status: {status}")

    print("\n" + "=" * 60)
    print("TODOS OS TESTES CONCLUÍDOS")
    print("=" * 60)


def demonstracao_passo_a_passo(x, y):
    """
    Demonstra o funcionamento do algoritmo passo a passo.

    Args:
        x: Primeiro número inteiro
        y: Segundo número inteiro
    """
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO PASSO A PASSO DO ALGORITMO DE KARATSUBA")
    print("=" * 60)
    print(f"\nMultiplicando {x} × {y}")

    if x < 10 or y < 10:
        print(f"Caso base: {x} × {y} = {x * y}")
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    print(f"\nDivisão dos números:")
    print(f"  {x} = {a} × 10^{m} + {b}")
    print(f"  {y} = {c} × 10^{m} + {d}")

    print(f"\nCálculos recursivos:")
    ac = a * c
    bd = b * d
    ad_plus_bc = (a + b) * (c + d) - ac - bd

    print(f"  ac = {a} × {c} = {ac}")
    print(f"  bd = {b} × {d} = {bd}")
    print(f"  (a+b) × (c+d) = {a + b} × {c + d} = {(a + b) * (c + d)}")
    print(f"  ad + bc = {(a + b) * (c + d)} - {ac} - {bd} = {ad_plus_bc}")

    resultado = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd

    print(f"\nCombinação final:")
    print(f"  {ac} × 10^{2 * m} + {ad_plus_bc} × 10^{m} + {bd}")
    print(f"  = {ac * (10 ** (2 * m))} + {ad_plus_bc * (10 ** m)} + {bd}")
    print(f"  = {resultado}")

    print(f"\nVerificação: {x} × {y} = {x * y} ✓")

    return resultado


def benchmark_comparativo():
    """
    Compara o desempenho do algoritmo de Karatsuba com a multiplicação tradicional.
    """

    print("\n" + "=" * 60)
    print("BENCHMARK COMPARATIVO")
    print("=" * 60)

    numeros_teste = [
        (10 ** 10, 10 ** 10),
        (10 ** 20, 10 ** 20),
        (10 ** 30, 10 ** 30),
        (10 ** 40, 10 ** 40),
        (10 ** 50, 10 ** 50)
    ]

    for x, y in numeros_teste:
        # Teste Karatsuba
        inicio = time.perf_counter()
        resultado_k = karatsuba(x, y)
        tempo_k = time.perf_counter() - inicio

        # Teste Tradicional
        inicio = time.perf_counter()
        resultado_t = multiplicacao_tradicional(x, y)
        tempo_t = time.perf_counter() - inicio

        print(f"\nTamanho: {len(str(x))} dígitos × {len(str(y))} dígitos")
        print(f"Karatsuba: {tempo_k:.6f} segundos")
        print(f"Tradicional: {tempo_t:.6f} segundos")
        print(f"Speedup: {tempo_t / tempo_k:.2f}x")


def menu_principal():
    """
    Menu interativo para testar o algoritmo.
    """
    while True:
        print("\n" + "=" * 60)
        print("ALGORITMO DE KARATSUBA - MENU PRINCIPAL")
        print("=" * 60)
        print("1. Executar testes automatizados")
        print("2. Demonstração passo a passo")
        print("3. Multiplicar dois números personalizados")
        print("4. Sair")
        print("=" * 60)

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            testar_karatsuba()
        elif opcao == "2":
            print("\nDigite dois números para a demonstração:")
            x = int(input("Primeiro número: "))
            y = int(input("Segundo número: "))
            demonstracao_passo_a_passo(x, y)
        elif opcao == "3":
            print("\nDigite dois números para multiplicar:")
            x = int(input("Primeiro número: "))
            y = int(input("Segundo número: "))
            
            # Medindo tempo do método Karatsuba
            inicio_k = time.perf_counter()
            resultado_k = karatsuba(x, y)
            tempo_k = time.perf_counter() - inicio_k
            
            # Medindo tempo do método tradicional
            inicio_t = time.perf_counter()
            resultado_t = multiplicacao_tradicional(x, y)
            tempo_t = time.perf_counter() - inicio_t
            
            print(f"\n{x} × {y} = {resultado_k}")
            print(f"Tempo Karatsuba: {tempo_k:.6f} segundos")
            print(f"Tempo Tradicional: {tempo_t:.6f} segundos")
            print(f"Speedup: {tempo_t / tempo_k:.2f}x")
        elif opcao == "4":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()