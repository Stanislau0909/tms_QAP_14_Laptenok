from statistics import mean

#1 Определить переменные всех типов и выведете их на экран
num = 1
num1 = 1.6
aa = "Hello world"
bb = [1, "valera", 2 , "car" , 3 ]
cc = {'name':'Stas', 'age':26}
dd =  {'1', '5', '2', '9', '2', '9', '1'}
ee = ('1', '5', '2', '9', '2', '9', '1')
print(type(num))
print(type(num1))
print(type(aa))
print(type(bb))
print(type(cc))
print(type(dd))
print(type(ee))
# 1.3 Найти значение выражений
x1 = (17 / (2 * 3)) + 2
x2 = 2 + (17 / (2 * 3))
x3 = 19 % 4 + (15 / (2 * 3))
x4 = (15 + 6) - (10 * 4)
x5 = (17 / 2) % (2 * (3**3))
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
#1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран.
neighbour1 = 25
neighbour2 = 35
neighbour3 = 18
neighbours = neighbour1 + neighbour2 + neighbour3
print(neighbours)
# Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.
neighbours1 = neighbour1, neighbour2, neighbour3
print(mean(neighbours1))

#1 Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99
print(int(a))
print(int(b))
#
# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
site = 'www.my_site.com#about'
newSite = site.replace("#", "/")
print(newSite)
# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
word = "strok"
word2 = "ing"
word3 = word + word2
print(word3)
# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
name1 = name.split()
print(' '.join(name1[::-1] ))
# 5 Напишите программу которая удаляет пробел в начале, в конце строки
programDel = " Hello word "
programDel1 = programDel.strip()
print(programDel1)
# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах
# (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a":"25", "1b":"23",
          "2a":"33", "2b":"31",
          "8a":"21", "8b":"19",
          "9a":"18", "9b":"18",
          "11A":"27", "11B":"24"}
print(school)
# 7 Создайте список и извлеките из него списка второй элемент.
notes = [1, "name", "newyear" , "santa" , 28 ]
print(notes[1])
# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
example1 = "employ"
example2 = "employment"
example3 = example1 in example2
print(example3)
# 9 Вывести нужные символы
#x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
x6 = "My name is Agent Smith"
print(x6[1])
print(x6[3:16:3])
# 10* Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
lot = [1, 5, 2, 9, 2, 9, 1]
def fucnc_count(lot):
    return [i for i in lot
            if lot.count(i)<2]
print(fucnc_count(lot))


# PS: создать ПР, использовать git (через терминал), если кто-то уже работал с функциями использовать их при написании дз


