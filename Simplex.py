from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD
import io
import sys
import re


def simplex_solver(obj_func, constraints, problem_type="max"):
    """
    Resolve problemas de programação linear e retorna as iterações do método Simplex.
    Exibe os valores das variáveis durante as iterações.

    :param obj_func: String da função objetivo (exemplo: "24*x1 + 22*x2 + 45*x3").
    :param constraints: Lista de strings das restrições (exemplo: ["2*x1 + 1*x2 + 3*x3 <= 42"]).
    :param problem_type: Tipo do problema, "max" para maximizar ou "min" para minimizar.
    :return: Lista de iterações do solver e valores das variáveis finais.
    """
    # Criar o modelo
    if problem_type == "max":
        model = LpProblem(name="simplex_solver", sense=LpMaximize)
    elif problem_type == "min":
        model = LpProblem(name="simplex_solver", sense=LpMinimize)
    else:
        raise ValueError("O tipo do problema deve ser 'max' ou 'min'.")

    # Identificar variáveis na função objetivo
    variables = sorted(set(re.findall(r"x\d+", obj_func)))

    # Criar variáveis de decisão
    var_dict = {var: LpVariable(name=var, lowBound=0) for var in variables}

    # Adicionar a função objetivo ao modelo
    model += eval(obj_func, None, var_dict), "Função Objetivo"

    # Adicionar as restrições ao modelo
    for i, constraint in enumerate(constraints):
        model += eval(constraint, None, var_dict), f"Restrição_{i + 1}"

    # Capturar os logs do solver redirecionando a saída padrão
    solver = PULP_CBC_CMD(msg=True)
    log_stream = io.StringIO()
    sys.stdout = log_stream  # Redirecionar saída padrão
    model.solve(solver)
    sys.stdout = sys.__stdout__  # Restaurar saída padrão

    # Processar os logs capturados
    log_output = log_stream.getvalue()
    log_stream.close()

    # Analisar as iterações do método Simplex e os valores das variáveis
    iterations = []
    capture = False
    iteration_data = []
    for line in log_output.split("\n"):
        if "Iteration" in line:  # Início de uma iteração
            if iteration_data:  # Salvar dados da iteração anterior
                iterations.append("\n".join(iteration_data))
            iteration_data = [line]
            capture = True
        elif capture and line.strip():  # Adicionar linha à iteração atual
            iteration_data.append(line)
        elif capture and not line.strip():  # Final da iteração
            capture = False
            if iteration_data:
                iterations.append("\n".join(iteration_data))
                iteration_data = []
    # Obter valores finais das variáveis
    final_values = {var: var_dict[var].varValue for var in variables}

    return iterations, final_values


# Exemplo de uso
obj_func = "24*x1 + 22*x2 + 45*x3"
constraints = [
    "2*x1 + 1*x2 + 3*x3 <= 42",
    "2*x1 + 1*x2 + 2*x3 <= 40",
    "1*x1 + 0.5*x2 + 1*x3 <= 45"
]

# Resolver e exibir as iterações
iterations, final_values = simplex_solver(obj_func, constraints, problem_type="max")

# Exibir as iterações do método Simplex
print("\nIterações do método Simplex:")
for i, iteration in enumerate(iterations):
    print(f"\n📌 Iteração {i + 1}:\n{iteration}")

# Exibir resultado final
print("\nResultado final das variáveis de decisão:")
for var, value in final_values.items():
    print(f"{var}: {value}")
