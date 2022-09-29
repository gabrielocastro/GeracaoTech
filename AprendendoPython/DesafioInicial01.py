# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

# Soluções:
# Solução01: Resolução feita de acordo com o modo de entrada sugerido no desafio.
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])
ICM = float(distancia/(diametro1 + diametro2))
print(f'{ICM:.2f}')

# Solução02: Uma solução que dialoga com o usuário final.
distanciaSS = int(input("A distância entre Sauron e Saruman é: "))
diametroS1 = int(input("O diâmetro do Palantír de Sauron é: "))
diametroS2 = int(input("O diâmetro do Palantír de Saruman é: "))

ICM = float(distanciaSS/(diametroS1 + diametroS2))
print(f'O ICM da comunicação dos Palatír de Sauron e Saruman é {ICM:.2f}!')
