# Algoritmo de Karatsuba - Multiplicação Eficiente de Inteiros

## Descrição do Projeto

Este projeto implementa o **Algoritmo de Karatsuba** em Python, uma técnica eficiente para multiplicação de números inteiros grandes desenvolvida por Anatolii Karatsuba em 1960. O algoritmo reduz a complexidade computacional da multiplicação de O(n²) para O(n^log₂3) ≈ O(n^1.585).

## Objetivo

Desenvolver uma implementação otimizada do algoritmo de Karatsuba que demonstre sua eficiência em comparação com o método tradicional de multiplicação, incluindo análises detalhadas de complexidade ciclomática e assintótica.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.13.x ou superior instalado
- Terminal ou prompt de comando

### Passos para Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/rfradieddine/fundamentos--projeto-analise-algoritmo.git
```

2. **Execute o programa principal:**
```bash
python main.py
```

3. **Menu de Opções:**
O programa apresentará um menu interativo com as seguintes opções:
- Testes automáticos
- Demonstração passo a passo
- Benchmark comparativo
- Multiplicação personalizada

## Lógica do Algoritmo

### Princípio Matemático

O algoritmo baseia-se na seguinte decomposição matemática:

Dados dois números `x` e `y` de `n` dígitos:
- x = a × 10^(n/2) + b
- y = c × 10^(n/2) + d

A multiplicação tradicional seria:
```
x × y = (a × 10^(n/2) + b) × (c × 10^(n/2) + d)
      = ac × 10^n + (ad + bc) × 10^(n/2) + bd
```

Karatsuba reduz de 4 para 3 multiplicações recursivas usando:
```
ad + bc = (a + b)(c + d) - ac - bd
```

### Explicação Detalhada do Código

```python
def karatsuba(x, y):
```
**Linha 5:** Define a função principal que recebe dois inteiros.

```python
    if x < 10 or y < 10:
        return x * y
```
**Linhas 9-12:** Caso base - quando um dos números tem apenas 1 dígito, realiza multiplicação direta.

```python
    n = max(len(str(x)), len(str(y)))
    m = n // 2
```
**Linhas 15-16:** Determina o tamanho do maior número e calcula o ponto médio para divisão.

```python
    a = x // (10 ** m)
    b = x % (10 ** m)
```
**Linhas 19-20:** Divide x em parte alta (a) e parte baixa (b).

```python
    c = y // (10 ** m)
    d = y % (10 ** m)
```
**Linhas 23-25:** Divide y em parte alta (c) e parte baixa (d).

```python
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
```
**Linhas 29-31:** Realiza as três multiplicações recursivas necessárias e retorna o resultado.

```python
    resultado = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd
    return resultado
```

## Relatório Técnico

### 1. Análise da Complexidade Ciclomática

#### Grafo de Fluxo de Controle

![Grafo de representação Karatsuba](IMG/Graph_Karatsuba.png)

#### Estrutura do Grafo
- **Nós (N):** 10
- **Arestas (E):** 11
- **Componentes Conexos (P):** 1

#### Cálculo da Complexidade Ciclomática
```
M = E - N + 2P
M = 11 - 10 + 2(1)
M = 11 - 10 + 2
M = 3
```

**Interpretação:** Complexidade ciclomática de 3 indica um código de baixa complexidade, bem estruturado e fácil de manter.

### 2. Análise da Complexidade Assintótica

#### Complexidade Temporal

##### Relação de Recorrência
```
T(n) = 3T(n/2) + O(n)
```

Onde:
- 3T(n/2): Três chamadas recursivas com metade do tamanho
- O(n): Operações de divisão e combinação

##### Aplicando o Teorema Mestre
Com a = 3, b = 2, f(n) = n:
- log_b(a) = log_2(3) ≈ 1.585
- Como f(n) = O(n^1) < O(n^1.585)

**Resultado:** T(n) = O(n^log₂3) ≈ O(n^1.585)

#### Complexidade Espacial

**S(n) = O(log n)**

A complexidade espacial é determinada pela profundidade da pilha de recursão, que é logarítmica em relação ao tamanho da entrada.

### 3. Análise dos Casos

#### Melhor Caso
- **Cenário:** Números com 1 dígito
- **Complexidade:** O(1)
- **Exemplo:** karatsuba(5, 7)
- **Comportamento:** Retorna imediatamente sem recursão

#### Caso Médio
- **Cenário:** Números com tamanhos balanceados
- **Complexidade:** O(n^1.585)
- **Exemplo:** karatsuba(1234, 5678)
- **Comportamento:** Divisões equilibradas em cada nível

#### Pior Caso
- **Cenário:** Números com muitos dígitos
- **Complexidade:** O(n^1.585)
- **Exemplo:** karatsuba(10^100, 10^100)
- **Comportamento:** Máxima profundidade de recursão

## Comparação com Multiplicação Tradicional

| Algoritmo | Complexidade Temporal | Complexidade Espacial |
|-----------|----------------------|----------------------|
| Tradicional | O(n²) | O(1) |
| Karatsuba | O(n^1.585) | O(log n) |

### Análise de Desempenho

Para números com `n` dígitos:
- **n < 10:** Tradicional é mais eficiente (menos overhead)
- **n > 100:** Karatsuba apresenta ganhos significativos
- **n > 1000:** Karatsuba pode ser 5-10x mais rápido

## Exemplos de Execução

### Exemplo 1: Números Pequenos
```
Input: 123 × 456
Processo:
  123 = 12 × 10¹ + 3
  456 = 45 × 10¹ + 6
  
  ac = 12 × 45 = 540
  bd = 3 × 6 = 18
  (a+b)(c+d) = 15 × 51 = 765
  ad + bc = 765 - 540 - 18 = 207
  
Resultado: 540 × 10² + 207 × 10¹ + 18 = 56088
```

### Exemplo 2: Números Grandes
```
Input: 123456789 × 987654321
Resultado: 121932631112635269
Tempo Karatsuba: ~0.0001s
Tempo Tradicional: ~0.0003s
Speedup: 3x
```

## Diagrama de Fluxo Visual

![Fluxo de Karatsuba](IMG/Fluxo_Karatsuba.png)

## 🛠️ Otimizações Implementadas

1. **Caso Base Otimizado:** Multiplicação direta para números < 10
2. **Reutilização de Cálculos:** ac e bd são calculados uma vez e reutilizados
3. **Redução de Multiplicações:** De 4 para 3 multiplicações recursivas

## 📚 Conclusão

O Algoritmo de Karatsuba representa um avanço significativo na multiplicação de inteiros grandes, oferecendo:

- **Eficiência Superior:** Complexidade O(n^1.585) vs O(n²) tradicional
- **Escalabilidade:** Ganhos crescentes com o tamanho dos números
- **Base Teórica:** Princípio divide-and-conquer aplicado elegantemente

A implementação demonstra claramente como técnicas algorítmicas avançadas podem resultar em melhorias substanciais de desempenho, especialmente em aplicações que envolvem criptografia, computação científica e processamento de números grandes.