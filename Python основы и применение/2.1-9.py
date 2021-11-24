class PositiveList(list):
    def positive_check(self,x):
        if x > 0:
            return self.append(x)
        else:
            raise NonPositiveError()


pl = PositiveList()
pl.append(1)
print(pl)  # [1]
pl.remove(1)
print(pl)  # []