words = input().split(' ')
palindrome = input()


def check_if_word_is_palindrome(words_list):
    palindromes = []
    for word in words_list:
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


def count_palindrome_occurrences(checked):
    counter = check_if_word_is_palindrome(words).count(checked)

    return counter


palindromes_list = check_if_word_is_palindrome(words)
palindrome_occurrences_count = count_palindrome_occurrences(palindrome)
print(palindromes_list)
print(f'Found palindrome {palindrome_occurrences_count} times')
