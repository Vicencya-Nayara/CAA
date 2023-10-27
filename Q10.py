def tem_par_com_soma(S, x):
    S.sort()  # Ordenar o conjunto
    for i in range(len(S)):
        complemento = x - S[i]
        # Pesquisa binária para o complemento
        baixo, alto = i + 1, len(S) - 1
        while baixo <= alto:
            meio = (baixo + alto) // 2
            if S[meio] == complemento:
                return True
            elif S[meio] < complemento:
                baixo = meio + 1
            else:
                alto = meio - 1
    return False

# Função de teste
def teste():
    S = [1, 2, 3, 4]
    x = 5
    print(tem_par_com_soma(S, x))  

    x = 8
    print(tem_par_com_soma(S, x))  

teste()
