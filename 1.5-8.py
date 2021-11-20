class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.current = 0
        self.capacity = capacity
    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.current + v <= self.capacity:
            return True
        else:
            return False
    def add(self, v):
        # положить v монет в копилку
        self.current += v
        print(self.current)

x = MoneyBox(15)
x.add(0)
x.add(5)
x.add(9)
x.add(3)