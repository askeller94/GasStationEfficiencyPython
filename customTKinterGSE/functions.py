def calculate_cost(distance1, distance2, cost1, cost2, mpg, gallons):
    # Calculate the cost to drive to each gas station
    cost_to_drive1 = round(distance1 / mpg * cost1, 2)
    cost_to_drive2 = round(distance2 / mpg * cost2, 2)
    
    # Calculate the total cost of gas for each gas station
    total_cost1 = round(cost1 * gallons, 2) + cost_to_drive1
    total_cost2 = round(cost2 * gallons, 2) + cost_to_drive2
    
    # Compare total cost and return the cheaper option
    if total_cost1 < total_cost2:
        return "Gas station 1 is cheaper with a total cost of $" + str(total_cost1) + " and the cost to drive there was $" + str(cost_to_drive1)
    else:
        return "Gas station 2 is cheaper with a total cost of $" + str(total_cost2) + " and the cost to drive there was $" + str(cost_to_drive2)
