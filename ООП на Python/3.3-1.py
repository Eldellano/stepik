"""
Вспомним нашего приятеля с предыдущих уроков: класс Vector.
Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
==//==
* переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
 * с целым числом, в результате должен получиться новый Vector, у которого каждый элемент атрибута values
   увеличен на число
 * с другим вектором такой же длины. В результате должен получиться новый Vector, состоящий из суммы элементов,
    расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение
    "Сложение векторов разной длины недопустимо";
 * В случае, если вектор складывается с другим типом(не числом и не вектором), нужны вывести сообщение
   "Вектор нельзя сложить с <значением>"
* переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
 * на целое число. В результате должен получиться новый Vector, у которого каждый элемент атрибута values умножен
   на переданное число;
 * на другой вектор такой же длины. В результате должен получиться новый Vector, состоящий из произведения
   элементов, расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение
   "Умножение векторов разной длины недопустимо";
 * В случае, если вектор умножается с другим типом(не числом и не вектором), нужны вывести сообщение
 "Вектор нельзя умножать с <значением>";
"""


class Vector:
    def __init__(self, *args):
        self.values = args

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        self.__values = []
        for i in value:
            if isinstance(i, int):
                self.__values.append(int(i))

    def __str__(self):
        if self.__values:
            self.__values.sort()
            tmp = (str(i) for i in self.__values)
            out = ', '.join(tmp)
            return f'Вектор({out})'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            tmp_list = []
            for i in self.__values:
                tmp_list.append(int(i) + other)
            return Vector(*(i for i in tmp_list))
        if isinstance(other, Vector):
            if len(self.__values) != len(other.values):
                return 'Сложение векторов разной длины недопустимо'
            cnt = 0  # индекс элемента
            tmp_list = []
            for i in self.__values:
                tmp_list.append(str(int(i) + int(other.__values[cnt])))
                cnt += 1
            return Vector(*(int(i) for i in tmp_list))
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            tmp_list = []
            for i in self.__values:
                tmp_list.append(int(i) * other)
            return Vector(*(i for i in tmp_list))
        if isinstance(other, Vector):
            if len(self.__values) != len(other.values):
                return 'Умножение векторов разной длины недопустимо'
            cnt = 0  # индекс элемента
            tmp_list = []
            for i in self.__values:
                tmp_list.append(str(int(i) * int(other.__values[cnt])))
                cnt += 1
            return Vector(*(int(i) for i in tmp_list))
        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"

v6 = Vector(1)
v7 = v6 + v1
v8 = v1 * v2
print(v8, v1, v2)
v9 = v6 * v1
v5 * 'hi'
