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
```

## Questões

Primeira Questão (Maximização):

    O código resolve a função objetivo 24*x1 + 22*x2 + 45*x3 sujeita a 3 restrições.
    Retornando estes valores:
    x1: 0.0
    x2: 36.0
    x3: 2.0

    🔹 Valor final da função objetivo (Z): 882.0

Segunda Questão (Diversos Itens):

    São apresentados 4 itens, cada um com uma função objetivo diferente e com restrições variáveis. O código resolve esses problemas individualmente, dependendo se é um problema de maximização ou minimização.
    Retornando estes valores:

    Resultado final das variáveis de decisão a Segunda Questão item a: 
    x1: 6.4285714
    x2: 0.57142857
    x3: 0.0

    🔹 Valor final da função objetivo (Z): 14.57142851

    Resultado final das variáveis de decisão a Segunda Questão item b: 
    x1: 3.0
    x2: 0.0
    x3: 4.0
    
    🔹 Valor final da função objetivo (Z): -14.0

    Resultado final das variáveis de decisão a Segunda Questão item c: 
    x1: 6.4285714
    x2: 0.57142857
    x3: 0.0
    
    🔹 Valor final da função objetivo (Z): 7.57142854

    Resultado final das variáveis de decisão a Segunda Questão item d: 
    x1: 6.4285714
    x2: 0.57142857
    x3: 0.0
    
    🔹 Valor final da função objetivo (Z): 21.14285704
Terceira Questão (Maximização):

    O código resolve a função objetivo 8*x1 + 5*x2 com 3 restrições. Além disso, ele lida com o ajuste dinâmico da restrição de quantidade de chapéus do tipo 1.
    
    Retornando estes valores:

    Item a:
    Solução ótima do Chapéu tipo 1: 100.0
    Solução ótima do Chapéu tipo 2: 200.0
    
    🔹 Valor final da função objetivo (Z): 1800.0

    Item b: 

    Preços duais:
    Acréscimo/Decréscimo do preço dual da Restrição_3 (chapéu tipo 2): 1.0 (faixa aplicável: -0.0)

    Item c:
    O novo limite de valor de 120 na restrição 2 não exige que recalcule o simplex
    O novo valor de z é definido através do preço dual dessa restrição, que para cada unidade é de: -0.0, logo -0.0 x 30 = -0.0 e o novo z será: 1800.0

    Item d:
    O preço dual da participação de mercado do chapéu tipo 2 é: 1.0, ou seja, z aumente em 1 se a restrição 3 aumentar em um, desde que as outras restrições também sejam válidas.
    A participação de mercado do chapéu tipo 2 pode ser aumentada até o limite da faixa aplicável do preço dual da restrição, mantendo o valor equivalente por unidade. No seu caso, a faixa aplicável é -0.0.
    Isso significa que não há uma variação significativa permitida para aumentar a participação de mercado, já que a faixa aplicável não permite uma mudança. Portanto, a participação de mercado não pode ser aumentada de forma mensurável sem afetar a        restrição e a função objetivo.
