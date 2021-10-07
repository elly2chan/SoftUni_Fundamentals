# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

input_string = input()
input_counter = int(input())

result = lambda string, counter: string * counter

print(result(input_string, input_counter))