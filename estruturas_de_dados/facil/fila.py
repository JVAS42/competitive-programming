"""
Problema: Fila (OBI 2014)
Categoria: Estruturas de Dados
Dificuldade: Fácil
Link: https://neps.academy/exercise/384
"""
def criar_fila(n, linha_inicial):
    lista_fila = [int(numero) for numero in linha_inicial.split()]
    return lista_fila


def atualizar_fila(fila_atual, quem_saiu_str):
    conjunto_saida = set(int(numero) for numero in quem_saiu_str.split())
    nova_fila = [pessoa for pessoa in fila_atual if pessoa not in conjunto_saida]
    return nova_fila


def principal():
    tamanho_inicial = int(input())
    fila_inicial_str = input()
    fila_atual = criar_fila(tamanho_inicial, fila_inicial_str)

    qtd_sairam = int(input())
    quem_saiu_str = input()
    fila_final = atualizar_fila(fila_atual, quem_saiu_str)

    print(*fila_final)


if __name__ == "__main__":
    principal()