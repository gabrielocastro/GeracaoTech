# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
# 0 - 600.00 17% / 600.01 - 900.00 13% / 900.01 - 1500.00 12% / 1500.01 - 2000.00 10% / Acima de 2000.00 5%

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input())

if (salario >= 0 and salario <= 600):
    novo_salario = int(salario * 1.17)
    reajuste = int(salario * 0.17)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 17%")

elif (salario > 600 and salario <= 900):
    novo_salario = int(salario * 1.13)
    reajuste = int(salario * 0.13)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 13%")

elif (salario > 900 and salario <= 1500):
    novo_salario = int(salario * 1.12)
    reajuste = int(salario * 0.12)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 12%")

elif (salario > 1500 and salario <= 2000):
    novo_salario = int(salario * 1.10)
    reajuste = int(salario * 0.10)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 10%")

else:
    novo_salario = int(salario * 1.05)
    reajuste = int(salario * 0.05)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 05%")
