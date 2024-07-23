# For i in range, actions

# Lets calculate the commission for each employee
revenue_list = [1290, 1900, 890, 1341, 870, 700, 2000]
commission_range = 0.1
target_commission = 1200

for employee_revenue in revenue_list:
    
    if employee_revenue >= target_commission:
        comission = employee_revenue * commission_range
        print(comission)
    else:
        comission = 0
        print(comission)