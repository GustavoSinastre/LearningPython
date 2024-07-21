# First we need to fix that a input is stored in a string variable
# When we want that the input be a number, we need to convert

# Inputs
#email = input("Escreva o seu e-mail: ")
#nome_completo = input("Escreva o seu nome completo: ")

# Importing the statistics library
import statistics

# Using a randomly sell list
# In Python, when we declare a list, the index starts with the first item of the list
sell_list = [50,20,30,90,150,80]

# Let's sum the amount of sales
total_sell_list = sum(sell_list)
print("O total em vendas foi",total_sell_list)

# Average using statistics library
average_sell_list = statistics.mean(sell_list)
print("A média em vendas foi",average_sell_list)

# Size of the list
sell_list_size = len(sell_list)
print("A quantidade de vendas foi",sell_list_size)

# Higher and lower value of the list
higher_value_sl = max(sell_list)
print("O maior venda foi de",higher_value_sl)
lower_value_sl = min(sell_list)
print("A menor venda foi de",lower_value_sl)

# Now, we have an input with an item of the list, and we need to verify if this item is on the list
product_list = ["iphone", "celular", "carregador", "garfo"]

#Adding a new product by inputs
product_list.append(input("Qual produto você quer adicionar? ").lower())
print(product_list)

item_to_remove = input("Qual produto você quer remover da lista? ").lower()
if item_to_remove in product_list:
    product_list.remove(item_to_remove)
    removed_item = "Ok, produto removido da lista"
else:
    removed_item = "O produto não está na lista"

print(removed_item)
print("A lista atualizada é:", product_list)

# Applying prices to products
product_price = [2000, 1000, 200, 10]
print("O preço dos produtos são:", product_price)

# Sorting the list of products
product_list.sort()
print("A lista de produtos em ordem alfabética é:", product_list)



# Remember that upper and lower letters is readed of differents forms in Python
# In this case, let's transform the input in lower letters
#searched_product = input("Digite o nome do produto: ").lower()
#print(searched_product)

#found_product = "Ok, produto na lista" if searched_product in product_list else "Não ok, você é um animal"
#print(found_product)

