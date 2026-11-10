"""
Problema: Fila (OBI 2014)
Categoria: Estruturas de Dados
Dificuldade: Fácil
Link: https://neps.academy/exercise/384
"""
def main():
    # Primeira parte: Tamanho e identificadores da fila inicial
    n = int(input())
    fila_inicial = input().split()

    # Segunda parte: Tamanho e identificadores das pessoas que saíram
    m = int(input())
    # O uso de set() converte a lista para uma estrutura de busca rápida O(1)
    sairam = set(input().split())

    # Terceira parte: Construir a nova fila filtrando quem saiu
    fila_final = [pessoa for pessoa in fila_inicial if pessoa not in sairam]

    # Impressão do resultado num único passo
    print(fila_final)
    print(" ".join(fila_final))


if __name__ == "__main__":
    main()

"""
def main():
    # PRIMEIRA PARTE: DEFININDO O TAMANHO DA FILA E ADICIONANDO O IDENTIFICADORES NA FILA
    fila = []
    incial_tam = int(input())

    inicial_indentificadores = input().split()
    inicial_indentificadores = list(map(int, inicial_indentificadores))
    inicial_indentificadores =  list(dict.fromkeys(inicial_indentificadores))

    for i in range(incial_tam):
        fila.append(inicial_indentificadores[i])

    # SEGUNDA PARTE: DEFININDO O TAMANHO DA EVASAO E OS IDENTIFICADORES
    evesao = []
    evesao_tam = int(input())

    evesao_indentificadores = input().split()
    evesao_indentificadores = list(map(int, evesao_indentificadores))
    evesao_indentificadores = list(dict.fromkeys(evesao_indentificadores))

    for i in range(evesao_tam):
        evesao.append(evesao_indentificadores[i])

    # TERCEIRA PARTE: REMOVENDO EVASAO DA FILA E MOSTRANDO A FILA FINAL
    for pos in fila[:]:
        if pos in evesao:
            fila.remove(pos)

    for pos in range(len(fila)-1):
        print(fila[pos], end=" ")
    print(fila[-1], end="")

if __name__ == "__main__":
    main()
"""
