"""
Problema: Copa do Mundo (OBI 2010)
Categoria: Estruturas de Dados
Dificuldade: Fácil
IA:
Link: https://neps.academy/exercise/276
"""
def main():
    times_disputando = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    vencedeores = list()

    while len(times_disputando) > 1:
        for i in range(0, len(times_disputando), 2):
            placar = list(map(int, input().split()))
            if placar[0] > placar[1]:
                vencedeores.append(times_disputando[i])
            else:
                vencedeores.append(times_disputando[i+1])
            placar.clear()

        times_disputando = vencedeores[:]
        vencedeores.clear()

    print(times_disputando[0])


if __name__ == "__main__":
    main()