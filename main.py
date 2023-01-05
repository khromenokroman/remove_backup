#! /usr/bin/python3
import os

PATH_PG = '/home/roma/Coding/remove_file/binari_test_folder' # Путь к вашей папке с бэкапами постгрес
PATH_OS = '/home/roma/Coding/remove_file/' # Путь к вашей папке с бэкапами ос
REMOVE = 5 #Сколько последних копий оставить

# Получим список имен всего содержимого папки
# и превратим их в абсолютные пути
dir_list = [os.path.join(PATH_PG, x) for x in os.listdir(PATH_PG)]


if dir_list:
    # Создадим список из путей к файлам и дат их создания.
    date_list = [[x, os.path.getctime(x)] for x in dir_list]

    # Отсортируем список по дате создания
    sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

    # Выведем количество элементов в списке
    print(f'Всего файлов и папок: {len(sort_date_list)}')

    count = 1

    for item in sort_date_list:
        if count <= REMOVE:
            count +=1
            continue
        else:
            try:
                print(f'Удаляю {item[0]}')
                os.remove(item[0])
            except:
                print(f'Нашел каталог {item[0]} пропускаю')
                continue   
