def get_total_cost_of_meal():
    # original meal price
    print("Meal Cost :")
    meal_cost = float(input())
    # tip percentage
    print("Tip percent :")
    tip_percent = int(input())
    # tax percentage
    print("Tax percent :")
    tax_percent = int(input())

    # Write your calculation code here
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tax + tip))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " rupes.")