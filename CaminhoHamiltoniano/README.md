# PROJETO: ALGORITMO PARA CAMINHO HAMILTONIANO

## DESCRIÇÃO DO PROJETO

Implementação de um algoritmo de backtracking para encontrar caminhos hamiltonianos em grafos orientados e não orientados.

## LÓGICA DO ALGORITMO

1. Inicia com um vértice arbitrário
2. Explora recursivamente todos os vértices adjacentes não visitados
3. Faz backtracking quando um caminho não leva à solução
4. Retorna o primeiro caminho válido encontrado

## COMO EXECUTAR

PRÉ-REQUISITOS

- Python 3.13.x

## INSTALAÇÃO

#### Clone o repositório

```bash
git clone https://github.com/rfradieddine/fundamentos--projeto-analise-algoritmo
```

#### Execute o Script

```bash
python main.py
```

## RELATÓRIO TÉCNICO

COMPLEXIDADE COMPUTACIONAL

- Classe: NP-Completo
- Tempo: O(n!) no pior caso
- Espaço: O(n²) para matriz de adjacência

### JUSTIFICATIVA

1. NP: Soluções verificáveis em tempo polinomial
2. NP-Completo: Redutível ao Problema do Caixeiro Viajante
3. NP-Difícil: Versão de decisão é NP-Completa

### ANÁLISE DETALHADA

- Melhor caso: O(n) (raro)
- Caso médio: O(n^n)
- Limitação prática: n ≤ 20 para tempos razoáveis

## ANÁLISE DA COMPLEXIDADE ASSINTÓTICA DE TEMPO

1. Complexidade Temporal do Algoritmo:

- Pior caso: O(n!)
- Caso médio: O(n^n)
- Melhor caso: O(n)

2. Determinação da Complexidade:
Método utilizado: Contagem de operações por análise de árvore de recursão

- Cada chamada recursiva gera (n-1) subchamadas no nível seguinte
- Profundidade máxima da recursão: n vértices
- Total de combinações testadas: n × (n-1) × (n-2) × ... × 1 = n!

### APLICAÇÃO DO TEOREMA MESTRE

1. Aplicabilidade:

- Não aplicável neste algoritmo

2. Justificativa:

- O Teorema Mestre requer recorrências do tipo T(n) = aT(n/b) + f(n)
- Este algoritmo não divide o problema em subproblemas de tamanho n/b
- A estrutura de backtracking gera subproblemas de tamanho variável
- A recorrência real é T(n) = (n-1)T(n-1) + O(n), não se enquadrando nos casos do teorema

### ANÁLISE DOS CASOS DE COMPLEXIDADE

1. Diferenças entre os casos:

- Melhor caso (O(n)): Caminho encontrado na primeira tentativa
- Caso médio (O(n^n)): Necessidade de explorar parte exponencial das combinações
- Pior caso (O(n!)): Teste exaustivo de todas permutações possíveis

2. Impacto no Desempenho:

- Pior caso:
  - Tempo de execução explode rapidamente (n=15 → ~1.3 trilhões de operações)
  - Impraticável para n > 20 mesmo em hardware potente
  
- Caso médio:
  - Performance altamente dependente da estrutura do grafo
  - Grafos densos tendem a ter melhor desempenho que esparsos
  
- Melhor caso:
  - Raro na prática, mas possível em grafos com caminho óbvio
  - Útil para validação rápida em testes específicos

### OBSERVAÇÕES ADICIONAIS

- Complexidade espacial: O(n²) para matriz de adjacência + O(n) para pilha de recursão
- Fator de redução prática: Podem existir otimizações com heurísticas de seleção de vértices

## EXEMPLO

### Entrada

Grafo não-orientado com 5 vértices:
0-1, 0-3, 1-2, 1-3, 1-4, 2-4, 3-4

### Saída

Caminho Hamiltoniano encontrado:
0 -> 1 -> 2 -> 4 -> 3

## REFERÊNCIAS

- [Cormen, T.H. et al. "Introduction to Algorithms](https://mitpress.mit.edu/9780262530910/introduction-to-algorithms/)
