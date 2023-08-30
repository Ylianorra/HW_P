# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# number3 = int(input("Введите третье число: "))
# answer = (number1 + number2)*number3
# print("Сумма введенных чисел: ", answer)


# start = int(input("Сколько кусков пиццы у вас было? "))
# eat = int(input("Сколько кусков пиццы вы съели? "))
# answer = (start - eat)
# print("У вас осталось ", answer, "кусочков пиццы")

# firstname = (input("Введите свое имя: "))
# numyear = int(input("Введите свой возраст: "))
# answer = numyear + 1
# print(firstname, ", в следующем году вам будет ", answer)


# check = int(input("Укажите сумму чека: "))
# countgosti = int(input("Укажите количество гостей: "))
# answer = check/countgosti
# print("Каждый гость должен заплатить по ", answer)

# days = int(input("Введите количество дней: "))
# hours = days *24
# minutes = days * 1440
# secunds = days * 8640
# print("В данном количестве дней ", hours, "часов или ", minutes, "минут или ", secunds, "секунд")

# kilogramm = int(input("Введите количество килограмм: "))
# pound = kilogramm *2.204
# answer = kilogramm*pound
# print("Данное количество килограмм равно ", answer, "фунтов" )

# number1 = int(input("Введите число больше 100: "))
# number2 = int(input("Введите число меньше 10: "))
# answer = number1//number2
# print("Число ", number2, "помещется в числе ", number1, answer, "раз")

# num = int(input("Введите число: "))
# if num > 10:
#  print("This is over 10")
# else:
#  print("This is not over 10")
# if num > 10:
#  print("This is over 10")
# elif num == 10:
#  print("This is equal to 10")
# else:
#  print("This is under 10")

# num = int(input("Введите число: "))
# if num >= 10:
#     if num <= 20:
# print("This is between 10 and 20")
#      else:
#  print("This is over 20")
#     else:
#  print("This is under 10")

# num = int(input("Enter an EVEN number between 1 and 5: "))
# if num <= 1 or num <= 5:
#  print("Thank you")
# else:
#  print("Incorrect")

# Предложите пользователю ввести два числа. Если первое число больше второго, сначала выведите второе число, а потом первое. В противном
# случае выведите сначала первое число, а потом второе

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# if number1 > number2:
#     print(number2, number1)
# else:
#     print(number1, number2)

# Предложите пользователю ввести число, меньшее
# 20. Если введенное число
# больше или равно 20, выведите сообщение «Too high»;
# в противном случае выведите сообщение «Thank you»

# # number1 = int(input("Введите число меньше 20: "))
# # if number1 >= 20:
# #      print("Too high")
# # else:
# #      print("Thank you")


# Предложите пользователю ввести любимый цвет. Если он введет «red», «RED»
# или «Red», выведите сообщение «I like red too». В противном случае выведите сообщение «I don’t like [colour], I prefer red».

# color = (input("Какой ваш любимый цвет? "))
# if color == "Красный" or color == "КРАСНЫЙ" or color == "красный":
#     print("Я тоже люблю ", color)
# else:
#     print("Я не люблю ", color, " цвет. Я предпочитаю красный ")

# wether = (input("На улице дождь? "))
# text = str.lower(text)
#  if wether == "да" or windy == "yes":
#     print(windy = (input("На ветрено? ")))
#     text = str.lower(text)
#     if windy == "да" or windy == "yes":

# else:
#      print("Я не люблю ", color, " цвет. Я предпочитаю красный ")

# windy = (input("На ветрено? "))
# text = str.lower(text)
#  if windy == "да" or windy == "yes":

#  print("Я тоже люблю ", color)
#  else:
#      print("Я не люблю ", color, " цвет. Я предпочитаю красный ")


# raining = input("На улице дождь? ")
# raining = str.lower(raining)
# if raining == "да" or raining == "yes":
#     windy = input("На улице ветрено? ")
#     windy = str.lower(windy)
#     if windy == "да" or windy == "yes":
#         print("Слишком ветрено для зонтика")
#     else:
#          print("Возьми зонтик")
# else:
#     print("Отлично! Хорошего дня!")

# Предложите пользователю
# ввести его возраст. Если
# введенное значение равно
# 18 и более, выведите сообщение «You can vote»; если
# 17 — сообщение «You can
# learn to drive»; если 16 —
# сообщение «You can buy a
# lottery ticket». Если значение
# меньше 16, выведите сообщение «You can go Trickor-Treating».

# age = int(input("Сколько вам лет? "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# elif age < 16:
#     print("You can go Trickor-Treating")


# Предложите пользователю ввести число. Если оно меньше 10, выведите сообщение «Too low»; если число лежит в диапазоне от 10
# до 20 — сообщение «Correct». В остальных случаях выведите сообщение «Too high»

# num = int(input("Введите целое цисло "))
# if num < 10:
#   print("Too low")
# elif num > 10 and num < 20:
#   print("Correct")
# elif num > 20:
#    print("Too high")


# Предложите пользователю ввести значение 1, 2 или 3. Если введено значение 1, выведите сообщение «Thank you»; если 2 — сообщение «Well done»; если 3 — сообщение «Correct». Если введено
# любое другое значение, выведите сообщение «Error message»

# num = int(input("введите значение 1, 2 или 3:  "))
# if num == 1:
#   print("Thank you")
# elif num == 2:
#   print("Well done")
# elif num == 3:
#    print("Correct")
# else:
#     print("Error message")


# name = input("Укажите ваше имя  ")
# long = len(name)
# print(long)

# name = input("Укажите ваше имя  ")
# surname = input("Укажите вашу фамилию ")
# print(name + " " + surname)
# longname = len(name)
# longsurname = len(surname)
# print(longname + longsurname)


# name = input("Укажите ваше имя с маленькой буквы ")
# surname = input("Укажите вашу фамилию с маленькой буквы ")
# name = name.title()
# surname = surname.title()
# fullname = name + " " + surname
# print(fullname)

# poem = input("Введите строку из вашего любимого стихотворения ")
# longpoem = len(poem)
# print("В этой строке содержится", longpoem, "символов")
# start = int(input("Введите начало отрезка, который необходимо вывести  "))
# end = int(input("Введите конец отрезка, который необходимо вывести "))
# part = (poem [start:end])
# print(part)

# name = input("Укажите ваше имя ")
# name = name.upper()
# print(name)

# name = input("Укажите ваше имя ")
# longname = len(name)
# if longname <= 5:
#     surname = input("Укажите вашу фамилию  ")
#     fullname = name + surname
#     fullname = fullname.upper()
#     print(fullname)
# else:
#     name = name.lower()
#     print(name)


# В шифре «поросячья латынь» начальная согласная
# буква слова перемещается в конец слова, и к ней добавляется суффикс «ay». Если слово начинается с гласной, к нему просто
# добавляется суффикс «way». Например, pig превращается в igpay, banana — в ananabay,
# а aardvark — в aardvarkway. Напишите программу,
# которая предлагает пользователю ввести слово и преобразует его в «поросячью латынь». Проследите за тем,
# чтобы новое слово выводилось в нижнем регистре.

# word = input("Введите слово   ")
# word = word.lower()
# first = word[0]
# length = len(word)
# rest = word[1:length]
# if first != "a" or first != "e" or first != "i" or first != "o" or first != "u":
#     newword = rest + first + "ay"
# else:
#     newword = word + "вay"
# print(newword.lower())


import math

# num = float(input("Введите дробное число с тремя знаками после запятой:  "))
# newnum = (num*2)
# print(round(newnum, 2))

# num = int(input("Введите число больше 500:  "))
# sqnum = math.sqrt(num)
# print(round(sqnum, 2))

# pi = math.pi
# print(round(pi, 5))

# num = int(input("Введите радиус круга:  "))
# pi = math.pi
# sqnum = (pi * (num*num))
# print(round(sqnum, 2))

# radius = int(input("Введите радиус цилиндра:  "))
# tall = int(input("Введите высоту цилиндра:  "))
# pi = math.pi
# sqnum = (pi * (radius*radius))
# answer = (sqnum*tall)
# print(round(answer, 3))


# num1 = int(input("Введите первое число:  "))
# num2 = int(input("Введите второе число:  "))
# tseldel = num1 // num2
# delenie = num1%num2

# print("Если разделить ", num1, " на ", num2, " ,получится", tseldel,"с остатком", delenie )

# print("1) Квадрат")
# print("2) Треугольник")
# print()
# menuselection = int(input("Выберетите число 1 или 2 : "))
# if menuselection == 1:
#     square1 = int(input("Укажите сторону квадрата в сантиметрах:  "))
#     square2 = int(input("Укажите вторую сторону квадрата в сантиметрах:  "))
#     aria = square1*square2
#     print("Площадь квадрата равна: ", aria, "сантиметров")
# elif menuselection ==2:
#     base = int(input("Укажите ширину основания треугольника в сантиметрах:  "))
#     tall = int(input("Укажите высоту треугольника в сантиметрах:  "))
#     trin = (tall*base)/2
#     print("Площадь треугольника равна: ", trin, "сантиметров")
# else:
#     print("Введены некорректные данные. Пожалуйста, выберите цифру 1 или 2")


# data = int(input("Введите число от 1 до 12:  "))
# for i in range(1, 13):
#     answer = i * data
#     print(i, "x", data, "=", answer)
import random

# print(lst := [random.randint(0,10) for _ in range(15)])
# new_list = []
# for i in lst:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# Сдвиг на некоторое количество элементов:

# print(lst := [random.randint(0,10) for _ in range(7)])

# shift = int(input('Введите сдвиг: '))
# for i in range(len(lst)):
#     print(lst[(i - shift) % len(lst)], end="  ")



# some_string = input("Введите строеку:  ")

# cnt_dict = {}
# for ch in some_string:
#     if ch in cnt_dict:
#         cnt_dict[ch] += 1
#     else:
#         cnt_dict[ch] = 0
#     print(ch if cnt_dict[ch] < 1 else f'{ch}_{cnt_dict[ch]}')
