"""
Реализуйте класс Wallet, аналог денежного кошелька, содержащий информацию о валюте и остатке имеющихся средств на счете.
"""


class Wallet:
    def __init__(self, currency, balance):
        self.balance = balance
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        for i in currency:
            if not i.isupper():
                raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return self.balance == other.balance
            else:
                raise ValueError('Нельзя сравнить разные валюты')
        else:
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')

    def __add__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return Wallet(other.currency, other.balance + self.balance)
            else:
                raise ValueError('Данная операция запрещена')
        else:
            raise ValueError('Данная операция запрещена')

    def __sub__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return Wallet(other.currency, self.balance - other.balance)
            else:
                raise ValueError('Данная операция запрещена')
        else:
            raise ValueError('Данная операция запрещена')


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
# print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
# wallet7 = wallet2 + wallet3
# print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')
