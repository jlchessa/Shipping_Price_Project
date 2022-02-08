from decimal import *

weight = float(input("Input package weight: "))

#Ground Shipping

if weight <= 2:
    cost_ground = weight * 1.50 + 20
elif weight <= 6:
    cost_ground = weight * 3 + 20
elif weight <= 10:
    cost_ground = weight * 4 + 20
else:
    cost_ground = weight * 4.75 + 20

print("Ground Shipping Price: $", cost_ground)

premium_ground_shipping = 125.00

print("Ground Shipping Premium $", premium_ground_shipping)

#Drone Shipping

if weight <= 2:
    drone_cost = weight * 4.50
elif weight <= 6:
    drone_cost = weight * 9
elif weight <= 10:
    drone_cost = weight * 12
else:
    drone_cost = weight * 14.25

print("Drone Shipping Cost: $", drone_cost)
