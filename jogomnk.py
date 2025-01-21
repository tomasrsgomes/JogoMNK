
##MNK - FP - Projeto 1

'''
Este projeto tem como objetivo escrever um programa em Python3 que permita jogar o jogo MNK.

Tomás Gomes
'''

#2.1
#2.1.1
def eh_tabuleiro(arg): 
    '''
    Verifica se é um tabuleiro

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento \
        corresponde a um tabuleiro e False caso contrário.
    eh_tabuleiro: universal --> booleano
    '''

    if not(type(arg) == tuple and 2 <= len(arg) <= 100):          
        return False
    
    for linha in arg:
        if not(type(linha) == tuple and 2 <= len(linha) <= 100):
            return False
        for valor in linha:
            if type(valor) != int or (valor != -1 and valor != 0 \
                and valor != 1):
                return False
    
    for linha in range(len(arg)-1):
        if len(arg[linha]) != len(arg[linha+1]):
            return False

    return True


#2.1.2
def eh_posicao(arg):
    '''
    Verifica se é uma posição de um tabuleiro

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento \
        corresponde a uma poscição de um tabuleiro e False caso contrário.
    eh_posicao: universal --> booleano
    '''

    return type(arg) == int and 1 <= arg <= 100**2


#2.1.3
def obtem_dimensao(tab):
    '''
    Obtem a dimensão de um tabuleiro --> (m,n)

    Recebe um tabuleiro e devolve um tuplo formado pelo número de linhas (m) \
        e colunas (n) do tabuleiro.
    obtem_dimensao: tabuleiro --> tuplo
    '''
    
    return (len(tab),len(tab[0]))


#2.1.4
def obtem_valor(tab, pos):
    '''    
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve o valor contido \
        nessa posição

    obtem_valor: tabuleiro X posicao --> inteiro
    '''

    l,c = obtem_coordenadas(tab,pos)

    return tab[l-1][c-1]


#2.1.5
def obtem_coluna(tab, pos):
    '''
    Obtem as posições da coluna de uma posição

    Recebe um tabuleiro e uma posição do tabuleiro, e devolve um tuplo com \
        todas as posições que formam a coluna em que está contida a posição, \
        ordenadas de menor a maior.
    obtem_coluna: tabuleiro X posicao --> tuplo
    '''

    m,n = obtem_coordenadas(tab, pos)
    l,c = obtem_dimensao(tab)

    coluna = ()
    for linha in range(1, l+1):
        pos_linha = (linha-1)*c + n
        coluna += (pos_linha,)
    
    return coluna


#2.1.6
def obtem_linha(tab, pos):
    '''
    Obtem as posições da linha de uma posição

    Recebe um tabuleiro e uma posição do tabuleiro, e devolve um tuplo com todas \
        as posições que formam a linha em que esta contida a posição, ordenadas de menor a maior.
    obtem_linha: tabuleiro X posicao --> tuplo
    '''

    l,c = obtem_coordenadas(tab, pos)
    m,n = obtem_dimensao(tab)

    pos_linha = (l - 1) * n + 1
    linha = (pos_linha,)
    for coluna in range(1, n):
        pos_linha += 1
        linha += (pos_linha,)

    return linha


#2.1.7
def obtem_diagonais(tab, pos):
    '''
    Obtem diagonal e antidiagonal que passam numa posição

    Recebe um tabuleiro e uma posição o do tabuleiro, e devolve o tuplo formado \
        por dois tuplos de posições correspondentes à diagonal (descendente da  \
        esquerda para a direita ) e antidiagonal (ascendente da esquerda para a \
        direita) que passam pela posição, respetivamente.
    obtem_diagonais: tabuleiro X posicao --> tuplo     
    '''

    l,c = obtem_coordenadas(tab, pos)
    m,n = obtem_dimensao(tab)
    pos_max = m*n

    #diagonal de cima
    posicao_dc = pos
    diagonal_c = ()
    count_colunas_dc = 1
    while posicao_dc - n - 1 > 0 and count_colunas_dc < c:
        posicao_dc = posicao_dc - n - 1
        diagonal_c = (posicao_dc,) + diagonal_c           
        count_colunas_dc += 1

    #diagonal de baixo
    posicao_db = pos
    diagonal_b = ()
    count_colunas_db = 1
    while posicao_db + n + 1 <= pos_max and count_colunas_db <= n - c:
        posicao_db = posicao_db + n + 1
        diagonal_b = diagonal_b + (posicao_db,)              
        count_colunas_db += 1

    ##diagonal
    diagonal = diagonal_c + (pos,) + diagonal_b


    #antidiagonal de cima
    posicao_ac = pos
    antidiagonal_c = ()
    count_colunas_ac = 1
    while posicao_ac - n + 1 > 1 and count_colunas_ac <= n - c:
        posicao_ac = posicao_ac - n + 1
        antidiagonal_c = antidiagonal_c + (posicao_ac,)
        count_colunas_ac += 1
    
    #antidiagonal de baixo
    posicao_ab = pos
    antidiagonal_b = ()
    count_colunas_ab = 1
    while posicao_ab + n - 1 < pos_max and count_colunas_ab < c:
        posicao_ab = posicao_ab + n - 1
        antidiagonal_b = (posicao_ab,) + antidiagonal_b
        count_colunas_ab += 1

    ##antidiagonal
    antidiagonal = antidiagonal_b + (pos,) + antidiagonal_c


    return (diagonal,antidiagonal)


#2.1.8
def tabuleiro_para_str(tab):
    '''
    Transforma o tabuleiro numa string

    Recebe um tabuleiro e devolve a cadeia de caracteres que o representa \
        (a representação externa ou representação “para os nossos olhos”).
    tabuleiro_para_str: tabuleiro --> string
    '''

    m,n = obtem_dimensao(tab)
    
    tabuleiro = ''
    coluna = 0
    n_linha = 0

    for linha in tab:
        for valor in linha:
            if valor == -1:
                tabuleiro += 'O'
                coluna += 1
            elif valor == 0:
                tabuleiro += '+'
                coluna += 1
            elif valor == 1:
                tabuleiro += 'X'
                coluna += 1
            if coluna != n:
                tabuleiro += '---'
        
        n_linha += 1
        coluna = 0
        if n_linha != m:
            tabuleiro += '\n' + '|   ' * (n-1) + '|\n'
    
    return tabuleiro
            


#2.2
#2.2.1
def eh_posicao_valida(tab, pos):
    '''
    Verefica se é uma posição válida do tabuleiro
    
    Recebe um tabuleiro e uma posição, e devolve True se aposição \
        corresponde a uma posição do tabuleiro, e False caso contrário
    eh_posicao_valida: tabuleiro X posicao --> booleano
    '''

    if not(eh_tabuleiro(tab) and eh_posicao(pos)):
        raise ValueError ('eh_posicao_valida: argumentos invalidos')
    
    m,n = obtem_dimensao(tab)
    pos_max = m * n

    return pos <= pos_max


#2.2.2
def eh_posicao_livre(tab, pos):
    '''
    Verifica se é uma posição livre do tabuleiro

    Recebe um tabuleiro e uma posição do tabuleiro, e devolve True se a \
        posição corresponde a uma posição livre (não ocupada por pedras), \
        e False caso contrário.
    eh posicao livre: tabuleiro X posicao --> booleano
    '''

    if not(verifica_argumentos(tab,pos,1,1)):                                     
        raise ValueError ('eh_posicao_livre: argumentos invalidos')
    

    return obtem_valor(tab, pos) == 0


#2.2.3
def obtem_posicoes_livres(tab):
    '''
    Obtem as posições livres de um tabuleiro

    Recebe um tabuleiro e devolve o tuplo com todas as posições \
        livres do tabuleiro, ordenadas de menor a maior.
    obtem_posicoes_livres: tabuleiro --> tuplo
    '''

    if not eh_tabuleiro(tab):
        raise ValueError ('obtem_posicoes_livres: argumento invalido')
    
    posicao = 1
    pos_livres = ()
    for linha in tab:
        for valor in linha:
            if valor == 0:
                pos_livres += (posicao,)
            posicao += 1
    
    return pos_livres


#2.2.4
def obtem_posicoes_jogador(tab, jog):
    '''
    Obtem as posições de um dos jogadores no tabuleiro

    Recebe um tabuleiro e um inteiro identificando um jogador  e devolve \
        o tuplo com todas as posições do tabuleiro ocupadas por pedras do \
        jogador, ordenadas de menor a maior.
     obtem_posicoes_jogador: tabuleiro X inteiro --> tuplo
    '''

    if not(verifica_argumentos(tab,1,jog,1)):
        raise ValueError ('obtem_posicoes_jogador: argumentos invalidos')
    
    posicao = 1
    pos_jogador = ()
    for linha in tab:
        for valor in linha:
            if valor == jog:
                pos_jogador += (posicao,)
            posicao += 1
    
    return pos_jogador


#2.2.5
def obtem_posicoes_adjacentes(tab, pos):
    '''
    Obtem as posições adjacentes a uma certa posição no tabuleiro

    Recebe um tabuleiro e uma posição do tabuleiro, e devolve o tuplo formado \
        pelas posição do tabuleiro adjacentes (horizontal, vertical e  \
        diagonal), ordenadas de menor a maior.
    obtem_posicoes_adjacentes: tabuleiro X posicao --> tuplo
    '''

    if not (verifica_argumentos(tab, pos, 1, 1)):
        raise ValueError ('obtem_posicoes_adjacentes: argumentos invalidos')

    posicao = 1
    pos_adjacentes = ()
    for linha in tab:
        for valor in linha:
            if obtem_distancia(tab, posicao, pos) == 1:
                pos_adjacentes += (posicao,)
            posicao += 1
    
    return pos_adjacentes


#2.2.6
def ordena_posicoes_tabuleiro(tab, tup):
    '''
    Ordena posições de acordo com a distância ao centro

    Recebe um tabuleiro e um tuplo de posições do tabuleiro, e devolve o \
        tuplo com as posições em ordem ascendente de distância à posição \
        central do tabuleiro.
    ordena_posicoes_tabuleiro: tabuleiro X tuplo --> tuplo
    '''

    if not (eh_tabuleiro(tab) and type(tup) == tuple):
        raise ValueError ('ordena_posicoes_tabuleiro: argumentos invalidos')

    pos_central = obtem_posicao_central(tab)
    lst_pos_ordenadas = []
    for elem_tup in tup:

        if not (eh_posicao(elem_tup) and eh_posicao_valida(tab, elem_tup)):
            raise ValueError ('ordena_posicoes_tabuleiro: argumentos invalidos')

        dist_central_tup = obtem_distancia(tab, elem_tup, pos_central)
        for pos_lst in range(len(lst_pos_ordenadas)):
            
            if elem_tup in lst_pos_ordenadas:
                break

            dist_central_lst = obtem_distancia(tab, \
                lst_pos_ordenadas[pos_lst], pos_central)
            
            if dist_central_lst == dist_central_tup and \
                elem_tup < lst_pos_ordenadas[pos_lst]:
                lst_pos_ordenadas.insert(pos_lst, elem_tup)
            
            elif dist_central_lst > dist_central_tup:
                lst_pos_ordenadas.insert(pos_lst, elem_tup)
        
        if elem_tup not in lst_pos_ordenadas:
            lst_pos_ordenadas.append(elem_tup)

    return tuple(lst_pos_ordenadas)
                
        
#2.2.7
def marca_posicao(tab, pos, jog):
    '''
    Marca a jogada de um jogador numa posição livre do tabuleiro

    Recebe um tabuleiro, uma posição livre do tabuleiro e um inteiro \
        identificando um jogador e devolve um novo tabuleiro com uma \
        nova pedra do jogador indicado nessa posição.
    marca_posicao: tabuleiro X posicao X inteiro --> tabuleiro 
    '''

    if not(verifica_argumentos(tab, pos, jog, 1) and eh_posicao_livre(tab, pos)):
        raise ValueError ('marca_posicao: argumentos invalidos')
    
    l,c = obtem_coordenadas(tab, pos)
    tab_lst = list(tab)
    linha_lst = list(tab_lst[l-1])
    linha_lst[c-1] = jog
    tab_lst[l-1] = tuple(linha_lst)

    return tuple(tab_lst)
    

#2.2.8
def verifica_k_linhas(tab, pos, jog, k): 
    '''
    Verifica se existe uma sequência de k elementos de um jogador numa certa \
        posição do tabuleiro

    Recebe um tabuleiro, uma posição do tabuleiro, um valor inteiro \
        identificando um jogador e um valor inteiro positivo k, e devolve \
        True se existe pelo menos uma linha (horizontal, vertical ou \
        diagonal) que contenha a posição \
        com k ou mais pedras consecutivas do jogador indicado , e False \
        caso contrário.
    verifica_k_linhas: tabuleiro X posicao X inteiro X inteiro --> booleano
    '''

    if not(verifica_argumentos(tab, pos, jog, k)):
        raise ValueError ('verifica_k_linhas: argumentos invalidos')
    

    if obtem_valor(tab, pos) != jog:
        return False


    linha = obtem_linha(tab, pos)
    coluna = obtem_coluna(tab, pos)
    diagonal, antidiagonal = obtem_diagonais(tab, pos)

    #Definição de função auxiliar de verificação
    def verifica(var):
        '''
        Auxilia a função verifica_k_linhas

        Verifica se existe uma sequência de k elementos de um jogador numa certa \
        linha (horizontal, vertical ou diagonal que passe numa certa \
        posição do tabuleiro.
        verifica: var --> booleano
        '''
        count = 0
        for posicao in var:
            if obtem_valor(tab, posicao) == jog:
                count += 1
                indice = var.index(posicao)
                if count >= k and pos in var[indice-count+1:indice+1]:
                    return True
            else:
                count = 0
        return False

    
    #verificação
    if verifica(linha) or verifica(coluna) or verifica(diagonal) or verifica(antidiagonal):
        return True    
    return False



#2.3
#2.3.1
def eh_fim_jogo(tab, k):
    '''
    Verifica se o jogo acabou

    Recebe um tabuleiro e um valor inteiro positivo k, e devolve um booleano a \
        indicar se o jogo terminou (True) ou não (False). Um jogo pode terminar \
        caso um dos jogadores tenha k pedras consecutivas, ou caso já não existam \
        mais pocsições livres para marcar. 
    eh_fim_jogo: tabuleiro X inteiro --> booleano
    '''

    m,n = obtem_dimensao(tab)

    if not(verifica_argumentos(tab,1,1,k)):
        raise ValueError ('eh_fim_jogo: argumentos invalidos')
    
    pos_max = m*n
    for pos in range(1, pos_max + 1):
        if verifica_k_linhas(tab, pos, 1, k) or \
            verifica_k_linhas(tab, pos, -1, k) or \
            obtem_posicoes_livres(tab) == ():
            return True
    return False
    

#2.3.2
def escolhe_posicao_manual(tab):
    '''
    Recebe um tabuleiro e devolve uma posição livre introduzida pelo jogador
    Enquanto o jogador não introduzir uma posição livre, continua a pedir posição.
    escolhe_posicao_manual: tabuleiro X posicao
    '''

    if not eh_tabuleiro(tab):
        raise ValueError ('escolhe_posicao_manual: argumento invalido')
    
    pos = input('Turno do jogador. Escolha uma posicao livre: ')
    if pos.isnumeric():
        pos = int(pos)

    while not(eh_posicao(pos) and eh_posicao_valida(tab, pos) and \
            eh_posicao_livre(tab, pos)):
        pos = input('Turno do jogador. Escolha uma posicao livre: ')
        if pos.isnumeric():
            pos = int(pos)

    return pos


#2.3.3
def escolhe_posicao_auto(tab, jog, k, lvl):
    '''
    Escolhe automaticamente a posição a jogar de acordo com a dificuldade escolhida

    Recebe um tabuleiro (em que o jogo não terminou ainda), um inteiro \
        identificando um jogador, um inteiro positivo correspondendo ao valor \
        k dum jogo m, n, k, e a cadeia de carateres correspondente à estratégia, \
        e devolve a posição escolhida automaticamente de acordo com a estratégia \
        selecionada.
    Sempre que houver mais do que uma posição que cumpra um dos critérios \
        definidos nas estratégias anteriores, deve escolher a posição mais \
        próxima da posição central do tabuleiro.
    escolhe_posicao_auto: tabuleiro X inteiro X inteiro X cad. carateres --> posicao 
    '''

    m,n = obtem_dimensao(tab)

    if not verifica_argumentos(tab,1,jog,k) or (lvl != 'facil' and lvl != 'normal' \
        and lvl != 'dificil') or eh_fim_jogo(tab,k):
        raise ValueError ('escolhe_posicao_auto: argumentos invalidos')
    

    #------------------ Definição das funções de estratégia ------------------#
    
    def estrategia_facil():
        '''
        Se existir no tabuleiro pelo menos uma posição livre e adjacente a \
            uma pedra própria, jogar numa dessas posições;
        Se não, jogar numa posição livre.
        '''
        
        pos_livres_ord = ordena_posicoes_tabuleiro(tab, \
            obtem_posicoes_livres(tab))

        for pos in pos_livres_ord:
            posicoes_adj = obtem_posicoes_adjacentes(tab, pos)
            for pos_adj in posicoes_adj:
                valor_adj = obtem_valor(tab, pos_adj)
                if valor_adj == jog:
                    return pos
                
        return pos_livres_ord[0]


    def estrategia_normal(tab, jog, k):
        '''
        Determinar o maior valor de L ≤ k tal que o próprio ou o adversário \
            podem conseguir colocar L peças consecutivas na próxima jogada numa \
            linha vertical, horizontal ou diagonal que contenha essa jogada. \
            Para esse valor:
        Se existir pelo menos uma posição que permita obter uma linha que \
            contenha essa posição com L pedras consecutivas próprias, jogar \
            numa dessas posições;
        Se não, jogar numa posição que impossibilite o adversário de obter L \
            pedras consecutivas numa linha que contenha essa posição.

        '''
        
        pos_central = obtem_posicao_central(tab)

        if obtem_posicoes_jogador(tab, jog) == () and \
            eh_posicao_livre(tab, pos_central):
            return obtem_posicao_central(tab)
        elif obtem_posicoes_jogador(tab, jog) == () and not \
            eh_posicao_livre(tab, pos_central):
            return obtem_posicoes_adjacentes(tab, pos_central)[0]
        
        pos_livres_ord = ordena_posicoes_tabuleiro(tab, \
            obtem_posicoes_livres(tab))


        #-1 --> _m1 (nas variáveis) --> obtemos lm1 e posicao_m1
        x = 0
        for lm1 in range(k, 0, -1):
            
            for posicao_m1 in pos_livres_ord:
                novo_tab_m1 = marca_posicao(tab, posicao_m1, -1)
                if verifica_k_linhas(novo_tab_m1, posicao_m1, -1, lm1):
                    x = 1
                    break
            
            if x == 1:
                break


        #1 --> obtemos l1 e posicao_1
        y = 0
        for l1 in range(k, 0, -1): 

            for posicao_1 in pos_livres_ord:
                novo_tab_1 = marca_posicao(tab, posicao_1, 1)
                if verifica_k_linhas(novo_tab_1, posicao_1, 1, l1):
                    y = 1
                    break

            if y == 1:
                break


        #posição a jogar
        if l1 == lm1 and jog == 1:
            return posicao_1
        elif l1 == lm1 and jog == -1:
            return posicao_m1
        elif l1 < lm1:
            return posicao_m1
        else:
            return posicao_1


    def estrategia_dificil():
        '''
        Se existir pelo menos uma posição que permita obter uma linha própria \
            com k pedras consecutivas (e ganhar o jogo), jogar numa dessas posições;
        Se não, e se existir pelo menos uma posição que impossibilite ao \
            adversário de obter uma linha com k pedras consecutivas (e ganhar \
            o jogo), jogar numa dessas posições;
        Se não, para cada posição livre, simular um jogo até ao fim em que o \
            jogador atual joga nessa posição e o resto de jogadas são \
            determinadas assumindo que os dois jogadores alternadamente \
            (o adversário e o próprio) jogam seguindo uma estratégia de jogo \
            normal. Registar o resultado de cada simulação e escolher a \
            posição que leva ao melhor resultado possível, isto é:
        Se existir pelo menos uma posição/simulação que permitiria ganhar o \
            jogo, jogar numa dessas posições;
        Se não, e se existir pelo menos uma posição/simulação que permitiria \
            empatar o jogo, escolher uma dessas posições;
        Se não, jogar numa posição livre
        '''

        
        pos_livres_ord = ordena_posicoes_tabuleiro(tab,\
            obtem_posicoes_livres(tab))

        adv = jog * -1

        #Ganha na próxima jogada?
        for pos_jog in pos_livres_ord:
            novo_tab_jog = marca_posicao(tab, pos_jog, jog)
            if verifica_k_linhas(novo_tab_jog, pos_jog, jog, k):
                return pos_jog
        

        #Impede adversário de ganhar na próxima jogada? 
        for pos_adv in pos_livres_ord:
            novo_tab_adv = marca_posicao(tab, pos_adv, adv)
            if verifica_k_linhas(novo_tab_adv, pos_adv, adv, k):
                return pos_adv
        

        #Simulação de jogo completo
        ##Vitória
        for pos_jog_s in pos_livres_ord:
            novo_tab_sim = marca_posicao(tab, pos_jog_s, jog)
            
            while not eh_fim_jogo(novo_tab_sim,k):
                pos_adv_sim = estrategia_normal(novo_tab_sim, adv, k)
                novo_tab_sim = marca_posicao(novo_tab_sim, pos_adv_sim, adv)
                if eh_fim_jogo(novo_tab_sim,k):
                    break

                pos_jog_sim = estrategia_normal(novo_tab_sim, jog, k)
                novo_tab_sim = marca_posicao(novo_tab_sim, pos_jog_sim,jog)
                if eh_fim_jogo(novo_tab_sim, k) and \
                    obtem_posicoes_livres(novo_tab_sim)!=():
                    return pos_jog_s
        

        #Simulação Empate
        for pos_jog_s in pos_livres_ord:
            novo_tab_sim = marca_posicao(tab, pos_jog_s, jog)
            
            while (not eh_fim_jogo(novo_tab_sim,k)):
                pos_adv_sim = estrategia_normal(novo_tab_sim, adv, k)
                novo_tab_sim = marca_posicao(novo_tab_sim, pos_adv_sim, adv)
                if eh_fim_jogo(novo_tab_sim,k):
                    if obtem_posicoes_livres(novo_tab_sim)==():
                        return pos_jog_s
                    else:
                        break

                pos_jog_sim = estrategia_normal(novo_tab_sim, jog, k)
                novo_tab_sim = marca_posicao(novo_tab_sim, pos_jog_sim,jog)
                if eh_fim_jogo(novo_tab_sim, k) and \
                    obtem_posicoes_livres(novo_tab_sim)==():
                    return pos_jog_s
                
        #Derrota
        return pos_livres_ord[0]
    
    #-------------------------------------------------------------------------#

    #Escolha da estratégia
    if lvl == 'facil':
        return estrategia_facil()

    elif lvl == 'normal':
        return estrategia_normal(tab, jog, k)
    
    else:
        return estrategia_dificil()


#2.3.4
def jogo_mnk(cfg, jog, lvl):
    '''
    Permite jogar o jogo - função principal

    É a função principal que permite jogar um jogo completo m, n, k de um \
        jogador contra o computador. A função recebe um tuplo de três valores \
        inteiros correspondentes aos valores de configuração do jogo m, n e \
        k; um inteiro identificando a cor das pedras do jogador humano; e uma \
        cadeia de caracteres identificando a estratégia de jogo utilizada \
        pela máquina. O jogo começa sempre com o jogador com pedras pretas a \
        marcar uma posição livre e termina quando um dos jogadores vence ou \
        se não existirem posições livres no tabuleiro. A função mostra o \
        resultado do jogo (VITORIA, DERROTA ou EMPATE) e devolve um inteiro \
        identificando o jogador vencedor (1 para preto ou -1 para branco), \
        ou 0 em caso de empate.
    jogo_mnk: tuplo X inteiro X cad. carateres --> inteiro
    '''

    if not(type(cfg) == tuple and len(cfg) == 3 and type(jog) == int and \
           (jog == 1 or jog == -1) and (lvl == 'facil' or lvl == 'normal' or \
            lvl == 'dificil')):
        raise ValueError ('jogo_mnk: argumentos invalidos')

    m , n, k = cfg

    if not(type(m)==int and 2 <= m <= 100 and type(n)==int and 2 <= n <= 100 \
           and type(k)==int and k > 0):
        raise ValueError ('jogo_mnk: argumentos invalidos')

    
    bot = jog*-1
    tab = ((0,)*n,)*m
    tab_str = tabuleiro_para_str(tab)


    #Jogador joga com O - O computador começao
    if jog == -1:

        print("O jogador joga com 'O'.")
        print(tab_str)
        print()

        while not eh_fim_jogo(tab, k):
            pos_bot = escolhe_posicao_auto(tab, bot, k, lvl)

            cont = '0'
            while not cont == '':
                cont = input(f'Turno do computador ({lvl}):' )
                
            tab = marca_posicao(tab, pos_bot, bot)
            tab_str = tabuleiro_para_str(tab)
            print(tab_str)
            print()
            if verifica_k_linhas(tab,pos_bot,bot,k):
                print('DERROTA')
                return bot
            elif eh_fim_jogo(tab,k):
                print('EMPATE')
                return 0
           
            pos_jog = escolhe_posicao_manual(tab)
            tab = marca_posicao(tab, pos_jog, jog)
            tab_str = tabuleiro_para_str(tab)
            print(tab_str)
            print()
            if verifica_k_linhas(tab, pos_jog, jog, k):   
                print('VITORIA') 
                return jog
            elif eh_fim_jogo(tab, k): 
                print('EMPATE')
                return 0
            

    #O jogador joga com X - o jogador começa
    else:

        print("O jogador joga com 'X'.")
        print(tab_str)
        print()

        while not eh_fim_jogo(tab, k):
            pos_jog = escolhe_posicao_manual(tab)
            tab = marca_posicao(tab, pos_jog, jog)
            tab_str = tabuleiro_para_str(tab)
            print(tab_str)
            print()
            if verifica_k_linhas(tab, pos_jog, jog, k):   
                print('VITORIA') 
                return jog
            elif eh_fim_jogo(tab, k): 
                print('EMPATE')
                return 0

            pos_bot = escolhe_posicao_auto(tab, bot, k, lvl)

            cont = ' '
            while not cont == '':
                cont =str(input(f'Turno do computador ({lvl}):' ))
            
            tab = marca_posicao(tab, pos_bot, bot)
            tab_str = tabuleiro_para_str(tab)
            print(tab_str)
            print()
            if eh_fim_jogo(tab, k) and not verifica_k_linhas(tab, pos_bot, bot, k):
                print('EMPATE')
                return 0            
            elif verifica_k_linhas(tab, pos_bot, bot, k):
                print('DERROTA')
                return bot


#---------------------------- Funções Auxiliares ----------------------------#

def obtem_coordenadas(tab,pos):
    '''
    Obtem as coordenadas de uma posicao de um tabuleiro --> (l,c)

    Recebe um tabuleiro e uma posição e devolve um tuplo com as cordenadas \
        (linha,coluna) dessa posição.
    obtem_coordenadas: tabuleiro X posicao --> tuplo
    '''
    
    m,n = obtem_dimensao(tab)

    linha = 1
    while linha*n < pos:
        linha += 1

    posicao = (linha - 1) * n + 1
    coluna = 1
    while posicao != pos:
        coluna += 1
        posicao +=1
    
    return (linha,coluna)


def obtem_distancia(tab, pos1, pos2):
    '''
    Recebe um tabuleiro e duas posições e devolve a distância entre elas
    obtem_distancia: tabuleiro X posicao X posicao --> inteiro
    '''

    l1, c1 = obtem_coordenadas(tab, pos1)
    l2, c2 = obtem_coordenadas(tab, pos2)

    return max(abs(l2-l1), abs(c2-c1))


def obtem_posicao_central(tab):
    '''
    Recebe um tabuleiro e devolve a posição central
    obtem_posicao_central: tabuleiro --> inteiro
    '''

    m,n = obtem_dimensao(tab)

    return  (m // 2) * n + n // 2 + 1


def verifica_argumentos(tab,pos,jog,k):
    '''
    Faz a verificação dos argumentos, auxiliando as outras funções
    verifica_argumentos: tabuleiro X posicao X jogador X --> 
    '''

    return eh_tabuleiro(tab) and eh_posicao(pos) and \
        eh_posicao_valida(tab, pos) and type(jog) == int and \
        (jog == 1 or jog == -1) and type(k) == int and k > 0

#----------------------------------------------------------------------------#

#JOGAR
def jogar():
    '''
    Apresenta o menu inicial e permite a escolha das variáveis
    '''
    print()
    print()
    print()
    print()
    print()
    print('-'*155)
    print()
    print()

    jogar = 'x'
    while jogar != '':
        jogar = input('Bem vindo ao JOGO MNK. (prima enter para começar)')
    print()

    #linhas
    m = '-1'
    while type(m) != int or not 1 <= m <= 100:
        m = input('Introduza a quantidade de linhas: ')
        if m.isnumeric():
            m = int(m)
    print()

    #colunas
    n = '-1'
    while type(n) != int or not 1 <= n <= 100:
        n = input('Introduza a quantidade de colunas: ')
        if n.isnumeric():
            n = int(n)
    print()

    #sequência
    k = '-1'
    while type(k) != int or not 1 <= max(m,n):
        k = input('Introduza o tamanha da sequência de vitória: ')
        if k.isnumeric():
            k = int(k)
    print()

    #jogador
    jogador = '0'
    while jogador != 'x' and jogador != 'X' and jogador != 'o' and jogador != 'O':
        jogador = input('Escolha o jogador (X/O): ')
    if jogador == 'x' or jogador == 'X':
        jogador = 1
    else:
        jogador = -1
    print()

    #dificuldade
    dificuldade = 'x'
    while dificuldade != 'facil' and dificuldade != 'normal' and dificuldade != 'dificil':
        dificuldade = input('Escolha a dificuldade (facil/normal/dificil): ')

    print()

    #jogo
    jogo_mnk((m,n,k),jogador,dificuldade)

    print()
    print()
    print('-'*155)
    print()
    print()
    print()

jogar()