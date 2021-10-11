def find_palindromes(integers):
    is_palindrome = []
    for integer in integers:
        if integer == integer[::-1]:
            is_palindrome.append(True)
        else:
            is_palindrome.append(False)
    return is_palindrome


list_of_numbers = input().split(', ')
result = find_palindromes(list_of_numbers)

for value in result:
    print(value)