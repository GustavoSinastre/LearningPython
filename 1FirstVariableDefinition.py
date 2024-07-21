#Variable Definition
revenue = 1000 #tipo int, número inteiro
costs = 500.90 #tipo float, número decimal
new_sales = 1000
new_revenue = revenue + new_sales
tax = new_revenue * 0.1
profit  = new_revenue - costs - tax
profit_margin = round(profit / new_revenue,2)

#Print information
print("The revenue was",new_revenue)
print("The costs was",costs)
print("The profit was",profit)
print("The profit margin was",profit_margin)

#Working with strings
print(f"The revenue was {revenue}, the cost was {costs}, and the final margin was {profit_margin}")

# Let's formate the revenue, costs and margin with the respective formatting
# Using the code above, let's print the same information, but with a new formatting
print(f"The revenue was R${revenue:.2f}, the cost was R${costs:.2f}, and the final margin was {profit_margin:.1%}")
