import os

def delete_file_if_possible(path):
    if os.path.exists(path):
        print("Path exists.")
        if os.access(path, os.W_OK):
            print("File is accessible.")
            os.remove(path)
            print(f"Файл '{path}' успешно удален.")
        else:
            print("Нет доступа к файлу.")
    else:
        print(f"Файл по указанному пути не существует: {path}")

path_to_file = input("Введите путь к файлу для удаления: ")
delete_file_if_possible(path_to_file)