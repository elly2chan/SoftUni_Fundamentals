def decrypt_message(message):
    morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                      'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                      'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                      'Z': '--..'}

    message = message.upper().split(' | ')
    decrypted_message = ''

    for word in message:
        word = word.split()
        for char in word:
            if char in morse_alphabet.values():
                letter = morse_alphabet.get(char)
                print(letter)




result = decrypt_message(input())

