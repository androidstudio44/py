class CalculatorAgain:
    
    def sumofPositiveIntegers(n):
        if n < 0:
            print("We are not calculating the sum for negative numbers")
            return None
        else:
            return sum(range(1, n+1))

    def multiplicationTable(num):
        for i in range(1, 11):
            print(f"{i} x {num} = {i*num}")

    def sumOfSquares(i):
        sum_of_squares = 0
        for num in range(1, i+1):
            sum_of_squares += num**2
        print(f"Input number: {i}")
        print(f"The sum of squares from 1 to {i} is {sum_of_squares}.")

        # Класс CalculatorAgain - это класс, который содержит три метода: sumofPositiveIntegers, multiplicationTable и sumOfSquares. Эти методы выполняют различные вычисления, которые могут быть полезными для математических задач.

# Метод sumofPositiveIntegers принимает параметр n и возвращает сумму первых n положительных чисел. Если n меньше нуля, то метод выводит сообщение "We are not calculating the sum for negative numbers" и возвращает значение None.

# Метод multiplicationTable принимает параметр num и выводит таблицу умножения для числа num от 1 до 10.

# Метод sumOfSquares принимает параметр i и вычисляет сумму квадратов чисел от 1 до i. Затем метод выводит сообщение о сумме квадратов от 1 до i.

# Эти методы могут быть использованы для решения различных математических задач. Например, метод sumofPositiveIntegers может использоваться для вычисления суммы всех положительных чисел до заданного числа, метод multiplicationTable может использоваться для
#  вывода таблицы умножения для заданного числа, а метод sumOfSquares может использоваться для вычисления суммы квадратов для различных значений.

class Planets:
    def __init__(self, name='Earth', position=3, moons=1):
        self.__name = name
        self.__position = position
        self.__moons = moons
    
    def details(self):
        print("Name:", self.__name)
        print("Position in Solar System:", self.__position)
        print("Number of Moons:", self.__moons)
planets_data = [
    {'name': 'Mercury', 'position': 1, 'moons': 0},
    {'name': 'Venus', 'position': 2, 'moons': 0},
    {'name': 'Earth', 'position': 3, 'moons': 1},
    {'name': 'Mars', 'position': 4, 'moons': 2},
    {'name': 'Jupiter', 'position': 5, 'moons': 79},
    {'name': 'Saturn', 'position': 6, 'moons': 82},
    {'name': 'Uranus', 'position': 7, 'moons': 27},
    {'name': 'Neptune', 'position': 8, 'moons': 14},
]

for data in planets_data:
    planet = Planets(data['name'], data['position'], data['moons'])
    planet.details()

favourite_planet = Planets('Saturn', 6, 82)
favourite_planet.details()

# Код, который вы предоставили, состоит из класса Planets, который используется для создания объектов, представляющих планеты. Этот класс имеет три переменные, которые хранят имя планеты, ее позицию в солнечной системе и количество ее спутников.

# Метод __init__ класса Planets используется для инициализации объектов класса, когда они создаются. Он имеет три параметра по умолчанию: name (имя планеты), position (позиция планеты в солнечной системе) и moons (количество спутников у планеты). Если значения этих параметров не заданы при создании объекта, они будут установлены в значения по умолчанию.

# Метод details класса Planets используется для вывода информации о планете на экран. Он выводит имя планеты, ее позицию в солнечной системе и количество ее спутников.

# В этом коде также есть список словарей planets_data, который содержит информацию о планетах, таких как имя, позиция и количество спутников. Этот список используется для создания объектов класса Planets для каждой планеты, используя цикл for. Для каждой записи в списке planets_data создается объект класса Planets, и метод details вызывается для вывода информации о планете на экран.



class Students:
    def __init__(self, firstname, lastname, classyear, marks, major):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__classyear = classyear
        self.__marks = marks
        self.__major = major

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_lastname(self):
        return self.__lastname

    def set_classyear(self, classyear):
        current_year = datetime.now().year
        if classyear < (current_year - 100) or classyear > current_year:
            self.__classyear = 0
            print('no such class year exists for us')
        else:
            self.__classyear = classyear

    def get_classyear(self):
        return self.__classyear

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            self.__marks = -1
            print('please give proper marks. this no joke.')
        else:
            self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_major(self, major):
        if len(major) <= 2:
            self.__major = 'NA'
            print('there is no such major or stream in our uni')
        else:
            self.__major = major

    def get_major(self):
        return self.__major

    def generateReport(self):
        print('Report Generated for {} {} of {} - {}'.format(self.get_firstname(), self.get_lastname(),
                                                             self.get_classyear(), self.get_major()))
        if self.get_marks() < 0:
            final_grade = "X"
        elif self.get_marks() >= 90:
            final_grade = "A"
        elif self.get_marks() >= 80:
            final_grade = "B"
        elif self.get_marks() >= 70:
            final_grade = "C"
        elif self.get_marks() >= 60:
            final_grade = "D"
        else:
            final_grade = "F"
        return final_grade

# Creating object of class and setting values
student1 = Students('Mike', 'Ross', 2010, 90, 'law')
student2 = Students('Lucifer', 'Morningstar', 1810, 10001, 'la')

# Calling generateReport method for each object
print('Final Grade of {} is {}'.format(student1.get_firstname(), student1.generateReport()))
print('Final Grade of {} is {}'.format(student2.get_firstname(), student2.generateReport()))


# Код написан на языке Python и создает класс под названием Students для работы со студентами. Внутри класса определены переменные экземпляра, которые не могут быть доступны за пределами класса. Каждый студент имеет имя, фамилию, год поступления, оценки и специализацию (например, Физика, Электротехника).

# Для всех переменных экземпляра класса определены геттеры и сеттеры. При установке значения для оценок устанавливаются правила валидации: оценки не могут быть меньше 0 и больше 100. Если оценка находится за пределами этого диапазона, устанавливается значение -1 и выводится сообщение об ошибке.

# Также есть правила валидации для года поступления и специализации: год поступления не может быть в будущем или быть меньше, чем 100 лет назад. Если год поступления не находится в этом диапазоне, устанавливается значение 0 и выводится сообщение об ошибке. Длина названия специализации должна быть больше 2 символов, и если длина меньше или равна 2, устанавливается значение "NA" и выводится сообщение об ошибке.

# Также в классе определен метод generateReport, который выводит отладочное сообщение в формате "Report Generated for [first name] [last name] of [class year] – major/stream", а затем вычисляет и возвращает итоговую оценку студента. Итоговая оценка вычисляется на основе следующих правил: оценка >= 90 -> "A", оценка >= 80 -> "B", оценка >= 70 -> "C", оценка >= 60 -> "D", оценка < 60 -> "F". Если оценка находится за пределами этого диапазона (0-100), возвращается значение "X".

# Далее, в анонимном блоке кода, создаются как минимум два экземпляра класса Students, устанавливаются все данные для каждого студента с помощью методов set, и вызывается метод generateReport для каждого. Значение, возвращаемое методом generateReport, выводится на экран в формате "Final Grade of [firstName] is [final grade]".

coloursList = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
print(coloursList)

print(len(coloursList))

if 'Red' in coloursList:
    print("Yes, 'Red' is in the list")
else:
    print("No, 'Red' is not in the list")

lastElement = coloursList[-1].upper()
print(lastElement)

coloursList[3] = coloursList[3].upper()
print(coloursList)

colourCodesList = ['#FF0000', '#0000FF', '#00FF00', '#FFFF00', '#800080']

if colourCodesList == coloursList:
    print("Lists are equal")
else:
    print("Lists are not equal")

mergedList = colourCodesList + coloursList
print(mergedList)

# Создаем список с названиями цветов и выводим его на экран
# coloursList = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
# print(coloursList)

# Выводим размер списка
# print(len(coloursList))

# Проверяем, содержится ли в списке цвет "Red"
# if 'Red' in coloursList:
#     print("Да, 'Red' есть в списке")
# else:
#     print("Нет, 'Red' нет в списке")

# Получаем последний элемент списка и выводим его в верхнем регистре
# lastElement = coloursList[-1].upper()
# print(lastElement)

# Переводим четвертый элемент списка в верхний регистр
# coloursList[3] = coloursList[3].upper()
# print(coloursList)

# Создаем другой список с кодами цветов
# colourCodesList = ['#FF0000', '#0000FF', '#00FF00', '#FFFF00', '#800080']

# Сравниваем два списка на равенство
# if colourCodesList == coloursList:
#     print("Списки равны")
# else:
#     print("Списки не равны")

# Объединяем два списка и выводим на экран новый список
# mergedList = colourCodesList + coloursList
# print(mergedList)