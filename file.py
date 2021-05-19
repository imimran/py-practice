# my_file = open('test.txt', 'r')
# content = my_file.read()
# print(content)
# my_file.close()

with open('test.txt', 'r') as my_file:
    content = my_file.read()
    print(content)