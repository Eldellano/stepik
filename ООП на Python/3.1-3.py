"""
Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
* конструктор __init__, принимающий произвольное количество аргументов.
  Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде
  списка;
* переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
  "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены
  по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
* "Пустой вектор", если наш вектор не хранит в себе значения
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
                self.__values.append(str(i))

    def __str__(self):
        if len(self.__values) > 0:
            self.__values.sort()
            out = ', '.join(self.__values)
            return f'Вектор({out})'
        else:
            return 'Пустой вектор'


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"
