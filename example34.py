"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух
считает, что ритм есть, если число слогов (то есть число гласных букв) в каждой фразе стихотворения
одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются
дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с
клавиатуры. В ответе напишите "Парам пам-пам", если с ритмом всё в порядке, или "Пам парам", если с
ритмом всё не в порядке.
"""

phrase = input("Введите стихотворение: ").lower().split()
lst = [sum(x in "аеёиоуыэюя" for x in phr) for phr in phrase]
if len(set(lst)) == 1:
    res = "Парам пам-пам"
else:
    res = "Пам парам"
print(res)
