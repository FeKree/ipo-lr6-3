kolvo = int(input("Введите количество строк которое вам придется вводить: ")) #Запрашиваем у пользователя количество строк
stroki=[]
if kolvo < 1: #Условие которое проверяет ввели мы корректное количество строк(ПРОВЕРКА) 
    print("Введено некорректное количество строк") #Если мы ввели некорректное количество строк то нам выведет что введено некорректное количество
else: #Иначе если мы ввели корректное количество строк(больше 0), то будет выполняться следующий код(заполнение самих строк) 
    for i in range(0, kolvo): #Цикл для заполнения строк
        stroki.append(str(input(f"Введите {i + 1} строку "))) #Заполнение строк
vse_str = " ".join(stroki) #Объединим все строки в одну(в один текст)
print(vse_str) #Выводит сначала нам всю строку
pr = " " #переменная пробел для подсчетов количества слов
kolvo_slov = 1 #Переменная в которой будет храниться количество слов
for i in vse_str: #Цикл для подсчетов слов
    if i in pr: #Ветвлнение для подсчетоа слов
        kolvo_slov += 1 #При выполнении цикла каждый раз прибавляем переменной значение 1
print(kolvo_slov) #Выводим количество слов(ИТОГ)
