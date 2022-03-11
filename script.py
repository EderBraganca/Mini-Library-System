# -*- coding: utf-8 -*-
EstoqueLivros = []
saldo = 0

#funções
def cadastrarLivro(Titulo, ISBN, Valor, QuantidadeEstoque):
    if QuantidadeEstoque >= 1:
        for livros in EstoqueLivros:
            if livros['ISBN'] == ISBN:
                livros['QuantidadeEstoque'] += QuantidadeEstoque
                print("+", QuantidadeEstoque, "adicionados com sucesso!")
                return
        livros = {}
        livros['Titulo'] = Titulo
        livros['ISBN'] = ISBN
        livros['Valor'] = Valor
        livros['QuantidadeEstoque'] = QuantidadeEstoque
        if QuantidadeEstoque > 1:
            print("Livros adicionados com sucesso!")
        else: 
            print("Livro adicionado com sucesso!")
        
        EstoqueLivros.append(livros)
    else:
        print("Digite uma quantidade válida!")

def constultarEstoqueTitulo(Titulo):
    for livros in EstoqueLivros:
        if livros['Titulo'] == Titulo:
            print("ISBN: ", livros['ISBN'])
            print("Valor: ", livros['Valor'])
            print("Quantidade em estoque: ", livros['QuantidadeEstoque'])
            return

        else:
            print("Este titulo não está cadastrado!")
            return

def consultarEstoqueISBN(ISBN):    
    for livros in EstoqueLivros:
        if livros['ISBN'] == ISBN:
            print("Título: ", livros['Titulo'])
            print("Valor: ", livros['Valor'])
            print("Quantidade em estoque: ", livros['QuantidadeEstoque'])
            return

        else:
            print("Este ISBN não está cadastrado!")
            return


def venderLivro(ISBN, QuantidadeVenda):
    global saldo 
    for livros in EstoqueLivros:
        if livros['ISBN'] == ISBN:
            if livros['QuantidadeEstoque'] - QuantidadeVenda >= 0:
                livros['QuantidadeEstoque'] -= QuantidadeVenda
                saldo += QuantidadeVenda * livros['Valor']
                if QuantidadeVenda > 1:
                    print("Livros vendidos com sucesso!")
                else:
                    print("livro vendido com sucesso!")
                return
            else: 
                print("Estoque indisponível!")
                return
        else:
            print("Digite um ISBN válido!")
            return
def consultarSaldo():
    print(saldo)

def menu():
    print("Escolha uma opção\n [1] para Cadastrar livro \n [2] para Consultar estoque(Busca por Título)\n [3] para Consultar estoque(Busca por ISBN) \n [4] para Vender um livro \n [5] para Consultar saldo da loja \n [6] para Salvar dados \n [9] para Sair")

    opcao = int(input())

    #teclas menu
    if opcao == 1:
        Titulo = input("Digite o Titulo do livro: ")
        ISBN = int(input("Digite o ISBN do livro: "))
        Valor = float(input("Digite o Valor do livro: "))
        QuantidadeEstoque = int(input("Digite a quantidade de livros adicionados ao estoque: "))
        cadastrarLivro(Titulo, ISBN, Valor, QuantidadeEstoque)
        menu()

    elif opcao == 2:
        Titulo = input("Digite o título do livro que deseja buscar: ")
        constultarEstoqueTitulo(Titulo)
        menu()

    elif opcao == 3:
        ISBN = int(input("Digite o ISBN do livro que deseja buscar: "))
        consultarEstoqueISBN(ISBN)
        menu()

    elif opcao == 4:
        ISBN = int(input("Digite o ISBN do livro que deseja vender: "))
        QuantidadeVenda = int(input("Digite a quantidade de livros que deseja vender: "))
        venderLivro(ISBN, QuantidadeVenda)
        menu()

    elif opcao == 5:
        consultarSaldo()
        menu()

    elif opcao == 6:
        print("salvarDados()") #só falta esse zezim gasolina
        menu()

    elif opcao == 9:
        print("Obrigado por utilizar nosso programa, até mais!")

    else:
        print("Digite um valor válido")
        menu()

menu()