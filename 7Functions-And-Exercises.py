# Adding resources
import pandas as pd
import os
from datetime import datetime

# Lets learn how to use functions in python
# Variables created in a function only exist in it

# In this code, we will calculate different theoretical tax for a product dictionary
# Income tax = IT
# Tax on assets and services = TAS 
# Contribution tax = CT

# Definition of the first variables
aliquot_IT_range_1 = 0.07 # Prices up to 1000
limit_aliquot_IT_range_1 = 1000
aliquot_IT_range_2 = 0.15 # Prices from 1001 to 2000
limit_aliquot_IT_range_2 = 2000
aliquot_IT_range_3 = 0.2 # Prices above 2000
aliquot_TAS = 0.05 # Generic
aliquot_CT = 0.02 # Generic

# Product Price
product_dictionary = {"airpod":1000, "ipad":1900,"iphone":2900,"macbook":12000}
# Product Cost
product_cost = {"airpod":300, "ipad":820,"iphone":1000,"macbook":5000}
# Creating a dictionary to save each tax for each item
tax_IT_dictionary = {}
tax_TAS_dictionary = {}
tax_CT_dictionary = {}
total_tax_dictionary = {}
net_profit_dictionary = {}
net_profit_percent_dictionary = {}

# Definition of the funcion to calculate the tax
def calculate_tax(price):
    if price <= limit_aliquot_IT_range_1:
        tax_IT = price * aliquot_IT_range_1
    elif limit_aliquot_IT_range_1 < price <= limit_aliquot_IT_range_2:
        tax_IT = price * aliquot_IT_range_2
    else:
        tax_IT = price * aliquot_IT_range_3        
    
    tax_TAS = price * aliquot_TAS
    tax_CT = price * aliquot_CT
    total_tax = tax_IT + tax_TAS + tax_CT

    return tax_IT, tax_TAS, tax_CT,total_tax

# Creating a function with a loop that fills the tax dictionary
def fills_tax_dictionaries(product_dictionary, product_cost):
    for product,price in product_dictionary.items():
        cost = product_cost.get(product, 0)
        tax_IT, tax_TAS, tax_CT,total_tax = calculate_tax(price)
        net_profit = price - cost - total_tax
        net_porcent_profit = round((net_profit/price), 4) if cost > 0 else 0
        
        # Fill the dictionaries 
        tax_IT_dictionary[product] = tax_IT
        tax_TAS_dictionary[product] = tax_TAS
        tax_CT_dictionary[product] = tax_CT
        total_tax_dictionary[product] = total_tax
        net_profit_dictionary[product] = net_profit
        net_profit_percent_dictionary[product] = net_porcent_profit

# Calling the function to fill the tax dictionaries
fills_tax_dictionaries(product_dictionary,product_cost)

# Printing the results
print("Product Prices:", product_dictionary)
print("Product Costs:", product_cost)
print("Income Tax Dictionary:", tax_IT_dictionary)
print("TAS Tax Dictionary:", tax_TAS_dictionary)
print("CT Tax Dictionary:", tax_CT_dictionary)
print("Total Tax Dictionary:", total_tax_dictionary)
print("Net Profit:", net_profit_dictionary)
print("% Net Profit:", net_profit_percent_dictionary)

# Export data to Excel
# Creatind a DataFrame using pandas
data_frame = pd.DataFrame({
    'Product': product_dictionary.keys(),
    'Price': [price for price in product_dictionary.values()],
    'Cost': [product_cost.get(product, 0) for product in product_dictionary],
    'IT Tax': [tax_IT_dictionary.get(product, 0) for product in product_dictionary],
    'TAS Tax': [tax_TAS_dictionary.get(product, 0) for product in product_dictionary],
    'CT Tax': [tax_CT_dictionary.get(product, 0) for product in product_dictionary],
    'Total Tax': [total_tax_dictionary.get(product, 0) for product in product_dictionary],
    'Net Profit': [net_profit_dictionary.get(product, 0) for product in product_dictionary],
    '% Net Profit': [net_profit_percent_dictionary.get(product, 0) for product in product_dictionary]
})

# Exportation data
exportation_path = r'C:\Users\luisg\OneDrive\Project Dev\Exports\Python\7Functions-And-Exercises'
file_name = 'Precificação Produtos.xlsx'
full_path = os.path.join(exportation_path,file_name)

# Backup and file handling
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_file_name = f'Precificação Produtos {timestamp}.xlsx'
backup_file_path = os.path.join(exportation_path, backup_file_name)

# Backup and file handling
if os.path.exists(full_path):
    # Get the modification time of the existing file
    modification_time = os.path.getmtime(full_path)
    # Convert modification time to a readable format
    timestamp = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d_%H-%M-%S')
    # Create a backup file name with the timestamp
    backup_file_name = f'Precificação Produtos {timestamp}.xlsx'
    backup_file_path = os.path.join(exportation_path, backup_file_name)
    # Rename (move) the existing file to backup
    os.rename(full_path, backup_file_path)
    print(f"Backup saved as '{backup_file_path}'")

# Ensure the exportation path exists
if not os.path.exists(exportation_path):
    os.makedirs(exportation_path)

# Write the combined DataFrame to a single Excel sheet
data_frame.to_excel(full_path, sheet_name='Analítico', index=False)