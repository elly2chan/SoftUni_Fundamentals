file_path = input().split('\\')
file, extension = file_path[-1].split('.')

print(f'File name: {file}')
print(f'File extension: {extension}')