"""
Problema: Frequência na Aula
Categoria: Estruturas de Dados
Dificuldade: Fácil
IA: Não Foi Usado
Link: https://neps.academy/exercise/252
"""
def main():
    registros = list()
    n = int(input())
    for i in range(0, n):
        registro = int(input())
        registros.append(registro)

    registros = set(registros)
    print(len(registros))


if __name__ == "__main__":
    main()
