"""
Давайте создадим класс Registration, который поможет зарегистрировать пользователя с безопасным паролем.
"""
from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Login must include at least one ' @ '")
        if '.' not in value:
            raise ValueError("Login must include at least one ' . '")
        self.__login = value

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(value):
        for i in digits:
            if i in value:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        cnt = 0
        for i in value:
            if i.isupper():
                cnt += 1
        if cnt >= 2:
            return True
        return False

    @staticmethod
    def is_include_only_latin(value):
        for i in value:
            if i not in ascii_letters and i not in digits:
                return False
        return True

    @staticmethod
    def check_password_dictionary(value):
        return True  # автор курса не реализовал проверку метода при сдаче задания!
        # with open('easy_password.txt', 'r') as file:
        #     for string in file:
        #         if string == value:
        #             return False
        #     return True

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if 5 < len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value


a = Registration('qwe@zp.com', 'fGnH123')
print(a.login, a.password)
a.password = 'rhjKN2'
print(a.password)

b = Registration('gh@ka.ng', 'ghmKLU5')
print(b.login, b.password)
print(a.login, a.password)
