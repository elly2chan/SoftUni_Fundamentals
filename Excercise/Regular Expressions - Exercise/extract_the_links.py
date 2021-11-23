import re

valid_urls = []

while True:
    sentence = input()

    if len(sentence) == 0:
        break

    pattern = r'(www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
    matches = re.finditer(pattern, sentence)

    for match in matches:
        valid_urls.append(match.group(0))

for url in valid_urls:
    print(url)