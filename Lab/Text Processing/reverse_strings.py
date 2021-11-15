while True:
    text = input()

    if text == 'end':
        break

    reversed_text = ''

    for ch in reversed(text):
        reversed_text += ch


    print(f'{text} = {reversed_text}')