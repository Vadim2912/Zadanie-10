
#Задача 1
duration = int(input("Введите время в секундах "))
day = duration // 86400
hours = (duration % 86400) // 3600
minutes = ((duration % 86400) % 3600) // 60
seconds = ((duration % 86400) % 3600) % 60
if duration > 86400:
      print(day, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
else: 
    if duration > 3600:
      print(hours, 'час', minutes, 'мин', seconds, 'сек')
    else: 
      if duration > 60:
        print(minutes, 'мин', seconds, 'сек')
      else: print(seconds, 'сек')

#Задача 2
print(sum(filter(lambda j: sum(map(int, str(j))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))
print(sum(filter(lambda j: sum(map(int, str(j + 17))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))

#Задача 3
a = ("Процент")
b = ("Процента")
c = ("Процентов")
numbs = {11,12,13,14}
for i in range(100):
    i = i + 1
    if i in numbs:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")
