class multifilter:
    def judge_half(self, pos, neg):
        # допускает элемент, если его допускает хотя бы половина функций (pos >= neg)
        if pos >= neg:
            return self

    def judge_any(self, pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return self

    def judge_all(self, pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return self

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция
        self.pos = 0
        self.neg = 0
        self.judge_any = self.judge_any

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            self.pos, self.neg = 0, 0
            for j in self.funcs:
                if j(i) == True:
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(i, self.pos, self.neg) is not None:
                yield i


# Для тестирования
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
