#Необходимые переменные
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
step = 0
len_list = len(my_list)-1

while my_list[step] >= 0 and step < len_list: #Главное условие работы цикла

    print(my_list[step]) #Вывод элемента из списка my_list с индексом step
    step += 1 #Переход к следующему элементу списка

    if my_list[step] == 0: #Если в списке встречается 0
        step += 1 #программа его "перешагивает"

    continue
