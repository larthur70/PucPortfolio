import copy

def calcular_troco(valor_produto, valor_pago, qtd_atualizados):
    troco = (valor_pago - valor_produto) * 100
    troco = round(troco)
    dinheiro = {
        'nota de 200': [20000,qtd_atualizados[0],0],
        'nota de 100': [10000,qtd_atualizados[1],0],
        'nota de 50': [5000,qtd_atualizados[2],0],
        'nota de 20': [2000,qtd_atualizados[3],0],
        'nota de 10': [1000,qtd_atualizados[4],0],
        'nota de 5': [500,qtd_atualizados[5],0],
        'nota de 2': [200,qtd_atualizados[6],0],
        'moeda de 1 real': [100,qtd_atualizados[7],0], 
        'moeda de 50 cent': [50,qtd_atualizados[8],0], 
        'moeda de 25 cent': [25,qtd_atualizados[9],0], 
        'moeda de 10 cent': [10,qtd_atualizados[10],0],
        'moeda de 5 cent': [5,qtd_atualizados[11],0],
        'moeda de 1 centavo': [1,qtd_atualizados[12],0]
    }
    copia_quantidade_notas = copy.deepcopy(qtd_atualizados)
    troco_din = 0
    troco_str = ''
    while troco_din < troco:
        i = 0
        for chave, valor in dinheiro.items():
            if valor[0] > troco:
                i +=1
                continue
            else:
                troco_din += valor[0]
                if troco_din > troco:
                    troco_din -= valor[0]
                    i += 1
                    continue
                else:
                    if valor[1] <= 0:
                        qtd_atualizados = copia_quantidade_notas
                        return 1,'não tem troco suficiente no caixa',qtd_atualizados
                    else:
                        valor[2] += 1
                        qtd_atualizados[i] -= 1
                        valor[1] = qtd_atualizados[i]
                        break

    for chave,valor in dinheiro.items():
        if valor[2] != 0:
            troco_str += f'{valor[2]}x {chave} \n'
    return 0,troco_din / 100, troco_str, troco,qtd_atualizados


def printar_maquina(matriz):
    for linha in matriz:
        for item in linha:
            print(item, end='     ')
        print('\n')


def criar_produto(id_produto):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input('Digite o preço do produto: '))
    estoque_produto = int(input('Digite o estoque do produto: '))
    maquina.append([id_produto, nome_produto, preco_produto, estoque_produto])


def editar_produto(id_editar):
    nome_produto = input("Digite o novo nome do produto: ")
    preco_produto = float(input('Digite o novo preço do produto: '))
    estoque_produto = int(input('Digite o novo estoque do produto: '))
    maquina[id_editar][1] = nome_produto
    maquina[id_editar][2] = preco_produto
    maquina[id_editar][3] = estoque_produto

qtd_atualizados = [1,2,5,5,5,7,7,7,10,10,10,10,10]

maquina = [
    ['id', 'produto', 'preço', 'estoque'],
    [1, 'coca-cola', 3.75, 2],
    [2, 'pepsi', 3.67, 5],
    [3, 'Monster', 9.96, 1],
    [4, 'Café', 1.25, 100],
    [5, 'RedBull', 13.99, 2]
]

id_ultimo_produto = 5

while True:
    printar_maquina(maquina)
    codigo = int(input("Digite o código do seu produto(0 para sair): "))
    if codigo == 0:
        break
    elif codigo == 777:
        while True:
            print('você está no modo adm')
            opcao = input("[C]adastrar [E]ditar [R]emover produto ou [S]air modo adm: ")
            opcao = opcao.upper()
            if opcao == 'C':
                id_ultimo_produto += 1
                criar_produto(id_ultimo_produto)
                print('produto criado!')
            elif opcao == 'E':
                produto_editar = int(input("Digite o id do produto que você deseja editar: "))
                editar_produto(produto_editar)
                print('produto editado!')
            elif opcao == 'R':
                produto_remover = int(input('Digite o id do produto que voce quer remover'))
                del maquina[produto_remover]
                id_ultimo_produto -= 1
                for i, linha in enumerate(maquina):
                    if i >= produto_remover:
                        maquina[i][0] -= 1
                print('produto removido!')
            else:
                break

    try:
        if codigo == maquina[codigo][0]:
            if maquina[codigo][3] > 0:
                print(f'O valor da(o) {maquina[codigo][1]} é R${maquina[codigo][2]}')
                valor_pago = float(input('inserir valor: '))
                while valor_pago < maquina[codigo][2]:
                    valor_pago = float(input('Valor inválido, digite outro por favor: '))
                x = calcular_troco(maquina[codigo][2], valor_pago,qtd_atualizados)
                if x[0] == 0:

                    qtd_atualizados = x[4]
                    print(f'Seu troco deu {x[1]}')
                    print(x[2])
                    print(f'obrigado por comprar =)')
                    maquina[codigo][3] -= 1
                else:
                    qtd_atualizados = x[2]
                    print(x[1])
                #print(qtd_atualizados)
            else:
                print("sem estoque")
    except IndexError:
        print('não tem esse produto')