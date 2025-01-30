from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD
import sys
import re

def simplex_solver(obj_func, constraints, problem_type):
    """
    Resolve problemas de programação linear e retorna as iterações do método Simplex.
    Exibe os valores das variáveis durante as iterações e o valor final da função objetivo Z.

    :param obj_func: String da função objetivo (exemplo: "24*x1 + 22*x2 + 45*x3").
    :param constraints: Lista de strings das restrições (exemplo: ["2*x1 + 1*x2 + 3*x3 <= 42"]).
    :param problem_type: Tipo do problema, "max" para maximizar ou "min" para minimizar.
    :param msg: Serve para retornar mais detalhes do método se True.
    :return: Lista de iterações do solver, valores das variáveis finais e valor final de Z.
    """
    if problem_type == "max":
        model = LpProblem(name="simplex_solver", sense=LpMaximize)
    elif problem_type == "min":
        model = LpProblem(name="simplex_solver", sense=LpMinimize)
    else:
        raise ValueError("O tipo do problema deve ser 'max' ou 'min'.")

    variables = sorted(set(re.findall(r"x\d+", obj_func)))

    var_dict = {var: LpVariable(name=var, lowBound=0) for var in variables}

    model += eval(obj_func, None, var_dict), "Função Objetivo"

    for i, constraint in enumerate(constraints):
        model += eval(constraint, None, var_dict), f"Restrição_{i + 1}"

    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)
    sys.stdout = sys.__stdout__

    final_values = {var: var_dict[var].varValue for var in variables}

    final_z = model.objective.value()

    return final_values, final_z, model


# Dados Questao 1
obj_func = "24*x1 + 22*x2 + 45*x3"
constraints = [
    "2*x1 + 1*x2 + 3*x3 <= 42",
    "2*x1 + 1*x2 + 2*x3 <= 40",
    "1*x1 + 0.5*x2 + 1*x3 <= 45"
]

final_values, final_z, model = simplex_solver(obj_func, constraints, problem_type="max")

# Exibir resultado final
a = input(f"Pressione enter para ver o resultado da Primeira Questão")
print("\nResultado final das variáveis de decisão da Primeira Questão:")
for var, value in final_values.items():
    print(f"{var}: {value}")

# Exibir valor final da função objetivo Z
print(f"\n🔹 Valor final da função objetivo (Z): {final_z}")

#Questao 2
obj_func_question_2 = ["2*x1 + 3*x2 - 5*x3","2*x1 + 3*x2 - 5*x3","1*x1 + 2*x2 + 1*x3","4*x1 - 8*x2 + 3*x3"]
constraints = [
    "1*x1 + 1*x2 + 1*x3 == 7",
    "2*x1 - 5*x2 + 1*x3 >= 10",
]
ordem_itens_max_min = ["max", "min", "max", "min"]
itens= ["a","b","c","d"]

for i, value in enumerate(obj_func_question_2):

    final_values, final_z, model = simplex_solver(value, constraints, ordem_itens_max_min[i])

    # Exibir resultado final
    a = input(f"Pressione enter para ver o resultado da Segunda Questão item {itens[i]}")
    print(f"\nResultado final das variáveis de decisão a Segunda Questão item {itens[i]}: ")
    for var, value in final_values.items():
        print(f"{var}: {value}")

    # Exibir valor final da função objetivo Z
    print(f"\n🔹 Valor final da função objetivo (Z): {final_z}")

"""
Modelo Questão 3:
Z=8x1+5x2
Restrições:
2x1+x2≤400,
x1≤150,
x2≤200
"""

obj_func_question_3 = "8*x1 + 5*x2"
ordem = "max"
constraints = [
    "2*x1 + 1*x2 <= 400",
    "1*x1 <= 150",
    "1*x2 <= 200"
]
a = input(f"Pressione enter para ver o resultado da Terceira Questão")
final_values, final_z, model = simplex_solver(obj_func_question_3, constraints, problem_type=ordem)
# Exibir resultado final
print("\nResultado final das variáveis de decisão Terceira Questão:")
for var, value in enumerate(final_values):
    print(f"Solução ótima do Chapéu tipo {var+1}: {final_values[value]}")

# Exibir valor final da função objetivo Z
print(f"\n🔹 Valor final da função objetivo (Z): {final_z}")

a = input("Pressione enter para o item b: ")

print("\nPreços duais:")
for name, constraint in model.constraints.items():
    if name == "Restrição_3":
        print(f"Acréscimo/Decréscimo do preço dual da {name} (chapéu tipo 2): {constraint.pi} (faixa aplicável: {constraint.slack})")

print("\n\n")
#Na terceira questão, o novo limite é 120, mas dou a opção para o usuário passar um novo limite e o algoritmo verifica se é necessário fazer um novo modelo
a = (input("Pressione enter para o item c, passando como parâmetro a nova restrição na qnt de chapéus do tipo 1 (por padrão da questão é 120): "))
if a == "":
    a = 120
else:
    a = int(a)
#150 é o limite de x1 anteriormente
variavel_restricao = 150 - a

for name, constraint in model.constraints.items():
    if name == "Restrição_2":
        if variavel_restricao <= constraint.slack:
            print(f"O novo limite de valor de {a} na restrição 2 não exige que recalcule o simplex")
            print(f"O novo valor de z é definido através do preço dual dessa restrição, que para cada unidade é de: {constraint.pi}, logo {constraint.pi} x {variavel_restricao} = {constraint.pi*variavel_restricao} e o novo z será: {final_z + constraint.pi*variavel_restricao}")
        else:
            print("É necessário recalcular o simplex, superou a faixa aplicável")


print("\n\n")
a = (input("Pressione enter para o item d: "))

for name, constraint in model.constraints.items():
    if name == "Restrição_3":
        print(f"O preço dual da participação de mercado do chapéu tipo 2 é: {constraint.pi}, ou seja, z aumente em 1 se a restrição 3 aumentar em um, desde que as outras restrições também sejam válidas")
        print("A participação de mercado do chapéu tipo 2 pode ser aumentada até o limite da faixa aplicável do preço dual da restrição, mantendo o valor equivalente por unidade. No seu caso, a faixa aplicável é -0.0.")
        print("Isso significa que não há uma variação significativa permitida para aumentar a participação de mercado, já que a faixa aplicável não permite uma mudança. Portanto, a participação de mercado não pode ser aumentada de forma mensurável sem afetar a restrição e a função objetivo.")