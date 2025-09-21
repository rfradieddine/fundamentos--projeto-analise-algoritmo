import time;

def max_min_select(arr, inicio, fim):
    """
    Função recursiva que encontra o maior e o menor elemento de um sub-array
    usando a abordagem de divisão e conquista.

    Parâmetros:
    arr (list): A lista completa de números.
    inicio (int): O índice inicial do sub-array a ser analisado.
    fim (int): O índice final do sub-array a ser analisado.

    Retorna:
    (int, int): Uma tupla contendo o menor e o maior elemento encontrados.
    """
    # Caso Base 1: Se houver apenas um elemento no sub-array.
    if inicio == fim:
        return arr[inicio], arr[inicio]

    # Caso Base 2: Se houver dois elementos no sub-array.
    if fim == inicio + 1:
        if arr[inicio] < arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]

    # Passo de Divisão: Se houver mais de dois elementos.
    meio = (inicio + fim) // 2

    # Passo de Conquista: Chamadas recursivas para as duas metades.
    min_esq, max_esq = max_min_select(arr, inicio, meio)
    min_dir, max_dir = max_min_select(arr, meio + 1, fim)

    # Passo de Combinação: Combina os resultados.
    menor_final = min(min_esq, min_dir)
    maior_final = max(max_esq, max_dir)

    return menor_final, maior_final

if __name__ == "__main__":
    # Solicita a entrada de dados ao usuário.
    input_usuario = input("Digite uma lista de números separados por espaço: ")

    try:
        # Tenta converter a entrada do usuário (string) em uma lista de números inteiros.
        # 1. .split() divide a string em uma lista de strings menores.
        # 2. int(num) converte cada string para um número inteiro.
        lista_numeros = [int(num) for num in input_usuario.split()]

        # Verifica se a lista não está vazia após a conversão.
        if not lista_numeros:
            print("Erro: A lista não pode estar vazia.")
        else:
            print("\nResultado:")
            print(f"\nLista inserida: {lista_numeros}")
            
            # Mede o tempo de execução do algoritmo MaxMin.
            start_time = time.time()
            menor, maior = max_min_select(lista_numeros, 0, len(lista_numeros) - 1)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # milissegundos

            # Imprime o resultado final.
            print(f"Menor elemento encontrado: {menor}")
            print(f"Maior elemento encontrado: {maior}")
            print(f"\nTempo de execução do algoritmo MaxMin: {execution_time:.6f} milissegundos")


    except ValueError:
        # Se a conversão para int() falhar, informa o usuário sobre o erro.
        print("\nErro: Por favor, digite apenas números inteiros separados por espaço.")