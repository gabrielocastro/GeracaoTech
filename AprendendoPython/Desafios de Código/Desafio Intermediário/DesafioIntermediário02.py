# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado
# esquerda ingles / direita frances / nenhuma portugues /  ambas caiu
# Dado determinada string de entrada reportar a devida linguagem correta.

momento = " "
while momento != "PARE":
    try:
        momento = input().upper()
        if momento == "ESQUERDA":
            print("ingles")
        elif momento == "DIREITA":
            print("frances")
        elif momento == "NENHUMA":
            print("portugues")
        elif momento == "AMBAS":
            print("caiu")
        else:
            break
    except EOFError:
        break
