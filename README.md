# gerenciador_estoque
A Python-based stock manager using functions and classes
How to Use:

1.Product Creation: To create a product object, you need to call the Produto class and pass three arguments to the init method: product name, price and quantity in stock.
example: product = Produto("Product 1", 10.00, 20)

2.Adding Product to Stock: To add a product to the stock, you need to call the add_estoque function and pass the product object as an argument.
example: add_estoque(product)

3.Removing Product from Stock: To remove a product from the stock, you need to call the remover_estoque function and pass the product object as an argument.
example: remover_estoque(product)

4.Updating Product Price: To update the price of a product, you need to call the atualizar_preco function and pass the product object and the new price as arguments.
example: atualizar_preco(product1, 4.0)

5.Total Price Calculation: To calculate the total price of the products in stock, you need to call the preco_total function. The result will be displayed on the screen.
example: preco_total()

6.Product Listing: To list all the products in stock, you need to call the listar function. The listing will include the product name, price and quantity in stock.
example: listar()
