#Before we start the structure, lets write the most useds comparations tests
# > bigger
# < lower
# >= bigger or equal
# <= lower or equal
# == equal
# !# different

import locale

# Configurate the locale for R$ format
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Variables
cross_value = 1290
cross_target = 1129
increase_cross_target = 1300
commission_range_1 = 0.1
commission_range_2 = 0.15
commission = 0
reached_target = ""

#Starting the structure
if cross_value >= increase_cross_target:
    commission = cross_value * commission_range_2
    reached_target = "A meta de incremento foi atingida" 
else:
    if cross_value >= cross_target:
        commission = cross_value * commission_range_1
        reached_target = "Somente a meta principal foi atingida" 
    else:
        commission = 0
        reached_target = "Nenhuma meta foi atingida" 

formatted_commission = locale.currency(commission,grouping=True)

print("Comissão atual:",formatted_commission)
print(reached_target)

#Lets use the list of the thirdy code
product_list = ["iphone", "celular", "carregador", "garfo"]
item_to_add = input("Escreva o produto a ser adicionado na lista: ").lower()

if item_to_add in product_list:
    print("O produto já está na lista")
else:
    product_list.append(item_to_add)
    print("Produto adicionado")
    print(product_list)
