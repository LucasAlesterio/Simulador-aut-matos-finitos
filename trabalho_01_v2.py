# Nome: Lucas Alesterio Marques Vieira
# Matricula: 11621ECP016

# Inicialização das variaveis
nEstados = 0
nSimbolos = 0
simbolos = []
nAceitacao = 0
aceitacao = []
nTransicoes = 0
transicoes = []
nCadeias = 0
cadeias = []

# Função para coletar as entradas


def entradas():
    # Declação das variaveis globais
    global nEstados, nSimbolos, simbolos, nAceitacao, aceitacao
    global nTransicoes, transicoes, nCadeias, cadeias
    # Capturando numero de estados e transformando em inteiro
    nEstados = int(input())
    # Capturando numero de simbolos e lista de simbolos
    auxInput = input()
    auxInput = auxInput.split(' ')
    nSimbolos = int(auxInput[0])
    simbolos = auxInput[1:]
    # Capturando numero de estados de aceitação e lista de aceitação
    auxInput = input()
    auxInput = auxInput.split(' ')
    nAceitacao = int(auxInput[0])
    aceitacao = list(map(int, auxInput[1:]))
    # Capturando numero de transições
    nTransicoes = int(input())
    # Capturando lista de transições em loop de
    # acordo com o numero digitado anteriormente
    transicoes = []
    while len(transicoes) < nTransicoes:
        transicoes.append(input().split(' '))
    # Capturando numero de cadeias
    nCadeias = int(input())
    # Capturando lista de cadeias em loop de
    # acordo com o numero digitado anteriormente
    cadeias = []
    while len(cadeias) < nCadeias:
        cadeias.append(list(input()))

# Função para percorrer todas as cadeias digitadas
# e faz a busca em cada uma com o estado inicial 0
# e cadeia digitada printando o resultado


def varredura():
    for cadeia in cadeias:
        print(busca(0, cadeia))

# Função de busca que tem como entrada o estado inicial
# e a cadeia a ser percorrida


def busca(estadoAtual, cadeia):
    # Testando caso a cadeia esteja vazia se o estado atual
    # esta na lista de aceitação e retorna o resultado
    if(not(cadeia)):
        if(estadoAtual in aceitacao):
            return('aceita')
        else:
            return('rejeita')
    # Teste caso a entrada seja vazia e mantendo a busca
    # no mesmo estado e continuando na cadeia
    elif(cadeia[0] == '-'):
        return(busca(estadoAtual, cadeia[1:]))

    # Verificando todas as possiveis transições a partir
    # do estado inicial para o primeiro simbolo da cadeia
    # e iniciando uma nova busca"
    for transicao in transicoes:
        if(int(transicao[0]) == estadoAtual and transicao[1] == cadeia[0]):
            if(busca(int(transicao[2]), cadeia[1:]) == 'aceita'):
                return('aceita')

    return('rejeita')


# Chamando as funções de entradas e varredura para iniciar o programa
entradas()
varredura()
