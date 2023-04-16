class Mydisk:
    def __init__(self, vol, st):
        self.vol = vol
        self.st = st

    def __set__(self, instance, vol):
        if vol.isdigit():
            instance.__dict__[self.vol] = vol
        else:
            return self.__set__(instance, input(f'{self.st}: '))


class G:
    __vol = Mydisk('vol', 'error')

    def __init__(self, vol):
        self.__vol = vol

    def task(self):
        v = int(self.vol) * int(self.vol)
        return v


a = G(input('enter: '))
print(a.task())
