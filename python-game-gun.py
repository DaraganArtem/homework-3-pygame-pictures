from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Bullet():
    """
    Класс снарядов
    Включает в себя классы: Ball-обычные снаряды, и Missile-торпеды.
    """
        
    def __init__(self, x=40, y=450):
        """
        Конструктор класса Bullet
        x - начальное положение снаряда по горизонтали
        y - начальное положение снаряда по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'brown'])
        self.live = 8

    def set_coords(self):
        """
        Функция изменения координат уже нарисованного снаряда
        """
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self, dt):
        """
        Функция вычисляет изменения координат снаряда через единицу времени dt
        """
        self.x += self.vx * dt
        self.y += self.vy * dt

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли снаряд с целью obj
        True в случае столкновения снаряда и цели. В противном случае False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False

    def death(self):
        """
        Функция удаления с экрана снаряда по прошествии его времени жизни
        """
        canv.delete(self.id)


class  Ball(Bullet):
    """
    Подкласс  Ball класса Bullet
    Это обычные снаряды в форме круга
    """
    k = 0.8 #Коэффициент затухания 
    g = 500 #Ускорение свободного падения

    def __init__(self):
        """
        Конструктор класса Ball
        Рисует обычные снаряды в форме круга
        """
        Bullet.__init__(self)
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def change_speed(self, dt):
        """
        Функция изменения направления и величины скоростей шариков при ударах об стенки о пол
        """
        if self.y >= 500:
            self.y = 500
            self.vy = -self.vy * Ball.k
            self.vx = self.vx * Ball.k
        if self.x >= 800:
            self.vx = -self.vx
        self.vy += Ball.g * dt


class Missile(Bullet):
    """
    Подкласс Missle класса Ball
    Торпеды квадратной формы, на которые не действует гравитация
    """
    def __init__(self):
        """
        Конструктор класса Missle
        Рисует торпеды в форме квадратов
        """
        Bullet.__init__(self)
        self.id = canv.create_rectangle(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def change_speed(self, dt):
        pass


class Gun():
    number_of_bullet_types = 2 #Число типов снарядов: обычные и торпеды
    type_of_bullet = 0 #Переменная для обозначения текущего типа снарядов: обычные - 0, торпеды - 1

    def __init__(self):
        """
        Конструктор класса Gun
        f2_power - мощность выстрела
        f2_on - переменная для определения нажата кнопка мыши или нет
        an - угол наклона дула пушки
        id - форма пушки - линия
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        """
        Функция начала стрельбы
        Меняет занчение переменной f2_on с 0 на 1
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел снарядом
        Происходит при отпускании кнопки мыши
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши
        и от того как долго она была зажата
        """
        global balls, bullet
        bullet += 1
        if Gun.type_of_bullet == 0:
            new_ball = Ball()
        if Gun.type_of_bullet == 1:
            new_ball = Missile()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = 10 * self.f2_power * math.cos(self.an)
        new_ball.vy = 10 * self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Прицеливание
        Меняется угол наклона дула пушки в зависимости от положения мыши
        и пушка становится длиннее 
        """
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """
        Функция усиления выстрела
        Чем дольше зажата кнопка мыши - тем больше мощность выстрела
        От этого пушка краснеет
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def change_type_of_bullet(self):
        """ Функция изменения типа снарядов """
        Gun.type_of_bullet = (Gun.type_of_bullet + 1) % Gun.number_of_bullet_types
        

class Target():
    points = 0 #Очки за попадание в цель
    id_points = canv.create_text(30, 30, text=points, font='28') #Вывод числа очков на экран

    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()
        self.vx = rnd(-100, 100, 1)
        self.vy = rnd(-100, 100, 1)

    def new_target(self):
        """ Создание новой цели """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 450)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """ Попадание шарика в цель """
        canv.coords(self.id, -10, -10, -10, -10)
        Target.points += points
        canv.itemconfig(Target.id_points, text=Target.points)

    def move(self, dt):
        """ Перемещение цели """
        if self.x >= 790 or self.x <= 10:
            self.vx = -self.vx
        if self.y >= 500 or self.y <= 10:
            self.vy = -self.vy
        self.x += self.vx * dt
        self.y += self.vy * dt
        canv.coords(self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r
                    )


number_of_targets = 3
targets = [Target() for i in range(number_of_targets)]
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    for t1 in targets:
        t1.new_target()
    bullet = 0
    balls = []
    canv.bind('1', g1.change_type_of_bullet)
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)


def mainloop():
    global bullet
    z = 0.03
    while True:
        for t1 in targets:
            t1.move(z)
            for b in balls:
                b.change_speed(z)
                b.move(z)
                b.set_coords()
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit()
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    for i in range(25):
                        for b in balls:
                            b.change_speed(z)
                            b.move(z)
                            b.set_coords()
                        time.sleep(z)
                        canv.update()
                    bullet = 0
                    canv.itemconfig(screen1, text='')
                    t1.new_target()
                    t1.live = 1
                b.live -= z
                if b.live <= 0 and b.vx <= 0.1:
                    balls.pop(0)
                    b.death()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
mainloop()
