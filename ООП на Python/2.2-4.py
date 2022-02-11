"""
 Создайте класс Zebra, внутри которого есть метод which_stripe,
 который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
"""

class Zebra:
    def __init__(self):
        self.cnt = 1

    def which_stripe(self):
        if self.cnt % 2 == 0:
            print('Полоска черная')
        else:
            print('Полоска белая')
        self.cnt += 1



z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"