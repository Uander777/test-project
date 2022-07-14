#Импортируем библиотеки
import os 
import sys 
import time
import shutil
#стартовый экран приветствия
print('Добро пожаловать в "Файловый менеджер !" ')
#пустой print для пробела
print()
#выводим список доступных команд
print('Список доступных команд:')
print('/create - Создать новый файл')
print('/delete - Удалить файл')
print('/rename - Переименовать файл')
print('/change -  1) /write Записать данные в файл')
print('/exit -  Выход')
#зацикливаем через while чтобы user мог повторно вводить команду после выполнения операции
while True:
    file_list=os.listdir("C:\\Users\\Home\Desktop\\File Manager Project")
    print(file_list.count)
    #Просим user ввести команду
    command = input('Введите команду: ')
    #Создание файлов
    if command == '/create':
        print('Внимание! Допустимо создание текстовых файлов: txt, docx, rtf!')
        command_create = input('Укажите расширение файла:   ')
        if command_create == 'txt':
            user_file = open("Testfile.txt", "w+")
            user_file.write('Ваш файл')
            user_file.close()
            for (p, n, fn) in os.walk('C:\Users\Home\Desktop\File Manager Project'):
                print(fn)
            print('Файл создан !')
            for file_item in file_list:
                print(file_item)
            command = input('Введите команду: ')
        if command_create == 'docx':
            user_file = open("Testfile.docx", "w+")
            user_file.write('Ваш файл')
            user_file.close()
            print('Файл создан !')
            command = input('Введите команду: ')
        if command_create == 'rtf':
            user_file = open("Testfile.rtf", "w+")
            user_file.write('Ваш файл')
            user_file.close()
            print('Файл создан !')
            command = input('Введите команду: ')

    #Переименование файлов        
    if command == '/rename':
        oldname = input('Старое название файла:') 
        newname = input('Новое название файла:') 
        os.rename(oldname, newname) 
        print('Файл переименован !')
        command = input('Введите команду:   ')
    
    #Запись в файл
    if command == '/write':
        filename = input("Введите название файла: ")
        with open(filename, "w") as f:
            f.write(input('Что записать?: '))
            print('Изменения записаны !')
        command = input('Введите команду:   ')
    #Удаление данных из файла
    if command == '/erase':
        file_e = open('Testfile.txt', 'w')
        file_e.truncate()
        file_e.close()
  
    
    #удаление созданных файлов
    if command == '/delete':
        myfile = input("Введите имя файла: ")
        try:
            os.remove(myfile)
            print('Файл удален !')
        except OSError as e:  
            print ("Error: %s - %s." % (e.filename, e.strerror))
    
    #выход из менеджера
    if command == '/exit':
        print('Всего доброго !')
        exit()
            
            
            
    
