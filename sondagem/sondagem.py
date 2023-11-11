def diagonal(matriz):

    for linha in matriz:                                        #percorre as linhas da matriz
        if(len(matriz) != len(linha)):                          #caso o numero de linhas seja diferente do numero de colunas daquela linha retorna False
            return False
        
    for linha in range(len(matriz)):                            #percorre coordenadas das linhas da matriz
        for coluna in range(len(matriz[linha])):                #percorre as colunas da linha do 'for' anterior chamados de celula
            if(linha != coluna and matriz[linha][coluna] != 0): #verifica se no par ordenado (linha, coluna) linha != coluna e se o item da matriz[linha][coluna] é diferente de 0
                return False                                    #caso qualquer elemento fora da diagonal principal seja diferente de 0, retorna False encerrando a função
            
    return True #caso percorra toda a matriz sem retornar False retorna True

def esparsa(matriz):
    elementos = 0                                   #contagem do total de elementos da matriz
    elementos_igual_a_zero = 0                      #contagem do total de elementos da matriz iguais a 0
    for linha in matriz:                            #percorre as linhas da matriz
        elementos += len(linha)                     #soma o numero de elementos daquela linha
        for celula in linha:                        #percorre as celulas daquela linha
            if(celula == 0):                        #caso o valor da celula seja igual a 0 incrementa o contador de elementos iguais a zero
                elementos_igual_a_zero += 1
    
    return elementos_igual_a_zero > elementos/2     #retorna True se numero de elementos iguais a 0 forem maioria, False se forem minoria

def giro(matriz):
    matriz_girada = []
    
    for linha in matriz:                                        #percorre as linhas da matriz
        if(len(matriz) != len(linha)):                          #caso o numero de linhas seja diferente do numero de colunas daquela linha retorna False
            return False
        
        #a roda de coordenadas a ser seguida é essa: 
        #[2][0] -> [1][0] -> [0][0] -> [2][1] -> [1][1] -> [0][1] -> [2][2] -> [1][2] -> [0][2]
        #perceba como a coluna varia menos que a linha, então o primeiro 'for' loop vai ser das colunas

    for coluna in range(len(matriz)):
        linhatmp = []                                           #cria um objeto lista vazio para organizar os valores de cada linha da matriz final
        for linha in range(len(matriz[coluna])-1, -1, -1):      #'for' loop indo de 2 a 0, com step de -1 seguindo a rota definida anteriormente
            linhatmp.append(matriz[linha][coluna])              #adiciona o valor das coordenadas (linha, coluna) na lista temporaria
        matriz_girada.append(linhatmp)                             #adiciona a lista temporaria na matriz
    return matriz_girada                                        #retorna a matriz ja girada
    



if __name__ == "__main__":
    diag = [[1,0,0],
            [0,5,0],
            [0,0,9]]
    for linha in diag:
        print(linha)
    
    print("\nMATRIZ DIAGONAL?: " + str(diagonal(diag)))

    print("MATRIZ ESPARSA?: " + str(esparsa(diag)))
    
    print("MATRIZ GIRADA 90% SENTIDO HORARIO:\n")
    for linha in giro(diag):
        print(linha)
