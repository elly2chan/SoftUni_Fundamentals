tail = input()
body = input()
head = input()

elements = [tail, body, head]

elements[0], elements[2] = elements[2], elements[0]

print(elements)