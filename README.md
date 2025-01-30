# Solver de Programação Linear - Simplex

Este repositório contém uma implementação de um **solucionador de programação linear** utilizando o método **Simplex** para resolver problemas de otimização linear. O código resolve várias questões relacionadas a problemas de maximização e minimização de funções objetivas sujeitas a restrições. O código foi desenvolvido em Python usando a biblioteca `PuLP`.

## Como Funciona

O código resolve um conjunto de problemas de programação linear, exibindo os resultados das variáveis de decisão e os valores finais da função objetivo. A cada iteração do método Simplex, ele exibe os valores das variáveis e o valor final da função objetivo \( Z \). O solver também exibe os preços duais e verifica se a alteração nas restrições afeta a solução ótima.

## Requisitos

- Python 3.x
- Biblioteca `PuLP` para resolver o problema de programação linear

Instale a biblioteca necessária com o seguinte comando:

```bash
pip install pulp


Como Usar

    Primeira Questão (Maximização):
        O código resolve a função objetivo 24*x1 + 22*x2 + 45*x3 sujeita a 3 restrições.

    Segunda Questão (Diversos Itens):
        São apresentados 4 itens, cada um com uma função objetivo diferente e com restrições variáveis. O código resolve esses problemas individualmente, dependendo se é um problema de maximização ou minimização.

    Terceira Questão (Maximização):
        O código resolve a função objetivo 8*x1 + 5*x2 com 3 restrições. Além disso, ele lida com o ajuste dinâmico da restrição de quantidade de chapéus do tipo 1.
