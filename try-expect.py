try:
    with open('text.txt', 'r') as my_file:
        content = my_file.read()
        print(content)

#execpt:
except FileNotFoundError as e:
    # print('File not Found')
    print(e)

print('Error Handle by Imran')
