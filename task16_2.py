class Turtle(object):
    x = 10
    y = 10
    s = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go_up(self): # - увеличивает y на s
        self.y += self.s

    def go_down(self): # - уменьшает y на s
        if (self.y - self.s < 0):
            self.y = 0
        else: 
            self.y -= self.s

    def go_left(self): # - уменьшает x на s
        if (self.x - self.s < 0):
            self.x = 0
        else: 
            self.x -= self.s

    def go_right(self): # - увеличивает y на s
        self.x += self.s

    def evolve(self): # - увеличивает s на 1
        self.s += 1

    def degrade(self): # - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if (self.s - 1 <= 0):
            print('нельзя уменьшить скорость до нуля')
        else: 
            self.s -= 1

    def count_moves(self, x2, y2): #  return 0
        cnt = 0
        
        while self.x < x2 and x2 - self.x >= self.s:
            self.go_right()
            print('шаг на x',self.x)
            cnt += 1
        else:
            if self.x < x2 and x2 - self.x != 0:
                self.degrade()
                self.go_right()
                self.evolve()
                cnt += 1
        

        while self.x > x2 and  self.x - x2 >= self.s:
            self.go_left()
            print('шаг на x',self.x)
            cnt += 1
        else:
            if self.x > x2 and self.x - x2 != 0:
                self.evolve()
                self.go_left()
                self.degrade()
                cnt += 1

        while self.y < y2 and y2 - self.y >= self.s:
            self.go_up()
            print('шаг на y',self.y)
            cnt += 1
        else:
            if self.y < y2 and y2 - self.y != 0:
                self.degrade()
                self.go_right()
                self.evolve()
                cnt += 1
        

        while self.y > y2 and  self.y - y2 >= self.s:
            self.go_down()
            print('шаг на y',self.y)
            cnt += 1
        else:
            if self.y > y2 and self.y - y2 != 0:
                self.evolve()
                self.go_left()
                self.degrade()
                cnt += 1
        return cnt

turtle = Turtle(50, 50)

print('шагов', turtle.count_moves(39,40))

