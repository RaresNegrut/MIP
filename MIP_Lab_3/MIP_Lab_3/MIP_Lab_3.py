import math

# Read the target power from the console input
target_power = int(input("Enter the target power: "))


years = math.ceil(math.log2(target_power ) * 1.5)

# Print the number of years it took to reach the target power
print(f"It will take {years} years to reach a power of {target_power}.")