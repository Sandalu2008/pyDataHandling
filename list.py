#Create the list named temperatured
temperatures = [25.5, 28.1, 22.9, 30.2, 27.8, 24.3, 29.5]

#Add 31.0 to the end of the temperatures list
temperatures.append(31.0)

#Remove the third element (index 2) from the list 
temp=temperatures.pop(2)
print(temp)

#Find the maximum and minimu temperatue in the list
max_temperature = max(temperatures)
min_temperature = min(temperatures)

print(f"Maximum temperature is: {max_temperature}")
print(f"Minimum temeperature is: {min_temperature}")

# Calculate the average temperature
average_temperature = sum(temperatures) / len(temperatures)

#Print the modified list, the maximum, minimum and the average temperatue
print(f"Modified temperatures list : {temperatures}")
print(f"Maximum teperature : {max_temperature}")
print(f"Minimu Temeperature: {min_temperature}")
print(f"Average temperature: {average_temperature}")

