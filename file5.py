
user_input = input("")
list1 = [item for item in user_input.split()]


path = input("Введите путь к файлу для записи: ")

def write_in_file(path, items):
    
    with open(path, 'w') as file:
        for line in items:
            file.write('%s\n' % line)
    


write_in_file(path, list1)
