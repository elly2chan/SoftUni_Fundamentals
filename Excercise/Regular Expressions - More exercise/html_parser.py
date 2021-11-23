import re

data = input()

title_pattern = r'<title>([^<>]*)<\/title>'
title = ''.join(re.findall(title_pattern, data))

body_pattern = r'<body>.*<\/body>'
body = ''.join(re.findall(body_pattern, data))

valid_body_content_pattern = r'>([^><]*)<'
valid_body = ''.join(re.findall(valid_body_content_pattern, body)).replace('\\n', '')

print(f'Title: {title}')
print(f'Content: {valid_body}')