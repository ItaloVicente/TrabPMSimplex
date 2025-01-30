from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD
import sys
import re

def simplex_solver(obj_func, constraints, problem_type="max"):
    """
    Resolve problemas de programação linear e retorna as iterações do método Simplex.
    Exibe os valores das variáveis durante as iterações e o valor final da função objetivo Z.

    :param obj_func: String da função objetivo (exemplo: "24*x1 + 22*x2 + 45*x3").
    :param constraints: Lista de strings das restrições (exemplo: ["2*x1 + 1*x2 + 3*x3 <= 42"]).
    :param problem_type: Tipo do problema, "max" para maximizar ou "min" para minimizar.
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

    return final_values, final_z


# Dados Questao 1
obj_func = "24*x1 + 22*x2 + 45*x3"
constraints = [
    "2*x1 + 1*x2 + 3*x3 <= 42",
    "2*x1 + 1*x2 + 2*x3 <= 40",
    "1*x1 + 0.5*x2 + 1*x3 <= 45"
]

final_values, final_z = simplex_solver(obj_func, constraints, problem_type="max")

# Exibir resultado final
print("\nResultado final das variáveis de decisão da Primeira Questao:")
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

    final_values, final_z = simplex_solver(value, constraints, ordem_itens_max_min[i])

    # Exibir resultado final
    print(f"\nResultado final das variáveis de decisão a Seungda Questao item {itens[i]}: ")
    for var, value in final_values.items():
        print(f"{var}: {value}")

    # Exibir valor final da função objetivo Z
    print(f"\n🔹 Valor final da função objetivo (Z): {final_z}")