#Empty list to store values.
my_list = []

# Append values to the list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert a value at a specific index.
my_list.insert(1, 15)

# Extend the list with multiple values.
my_list.extend([50, 60, 70])

# Remove the last element from the list.
my_list.pop(-1)

# Sort the list in ascending order.
my_list.sort()



#Find and print the index of the value 30 in my_list.


for i in range(my_list):
    if my_list[i] == 30:
        print(i)
        
        


