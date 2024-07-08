class BoxOffice(object):
    __amount = 0 
    def __init__(self, amount):
        self.__amount = amount

    def top_up(self, x):
        self.__amount += x

    def get_amount(self):
        return self.__amount
    
    def count_1000(self):
        return self.__amount // 1000

    def take_away(self, x):
        if self.__amount < x:
            print('в кассе недостаточно средств')
        else:
            self.__amount -= x
            print(f'выдано {x}')


boxOffice = BoxOffice(100)
print(boxOffice.get_amount())
boxOffice.top_up(10000)
print(boxOffice.get_amount())
print(boxOffice.count_1000())
boxOffice.take_away(5000)
print(boxOffice.get_amount())
