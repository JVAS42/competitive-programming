"""
Problema: Fila (OBI 2014)
Categoria: Estruturas de Dados
Dificuldade: Fácil
IA: Moderado
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
