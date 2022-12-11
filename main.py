#Задание 1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2


print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#Задание 2-3
def get_sign(x):
    if x[0] in '+-':
        return x[0]

arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(arr):
    sign = get_sign(arr[i])
    if arr[i].isdigit() or (sign and arr[i][1:].isdigit()):
        if sign:
            arr[i] = sign + arr[i][1:].zfill(2)
        else:
            arr[i] = arr[i].zfill(2)

        arr.insert(i, '"')
        arr.insert(i + 2, '"')
        i += 2

    i += 1

print(arr)



s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(" ".join(map(lambda x: '"%s"' % __import__('re').sub('\d+', lambda x: f'{x[0]}'.zfill(2), x) if any(map(str.isdigit, x)) else x, s)))
# задание 4

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in my_list:
    print('Привет', position.split()[-1].title(),'!')

# Задание 5
input_list = [57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42,
        96.64, 34.17, 97.45, 40.62, 84.94, 7, 52.23, 93.74, 89, 3.93]

store_id = id(input_list)
print(input_list)

# Задание 5.1
print(f"{'a':-^100}")

end_word:str = ", " 

for i, num in enumerate(input_list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(input_list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

# Задание 5.2
print(f"{'b':-^100}")

print(f"id before sort {store_id}")
input_list.sort()
print(input_list)
print(f"id after sort {id(input_list)}")

if store_id == id(input_list):
    print("In place")
else:
    print("Diff obj")


# Задание 5.3
print(f"{'c':-^100}")

copy_of_list = input_list.copy() 
copy_of_list.sort(reverse=True) 

print(copy_of_list)
print(store_id)
print(id(copy_of_list))

if store_id == id(copy_of_list):
    print("In place")
else:
    print("Diff obj")



# Задание 5.4
print(f"{'d':-^100}")


print("пять самых дорогих товаров", input_list[-6:-1])
