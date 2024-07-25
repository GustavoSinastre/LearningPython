# Learning to work with dictionaries and data structures

# Creating two different lists
product_list = ["airpod", "ipad", "iphone", "macbook"]
price_list = [1000, 8000, 5000, 12000]

# Using dictionaries, we can join a key with a value
# product_dictionary = {"key":value, "key2":value2}
product_dictionary = {"airpod":1000, "ipad":8000,"iphone":5000,"macbook":12000}

# To find a value in a dictionary, we use the key to search the value
print(product_dictionary["iphone"])
print(product_dictionary)

# Treatment of values
product_dictionary["iphone"] = product_dictionary["iphone"] * 1.3
print(product_dictionary["iphone"])
print(product_dictionary)

# Size or quantity of list items
size_product_dictionary = len(product_dictionary)
print(size_product_dictionary)

# Removing an item
product_dictionary.pop("airpod")
print(product_dictionary)

# Adding and editing an item 
# if a key already exists, the code edits it, if not, it creates it
product_dictionary["airpod"] = 2000
print(product_dictionary)
product_dictionary["apple watch"] = 3000
print(product_dictionary)
product_dictionary["apple watch"] = 2800
print(product_dictionary)

# The code always use the key to find a value
# Example using and if
if "iphone" in product_dictionary:
    print("Produto existe no dicionário")
else:
    print("Produto não existe no dicionário")

# To search the value in the dictionary, we need to transform the condition if
iphone_value = product_dictionary["iphone"]
print(iphone_value)

if iphone_value in product_dictionary.values():
    print("Valor está dentro do dicionário atrelado a algum produto")
else:
    print("Valor não encontrado no dicionário")



# To practice the content, we will create a small registration system
new_product_name = input("Digite o nome do produto: ").lower()
print(new_product_name)
new_product_price = float(input("Digite o preço do produto: "))
print(new_product_price)

# Checking if the product exists in the dicionary
if new_product_name in product_dictionary:
    print("O produto já existe na lista, atualizando o preço")
    product_dictionary[new_product_name] = new_product_price
    print(product_dictionary[new_product_name])
else:
    print("O produto não existe, cadastrando agora")
    product_dictionary[new_product_name] = new_product_price
    print(product_dictionary[new_product_name])
print(product_dictionary)

# Updating the price of all the products in 10%
increment = 1.10
for product in product_dictionary:
    # Updating the price in 10%
    updated_price = product_dictionary[product] * increment
    product_dictionary[product] = round(updated_price,2)
print("Preço atualizado em 10%")
print(product_dictionary)

