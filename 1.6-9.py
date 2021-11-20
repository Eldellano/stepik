import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):  # класс наследуется от двух других
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)


test = LoggableList()
test.append(2)  # Tue Nov  9 22:22:22 2021: 2
test.append(3)  # Tue Nov  9 22:22:22 2021: 3
print(test)  # [2, 3]
