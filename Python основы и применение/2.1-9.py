class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError()


def test():  # Проверка, не отправлять с решением
    lst = PositiveList([1, 2, 3])
    lst.append(-4)
    print(lst)


test()
