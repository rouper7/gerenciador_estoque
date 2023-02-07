estoque=[]
class Produto :
    def __init__(self,nome,preco,qtd_estoque):
        self.nome=nome
        self.preco=preco
        self.qtd_estoque=qtd_estoque

add_estoque=lambda produto:estoque.append(produto)
remover_estoque=lambda produto:estoque.remove(produto)

def atualizar_preco(produto,preco):
    if produto in estoque:
        produto.preco=preco
    

def preco_total():
    total=0
    for produto in estoque:
        total+=produto.preco*produto.qtd_estoque
    print(total)

def listar():
    for produto in estoque:
        print(f'{produto.nome}| preco:${produto.preco}| quantidade:{produto.qtd_estoque}')
    

#---------------exemplos de uso----------------------------------
p1=Produto('iphone 13',5000,1)
p2=Produto('galaxy s23',6000,2)

add_estoque(p1) #adiciona produto no estoque        
add_estoque(p2)
atualizar_preco(p2,50) #atualiza o preco 
listar()        #lista os produtos do estoque
preco_total()   #informa o preço total

#removendo um produto
remover_estoque(p1) 
listar()
#made by rouper7/phoenix
